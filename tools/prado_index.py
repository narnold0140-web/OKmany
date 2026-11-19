#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PRADO-index készítő az Okmányvizsgáló apphoz.

Mit csinál: végigmegy a PRADO összes kiállító országán, megszámolja, hány okmányminta van
kategóriánként (útlevél, személyi, vezetői engedély ...), és ebből hány ÉRVÉNYES
(a PRADO adatlapján „Valid: yes”). Az eredményt (prado-index.json) feltölti a GitHubra,
ahonnan az app magától letölti.

Miért a saját gépről: a PRADO a felhőszolgáltatók (pl. GitHub) gépeit letiltja,
otthoni internetről viszont elérhető.

Futtatás:  python3 prado_index.py            (minden ország, feltöltéssel)
           python3 prado_index.py --orszag HUN,SRB --nincs-feltoltes   (próba)
Feltöltéshez egy GitHub-token kell a script melletti github-token.txt fájlban
(vagy az OKMANY_TOKEN környezeti változóban). Csak a Python alapkönyvtárát használja.
"""
import argparse, base64, datetime, html, json, os, re, sys, threading, time, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor

BASE = os.environ.get('PRADO_BASE', 'https://www.consilium.europa.eu/prado/en/')   # tesztelésnél felülírható
REPO = 'narnold0140-web/OKmany'
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, 'prado-cache.json')
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15'
# minta-adatlap hivatkozása: abszolút (…/prado/en/HUN-PB-04001/index.html) vagy relatív (../../HUN-PB-04001/index.html) is lehet
DOC_RE = re.compile(r'(?<![A-Z0-9-])([A-Z]{3}-[A-Z]{2}-\d{3,6})/index\.html', re.I)
CTRY_RE = re.compile(r'prado-documents/([A-Z]{3})/index\.html', re.I)
RECHECK_DAYS = 30          # ennyi nap után az érvényesnek tárolt mintát újra megnézi
DELAY = 0.3                # kis szünet kérésenként (szálanként)
SLOCK = threading.Lock()
THREADS = 3                # ennyi adatlapot kér le egyszerre (kíméletes tempó: a PRADO a sok gépi kérést elutasítja)
WAIT_K = float(os.environ.get('PRADO_WAIT_K', '1'))   # újrapróbálási várakozás szorzója (teszthez)


# Csak azokat a kategóriákat nézzük, amelyeket az app gombként megjelenít: így jóval kevesebb adatlapot kell megnyitni.
# Uniós és schengeni kiállító: útlevél (A), személyi (B), vízum (C), tartózkodási (H), úti okmány külföldinek (J).
# Harmadik ország: útlevél (A) és vezetői engedély (F).
EU_SCH = set('AUT BEL BGR HRV CYP CZE DNK EST FIN FRA D DEU GRC HUN IRL ITA LVA LTU LUX MLT NLD POL PRT ROU SVK SVN ESP SWE ISL LIE NOR CHE'.split())
def wanted(country):
    return set('ABCHJ') if country in EU_SCH else set('AF')


def log(*a):
    print(*a, flush=True)


def get(url, tries=5):
    """Oldal letöltése újrapróbálással: a PRADO sokszor elutasít egy-egy kérést (403/429/5xx)."""
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'en'})
            with urllib.request.urlopen(req, timeout=40) as r:
                data = r.read().decode('utf-8', 'replace')
            time.sleep(DELAY)
            return data
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            wait = (1.5 + 2 * i * i) * WAIT_K
        except Exception:
            wait = (1.5 + 2 * i * i) * WAIT_K
        time.sleep(wait)
    return None


def text_of(page):
    return html.unescape(re.sub(r'<[^>]+>', ' ', page))


def parse_validity(page):
    """('yes'|'no'|None, 'NN/NN/NNNN'|None) az okmány adatlapjáról."""
    t = re.sub(r'\s+', ' ', text_of(page))
    m = re.search(r'(?<![A-Za-z])Valid\s*:\s*(yes|no)\b', t, re.I)
    d = re.search(r'Not valid after\s*:\s*(\d{2}/\d{2}/\d{4})', t, re.I)
    return (m.group(1).lower() if m else None), (d.group(1) if d else None)


def expired(dstr):
    try:
        return datetime.datetime.strptime(dstr, '%d/%m/%Y').date() < datetime.date.today()
    except Exception:
        return False


def load_json(path, default):
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return default


def doc_valid(code, cache, stats):
    """Igaz, ha a minta érvényes; a tárolt eredményt használja, amíg lehet."""
    c = cache.get(code)
    today = datetime.date.today()
    if c:
        if c.get('v') == 'no':
            return False                                         # a visszavont minta nem válik újra érvényessé
        if c.get('until') and expired(c['until']):
            c['v'] = 'no'; return False
        if c.get('v') == 'yes' and (today - datetime.date.fromisoformat(c['t'])).days < RECHECK_DAYS:
            return True
    page = get(BASE + code + '/index.html')
    if page is None:
        with SLOCK: stats['hiba'] += 1
        return c.get('v') != 'no' if c else True                # nem elérhető: a korábbi állapot (vagy érvényes) marad
    v, until = parse_validity(page)
    if until and expired(until):
        v = 'no'                                                 # a lejárati dátum elmúlt: nem érvényes, bármit mutat a jelölés
    if v is None:
        with SLOCK: stats['ismeretlen'] += 1
        v = 'yes'                                                # ha nincs jelölés, a mintát nem vesszük el
    cache[code] = {'v': v, 'until': until, 't': today.isoformat()}
    with SLOCK: stats['letoltve'] += 1
    return v == 'yes'


def country_codes():
    page = get(BASE + 'search-by-document-country.html') or ''
    codes = sorted(set(c.upper() for c in CTRY_RE.findall(page)))
    return codes


def doc_codes(page, code):
    return set(c.upper() for c in DOC_RE.findall(page or '') if c.upper().startswith(code + '-'))


def country_docs(code):
    """Az ország összes mintájának kódja. Előbb az „összes okmány” listát nézi; ha az üres vagy nem elérhető,
    akkor az ország kategóriáit egyenként (és a kategórián belüli típuslistákat is)."""
    page = get(BASE + 'prado-documents/%s/all/docs-all.html' % code)
    docs = doc_codes(page, code)
    if docs:
        return sorted(docs)
    idx = get(BASE + 'prado-documents/%s/index.html' % code)
    if idx is None:
        return None
    cats = sorted(set(k.upper() for k in re.findall(r'prado-documents/%s/([A-Z])/docs-per-category\.html' % code, idx, re.I)))
    ok = 0
    for k in cats:
        cp = get(BASE + 'prado-documents/%s/%s/docs-per-category.html' % (code, k))
        if cp is None:
            continue
        ok += 1
        docs |= doc_codes(cp, code)
        for t in sorted(set(x.upper() for x in re.findall(r'prado-documents/%s/%s/([A-Z])/docs-per-type\.html' % (code, k), cp, re.I))):
            docs |= doc_codes(get(BASE + 'prado-documents/%s/%s/%s/docs-per-type.html' % (code, k, t)), code)
    if cats and not ok:
        return None                                              # egyik kategória sem volt elérhető: sikertelennek számít
    return sorted(docs)


def gh(method, path, token, body=None):
    req = urllib.request.Request('https://api.github.com/repos/%s/%s' % (REPO, path), method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={'Authorization': 'Bearer ' + token, 'Accept': 'application/vnd.github+json',
                                          'User-Agent': 'okmany-prado-index'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def read_token():
    t = os.environ.get('OKMANY_TOKEN', '').strip()
    if not t:
        try:
            with open(os.path.join(HERE, 'github-token.txt'), encoding='utf-8') as f:
                t = f.read().strip()
        except Exception:
            pass
    return t


def main():
    global DELAY
    try:   # Windows-konzolon és naplófájlba írva is maradjanak meg az ékezetek
        sys.stdout.reconfigure(encoding='utf-8', errors='replace'); sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    ap = argparse.ArgumentParser(description='PRADO-index készítő (Okmányvizsgáló)')
    ap.add_argument('--orszag', help='csak ezek az országok, vesszővel (pl. HUN,SRB)')
    ap.add_argument('--nincs-feltoltes', action='store_true', help='csak helyben menti, nem tölti fel')
    ap.add_argument('--tempo', type=float, default=DELAY, help='szünet két kérés között (mp)')
    a = ap.parse_args()
    DELAY = a.tempo
    token = read_token()
    if not a.nincs_feltoltes and not token:
        log('Nincs GitHub-token (github-token.txt). Próbafuttatáshoz: --nincs-feltoltes'); return 2

    # a jelenlegi index a GitHubról: a sikertelen országok adatai ebből maradnak meg
    old, sha = {}, None
    if token:
        try:
            f = gh('GET', 'contents/prado-index.json', token)
            sha = f['sha']; old = json.loads(base64.b64decode(f['content']).decode('utf-8'))
        except Exception as e:
            log('A régi index nem olvasható a GitHubról:', e)
    cache = load_json(CACHE, {})

    codes = [c.strip().upper() for c in a.orszag.split(',')] if a.orszag else country_codes()
    if not codes:
        log('A PRADO országlistája nem érhető el. Próbáld később.'); return 1
    log('Országok:', len(codes))
    out, failed = {}, []
    stats = {'letoltve': 0, 'hiba': 0, 'ismeretlen': 0}
    t0 = time.time()
    for i, c in enumerate(codes, 1):
        docs = country_docs(c)
        if not docs:
            failed.append(c)
            if c in (old.get('countries') or {}): out[c] = old['countries'][c]
            log('[%d/%d] %s: nem elérhető' % (i, len(codes), c)); continue
        docs = [d for d in docs if d[4] in wanted(c)]       # csak az appban megjelenő kategóriák
        cats = {}
        done = [0]; lock = threading.Lock()
        def one(d):
            v = doc_valid(d, cache, stats)
            with lock:
                done[0] += 1
                if done[0] % 10 == 0 or done[0] == len(docs):
                    print('\r   %s: %d/%d adatlap' % (c, done[0], len(docs)), end='', flush=True)
            return d, v
        with ThreadPoolExecutor(THREADS) as ex:
            res = list(ex.map(one, docs))
        print('\r', end='')
        for d, v in res:
            k = d[4]                                             # pl. HUN-AO-02001 -> A (útlevél)
            e = cats.setdefault(k, {'v': 0, 'n': 0})
            e['n'] += 1
            if v: e['v'] += 1
        out[c] = cats
        log('[%d/%d] %s: %d minta, ebből érvényes %d  (%.0f perc)' % (i, len(codes), c, len(docs), sum(x['v'] for x in cats.values()), (time.time() - t0) / 60))
        with open(CACHE, 'w', encoding='utf-8') as f: json.dump(dict(cache), f)   # minden ország után mentjük: megszakítás után innen folytatja
    with open(CACHE, 'w', encoding='utf-8') as f: json.dump(cache, f)

    if not a.orszag and len(failed) > max(5, len(codes) * 0.3):
        log('Túl sok ország nem volt elérhető (%d/%d): az index nem frissül.' % (len(failed), len(codes))); return 1
    if a.orszag:                                                 # részleges futás: a többi ország marad a régiből
        merged = dict(old.get('countries') or {}); merged.update(out); out = merged
    res = {'updated': datetime.date.today().isoformat(), 'source': BASE, 'format': 'v/n = érvényes / összes minta kategóriánként',
           'countries': dict(sorted(out.items())), 'failed': failed}
    body = json.dumps(res, ensure_ascii=False, indent=0)
    with open(os.path.join(HERE, 'prado-index.json'), 'w', encoding='utf-8') as f: f.write(body)
    log('Kész: %d ország, sikertelen: %s | letöltött adatlap: %d, hiba: %d, jelölés nélküli: %d' % (len(out), ' '.join(failed) or '-', stats['letoltve'], stats['hiba'], stats['ismeretlen']))
    if a.nincs_feltoltes:
        log('Mentve: tools/prado-index.json (nem töltöttem fel).'); return 0
    gh('PUT', 'contents/prado-index.json', token, {'message': 'PRADO-index frissítése (%s)' % res['updated'],
       'content': base64.b64encode(body.encode('utf-8')).decode(), **({'sha': sha} if sha else {})})
    log('Feltöltve a GitHubra; az app a következő indításkor már ezt használja.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
