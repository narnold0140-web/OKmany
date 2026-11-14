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
- A kerek gomb megállítja a képet (pillanatkép). Ezt tovább nagyíthatod és mozgathatod.
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
- A Mentés a feldolgozott képet menti, amit éppen látsz.
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

A kamera és az élő kép feldolgozása sok energiát kér, ezért az app csak akkor dolgoztatja a kamerát, amikor kell:

- **Rögzített képnél a kamera pihen.** Amíg a megállított képet vizsgálod, nagyítod vagy mented, a kamera nem dolgozik. Az Élő kép gombra azonnal folytatja.
- **Letett telefonnál szünet.** Ha másfél percig nem érsz a kijelzőhöz, és a kép sem változik (a telefon le van téve), a kamera megáll, és a kijelző is elalhat. Koppintásra folytatja. Kézben tartott telefonnál a kép mindig mozog, ott nem szüneteltet.
- Hosszabb vizsgálatnál a legtakarékosabb, ha rögzíted a képet, és azon dolgozol, nem az élő képen.
- Az app a képkockánkénti számítást úgy végzi, hogy a telefonnak a lehető legkevesebb adatot kelljen mozgatnia: a kamera képét a grafikus processzor kicsinyíti és dolgozza fel, és minden képkockát csak egyszer.
- Az Élesítés, a Stabil, a 60 fps és az Alnyomat-nézet élő képen többletmunkát ad a telefonnak. Ha nincs rájuk szükség, kikapcsolva kevesebbet fogyaszt.

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
