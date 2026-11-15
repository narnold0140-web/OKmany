# Okmányvizsgáló – webapp iPhone-ra

Nem kell hozzá Mac, Xcode vagy App Store. Egy webcímre kell feltölteni (https), és onnan
a Safariból felteszed a Kezdőképernyőre, mint az Nvidia GeForce Now-t.

## 1. Feltöltés (egyszer kell, kb. 2 perc)

A kamerát az iPhone csak biztonságos (https) oldalon engedi, ezért a mappát egy ingyenes
tárhelyre kell tenni. A legegyszerűbb:

**Netlify Drop** (https://app.netlify.com/drop)
1. Csomagold ki a zip fájlt.
2. Húzd rá a kicsomagolt mappát (az `index.html` legyen benne) az oldalra.
3. Kapsz egy https címet. Tartós megtartásához ingyenes Netlify-fiókba kell belépni.

Alternatívák: GitHub Pages vagy Cloudflare Pages (mindkettő ingyenes és tartós).

## 2. Telepítés az iPhone-ra

1. Nyisd meg a kapott címet **Safariban**.
2. Koppints a Megosztás gombra, majd: **Hozzáadás a Kezdőképernyőhöz**.
3. Indítsd a Kezdőképernyőn lévő Okmány ikonról. Teljes képernyőn, app módban nyílik meg.
4. Az első indításkor engedélyezd a kamerát.

## Használat

- Élő képen csípéssel, dupla koppintással, csúszkával vagy az 1×, 2×, 4×, 8× gombokkal nagyítasz.
- Fektetett telefonnal is használható: a vezérlők ilyenkor a jobb oldali sávba kerülnek. Ehhez a Vezérlőközpontban kapcsold ki a tájolás zárolását.
- A nagyított képet ujjal mozgathatod.
- Ha a telefonon több hátlapi kamera van, az Objektív sor gombjaival válthatsz: 0,5× (ultraszéles), 1× (fő), Tele (teleobjektív). A sor csak akkor jelenik meg, ha az eszköz több hátlapi kamerát ad át a böngészőnek.
- Az ultraszéles kamera közelről csak az iPhone 13 Pro és újabb Pro modelleken élesít. Máshol közeli okmányhoz az 1× objektívet használd.
- Az írisz formájú kerek gomb megállítja a képet (pillanatkép). Nyomásra a lamellái összezárnak; Alnyomat-nézetben hullámvonal látszik a közepén, jelezve, hogy ott a feldolgozott képet rögzíti. Ezt tovább nagyíthatod és mozgathatod.
- Az Élő kép gomb eldobja a pillanatképet.
- A Mentés gomb csak akkor ment, ha megnyomod: megnyílik az iPhone megosztó menüje, ott válaszd a Kép mentése lehetőséget.

## Funkciók

- **Legélesebb képkocka:** a pillanatkép gombra az app néhány képkockát rögzít, és a legélesebbet tartja meg.
- **Képszűrők:** Kontraszt, Élesítés, Szürke, Inverz. Az Élesítés az élő képen is látszik, minden nagyításnál, ugyanolyan erősséggel, mint a rögzített képen: nagyítás közben azt látod, amit rögzítés után kapsz. A telefon grafikus processzora számolja; ha egy eszközön ez nem érhető el, ott az élesítés csak a rögzített képen jelenik meg, és az app erre egy rövid felirattal figyelmeztet. A szűrők a mentett képre is rákerülnek.
- **Váltható keret:** a keret gombbal Bankkártya (ID-1) és Útlevél méret között válthatsz.
- **Lupe:** hosszan nyomd az ujjad a képen, és a kép alatt egy kerek nagyító követi. Felengedésre eltűnik.
- **Panel elrejtése:** a panel tetején lévő kis vonalra koppintva a vezérlők eltűnnek, csak a zárógomb marad.
- **Dupla koppintás** az egész képernyőn (a gombokon kívül) 3×-ra nagyít, a következő visszaállítja. Két ujjal csípve a nagyítás az ujjaid között lévő pontnál marad.

## Alnyomat-nézet

A felső sávban a hullámvonal ikonnal kapcsolható. Közeli, mikroszerkezeti vizsgálathoz való (alnyomat, mikroszöveg, guilloche).

- Bekapcsoláskor az app átvált az ultraszéles (0,5×) objektívre, ahol van, kilépéskor visszaáll az előzőre. Közelről ez csak a Pro modelleken élesít.
- **Éles:** erős részletkiemelés. **Vonal:** csak a finom vonalak látszanak szürkén, az alapszín eltűnik.
- A nézet a látott területet a kamera valódi felbontásán dolgozza fel, ezért nagyításkor is valódi részletet mutat.
- A **Stabil** kapcsoló itt is érvényes: nagyításnál a kéz remegését az Alnyomat-nézetben is ellensúlyozza. A kapcsolót a nézetből kilépve, a szűrők sorában találod.
- Az élő képet a telefon grafikus processzora számolja, ezért folyamatos, nem szaggat. Bekapcsoláskor egy rövid „Alnyomat-vizsgáló” felirat jelzi, hogy ebben a nézetben vagy.
- **Felvétel az Alnyomat-nézetben:** a rögzítő gomb itt képernyőfotót készít: pontosan az a feldolgozott kép áll meg, amit a kijelzőn látsz (a választott móddal, Erősséggel, Finomsággal és Inverzzel). A megállított képet tovább nagyíthatod, és két gomb közül választhatsz: **Élő kép** (vissza ugyanoda, ahol voltál) vagy **Mentés**. A felvétel közben a nézet beállításai nem látszanak, mert a megállított képen már nem változtatnak.
- **Inverz:** megfordítja a világos és a sötét részeket. A világos alapon lévő halvány, világos vonalak sötét alapon gyakran jobban kivehetők. Az Éles és a Vonal móddal is működik, a rögzített képre és a mentésre is érvényes.
- **Erősség:** mennyire emelje ki a mintát. Halvány, fakó alnyomatnál told feljebb. Ha a kép szemcsés, zajos, vagy a vonalak körül világos udvar jelenik meg, vedd lejjebb.
- **Finomság:** a csúszka bal szélén a hajszálvékony vonalakra és a mikroszövegre érzékeny, jobbra tolva a vastagabb vonalakra és a nagyobb mintákra. Ha közelről, élesen látsz, hagyd balra. Ha távolabbról nézed, vagy a minta durvább, told jobbra.
- Az **Alap** gomb visszaállítja a kiinduló értékeket. A beállítást a telefon megjegyzi, a rögzített képre és a mentésre is érvényes.
- **Tábla (nyomtatási technika segédtábla):** kilenc lapon mutatja, hogyan néz ki erős nagyításban az okmánygyártásban használt nyomtatás, és hogyan az irodai nyomtató vagy a másolat. A kamerában látott képet a rajzhoz hasonlítod, az Előző és a Tovább gombbal lapozol.
  - Zöld címke (Biztonsági nyomat): ofszet, írisznyomat, metszetmélynyomás, magasnyomás. Az alnyomatban és a díszítő mintákban ezt várod.
  - Fehér címke (Megszemélyesítés): lézergravírozás, hőszublimációs nyomat. A fotónál és az adatoknál fordul elő.
  - Narancs címke (Alnyomatban gyanús): tintasugaras nyomtató, lézernyomtató, raszteres másolat. Ha az alnyomat vagy a díszítő minta ilyen, az hamisítványra utal. A fotónál és az adatoknál viszont eredeti okmányon is előfordulhat, mert sok ország így személyesít meg.
  - A rajzok sematikusak, nem valódi felvételek. Hogy egy adott okmányon melyik technikának hol kell lennie, azt az okmány leírásából (például PRADO) tudod, a tábla csak a felismerést segíti.

## Stabilizálás és folyékony kép

A szűrők sorában két kapcsoló van:

- **Stabil** (alapból be): nagyításnál a kéz remegését digitálisan ellensúlyozza az élő képen. A stabilizált képet az app maga rajzolja ki, így a mozgás sima, nem rángat. A lassú, szándékos mozgást követi, a gyors remegést kiveszi. 1× nagyításnál nem dolgozik, mert ott nincs tartalék a kép szélén. A rögzített képet és a mentést nem érinti. Egyszínű felületen, ahol nincs mihez igazítani, lágyan elengedi a korrekciót.
- **60 fps:** a kamera kisebb felbontáson, de másodpercenként kétszer annyi képkockával megy, ezért a mozgás folyékonyabb. Az ára, hogy erős nagyításnál és a rögzített képen kevesebb a részlet, és többet fogyaszt. Bekapcsoláskor az app kiírja, milyen felbontást és képkockaszámot adott a telefon. A beállítást megjegyzi.

## Fogyasztás és melegedés

- **Sötét kép (v54-től):** ha a kamera 15 másodpercig csak feketét lát (letakart lencse, zseb, arccal lefelé letett telefon), magától kikapcsol, és ezt egy felirat jelzi. A felső kamera gombbal kapcsolható vissza.
- **Okmány felismerése lap (v54-től):** amíg a lap nyitva van, a kamera áll; csak a **Scan** idejére kapcsol be, utána újra leáll. A lap bezárásakor visszaáll az előző állapot (ha előtte ki volt kapcsolva, kikapcsolva marad).

- **Felbontás igény szerint:** élő képen a kamera Full HD-ban fut, mert a kijelző ennél többet úgysem mutat, a 4K pedig négyszer annyi adatot mozgat és melegíti a telefont. 2× nagyítás fölött és a rögzítés pillanatában az app magától teljes felbontásra vált, így a rögzített kép ugyanolyan részletes, mint eddig. Rögzítéskor ezért a kép egy pillanattal később áll meg.
- A gombok és a panel háttere nem elmosott, hanem átlátszatlan: az elmosás a videó mögött minden képkockánál terhelte a grafikus processzort.

- **Kamera ki/be:** a felső sáv első gombjával (kamera ikon) a kamerát teljesen leállíthatod, és ugyanott visszakapcsolhatod. Kikapcsolva a kamera nem fut, a kijelző tetején a kamerajelző pötty is eltűnik, és a telefon nem melegszik tőle. Közben a rögzített kép, a Mintaokmány-tár és az okmányfelismerés használható. Ha háttérbe teszed az appot, kikapcsolt kamerát a visszatérés nem kapcsol be. Bekapcsoláskor az iPhone ritkán újra engedélyt kérhet.

A kamera és az élő kép feldolgozása sok energiát kér, ezért az app csak akkor dolgoztatja a kamerát, amikor kell:

- **Rögzített képnél a kamera pihen.** Amíg a megállított képet vizsgálod, nagyítod vagy mented, a kamera nem dolgozik. Az Élő kép gombra azonnal folytatja.
- **Letett telefonnál szünet.** Ha másfél percig nem érsz a kijelzőhöz, és a kép sem változik (a telefon le van téve), a kamera megáll, és a kijelző is elalhat. Koppintásra folytatja. Kézben tartott telefonnál a kép mindig mozog, ott nem szüneteltet.
- Hosszabb vizsgálatnál a legtakarékosabb, ha rögzíted a képet, és azon dolgozol, nem az élő képen.
- Az app a képkockánkénti számítást úgy végzi, hogy a telefonnak a lehető legkevesebb adatot kelljen mozgatnia: a kamera képét a grafikus processzor kicsinyíti és dolgozza fel, és minden képkockát csak egyszer.
- Az Élesítés, a Stabil, a 60 fps és az Alnyomat-nézet élő képen többletmunkát ad a telefonnak. Ha nincs rájuk szükség, kikapcsolva kevesebbet fogyaszt.

## Okmány felismerése a gépi sorból

A felső sávban az igazolvány ikonnal nyílik. Az app a gépi sorból (MRZ, az okmány alján a << jeleket tartalmazó sorok) felismeri az okmányt, ellenőrzi, és a megfelelő PRADO-oldalra visz.

1. Koppints a **Scan** gombra (v54-től ez az app saját kamerás olvasója; az Élő szöveges beolvasás kikerült).
2. Igazítsd a gépi sort a keretbe, és tartsd mozdulatlanul. Sötétben kapcsold be a **Lámpát**. A gépi sort be is gépelheted a mezőbe.

3. Az app megmutatja:
   - a kiállító országot és az okmány típusát (útlevél, személyi igazolvány, tartózkodási engedély, vízum);
   - a gépi sor adatait (név, okmányszám, állampolgárság, születési dátum, nem, lejárat), hogy összevesd őket az okmányra nyomtatott adatokkal;
   - az ellenőrző számjegyeket mezőnként (✓ vagy ✗), és ha az okmány lejárt.
4. A **PRADO** gomb a kiállító ország megfelelő okmánykategóriájának oldalát nyitja meg. Alatta ugyanennek a kiállítónak a többi kategóriája és az összes okmánya is elérhető.

Tudnivalók:
- A Scan beolvasását az iPhone saját szövegfelismerője végzi (iOS 15-től, iPhone XS és újabb), a kamerás olvasást az app saját olvasója. Az app a gépi sort csak a memóriában tartja, nem menti és nem küldi el; bezáráskor és háttérbe váltáskor törli.
- **Eltérés az ellenőrző számjegyekben:** lehet beolvasási hiba is. Hasonlítsd össze a mezőt a gépi sorral, főleg a könnyen összetéveszthető karaktereket (O és 0, I és 1, B és 8, S és 5, Z és 2). Ha a beolvasás biztosan pontos, az eltérés átírt adatra utalhat.
- A szövegfelismerő a hosszú << sorokban gyakran kevesebb vagy több kitöltőjelet ad vissza, és egy sort néha két darabra tör. Az app ezt pótolja, illetve összeilleszti, és csak akkor fogadja el, ha az ellenőrző számjegyek igazolják; erről külön üzenetet ír. Ha egy sor nagyon hiányos, megmutatja soronként, hány karakter érkezett.
- Az okmányszámban az app szándékosan nem javít semmit automatikusan, mert ott betű és szám is szabályos lehet, és egy átírt adatot is „rendbe tehetne”. A dátumokban, ahol betű nem állhat, a betűt számjegynek olvassa (például O → 0), de ezt narancssárgán jelzi.
- Ha az ellenőrző számjegyek stimmelnek, az csak azt jelenti, hogy a gépi sor önmagában ellentmondásmentes. Egy jól elkészített hamisítványon is stimmelhetnek, ezért ez nem helyettesíti az okmány vizsgálatát.
- A típus a dokumentumkódból becsült: kártyaformátumú okmányoknál (személyi igazolvány, tartózkodási engedély) nem mindig egyértelmű, ezért a többi kategória is elérhető. Ha a PRADO-ban a kiállítónak nincs ilyen kategóriája, hibaoldal jelenik meg: ilyenkor nyisd meg az összes okmányát.

## Belépési feltételek (v51-től)

Az okmány felismerése után az eredmény alatt egy **Belépési feltételek** kártya jelenik meg, a gépi sor állampolgársága és okmánytípusa alapján:
- **Szabad mozgás joga**: uniós, EGT-s (Izland, Norvégia, Liechtenstein) vagy svájci állampolgár.
- **Vízummentes** vagy **Vízumköteles**, és közvetlenül alatta kiemelve a **tartózkodási idő** (v52-től): vízummentesnél 90 nap bármely 180 napon belül; vízumkötelesnél a vízum „Tartózkodás időtartama” mezője szerint (C vízummal legfeljebb 90/180, D vízummal vagy tartózkodási engedéllyel a kiállító országban az érvényesség alatt); uniós/EGT/svájci polgárnál nincs 90/180 napos korlát. Vízum gépi sorának beolvasásakor a vízumbélyeg mezőire utal.
- A státusz az uniós vízumlista (2018/1806 rendelet) szerint. Külön jelzés: csak biometrikus útlevéllel mentes országok, a szerb Koordinációs Igazgatóság útlevele, Tajvan, Hongkong/Makaó, a brit tengerentúli jogállások, a grúz diplomata-, szolgálati és hivatalos útlevelek felfüggesztése (2026. 03. 06-tól 12 hónapig).
- **Repülőtéri tranzitvízum** az érintett 12 országnál.
- Schengeni ország által kiadott **tartózkodási engedély**, illetve uniós polgár **családtagja** (emlékeztető).
- **Különleges jogállás** (hontalan, menekült, ENSZ stb.), **diplomata- / szolgálati útlevél**, **3 hónapon belül lejáró** útlevél, **kiskorú**.

A lista a felhasználó által küldött magyar szövegen alapul, a hatályos állapotra igazítva: Koszovó 2024. 01. 01. óta vízummentes, Vanuatu 2025. 02. 03. óta vízumköteles, az Egyesült Királyság vízummentes, Észak-Macedónia új néven. A kártya alján látszik a lista dátuma; fél év után az app figyelmeztet, hogy frissíteni kell. Ez gyors tájékoztató, nem helyettesíti a hatályos jogszabályt és a belső utasításokat.

**Automatikus figyelés:** a csomagban lévő `.github/workflows/vizumlista-figyelo.yml` hetente megnézi az EUR-Lexen, van-e új hatályos változata a vízumlistának. Ha van, nyit egy Issue-t a repóban, és erről a GitHub e-mailt küld. Ilyenkor kérd meg Claude-ot a lista frissítésére. Ha a `.github` mappa feltöltése a GitHub weboldalán nem megy (a ponttal kezdődő mappák néha kimaradnak), hozd létre kézzel: **Add file → Create new file**, a név `.github/workflows/vizumlista-figyelo.yml`, és másold bele a fájl tartalmát; ugyanígy a `.github/vizumlista-allapot.txt` fájlt `2025-12-30` tartalommal. Az **Actions** fülön a **Run workflow** gombbal kézzel is kipróbálható.

**Gyorsabb olvasás (v55-től):** a kamera a Scan indításakor egyből teljes felbontásban indul, az olvasó kb. négyszer gyorsabban dolgozik fel egy képet, és sűrűbben olvas. A „Másik kategória” gombok közül az „Egyéb úti okmány” kikerült; a sorrend: Személyi igazolvány, Tartózkodási engedély, Úti okmány külföldinek, Vízum.

## Mintaokmány-tár

A felső sávban a rétegek ikonnal nyitható. Itt saját mintaképeket tölthetsz be (Minta hozzáadása), és az okmány méretét is megadod, így a keret erre igazodik.

- **Átfedés:** a minta átlátszóan a kereten jelenik meg az élő képen. Az átlátszóságot a felül megjelenő csúszkával állítod.
- **Egymás mellett:** a képernyő két félre oszlik, fent az élő kép, lent a minta. A nagyítás és a mozgatás közös, tehát ugyanazt a részletet látod mindkét helyen.
- **Lista:** a minta szerkesztésénél soronként felírhatod az ellenőrzendő elemeket (például „Hologram a fotó mellett”). Összehasonlítás közben a Lista gombbal pipálható ellenőrzőlistaként jelenik meg. A pipák nem maradnak meg, a következő használatnál tiszta lappal indul.
- A minta képét vágd az okmány széléig, hogy pontosan illeszkedjen a keretbe.
- A minta színe eltérhet az eredetitől, ezért a színegyezés önmagában nem döntheti el, hogy az okmány eredeti-e.

**Fontos a forrásról:** az app nem tartalmaz PRADO-képet. A Tanács oldala szerint a PRADO-anyagok másolása, terjesztése és keretezése írásos engedélyhez kötött, a hivatkozás szabad. Ezért csak olyan mintaképet tölts be, amelynek használatára jogod van (saját, vagy a szervezeted által rendelkezésre bocsátott). A PRADO megnyitása gomb csak hivatkozás az oldalra.

A mintaképek csak a telefonon tárolódnak (az app böngészőtárolójában), nem kerülnek fel sehova. Tölts be mintaokmányt (specimen), valódi személy okmányát ne. Ha a Kezdőképernyőről telepített appot törlöd, a minták is törlődnek.

## Adatvédelem

- A kép csak a telefon memóriájában van, és kilépéskor vagy háttérbe váltáskor törlődik.
- Az app nem küld el semmit sehova. Az app fájljai, a választott keretméret, a kameramód, az Alnyomat-nézet két csúszkájának állása és az általad betöltött mintaképek a telefonon tárolódnak, hogy internet nélkül is elinduljon. A vizsgált okmányról készült képet az app nem tárolja.
- Képernyőképet az app nem tud megakadályozni.

## Tudnivalók

- A nagyítás digitális. Az app a legnagyobb elérhető felbontást kéri a kamerától, hogy nagyításkor is éles maradjon.
- A zseblámpa gomb a felső sávban akkor jelenik meg, ha a telefon az éppen használt objektívhez enged vakuvezérlést (jellemzően a fő kameránál). Más objektívre váltva eltűnhet, visszaváltva újra megjelenik.
- A kezdőlap alján látszik a verziószám. Ha feltöltés után még a régi számot látod, zárd be teljesen az appot, és nyisd meg újra.
- Új verzió feltöltése után az app a következő indításkor frissül.
