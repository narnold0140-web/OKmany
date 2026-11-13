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
- **Tükröződés-jelző:** a napocska gombbal kapcsolható. A kiégett, fényvisszaverő foltokat narancssárgán jelöli az élő képen, és ha a keretben sok van belőlük, a felső sávban figyelmeztet. Dönts a telefonnal, amíg el nem tűnnek.
- **Képszűrők:** Kontraszt, Élesítés, Szürke, Inverz. Az Élesítés csak a rögzített képen látszik. A szűrők a mentett képre is rákerülnek.
- **Váltható keret:** a keret gombbal Bankkártya (ID-1), Útlevél és Saját méret között válthatsz, a környíl gombbal elforgathatod.
- **Lupe:** hosszan nyomd az ujjad a képen, és a kép alatt egy kerek nagyító követi. Felengedésre eltűnik.
- **Panel elrejtése:** a panel tetején lévő kis vonalra koppintva a vezérlők eltűnnek, csak a zárógomb marad.
- **Dupla koppintás** az egész képernyőn (a gombokon kívül) 3×-ra nagyít, a következő visszaállítja. Két ujjal csípve a nagyítás az ujjaid között lévő pontnál marad.

## Alnyomat-nézet

A felső sávban a hullámvonal ikonnal kapcsolható. Közeli, mikroszerkezeti vizsgálathoz való (alnyomat, mikroszöveg, guilloche).

- Bekapcsoláskor az app átvált az ultraszéles (0,5×) objektívre, ahol van, kilépéskor visszaáll az előzőre. Közelről ez csak a Pro modelleken élesít.
- **Éles:** erős részletkiemelés. **Vonal:** csak a finom vonalak látszanak szürkén, az alapszín eltűnik. **Szivárvány:** felerősített színek, a színváltó (OVD) festékek és az átmenetes nyomat kiemeléséhez.
- A nézet a látott területet a kamera valódi felbontásán dolgozza fel, ezért nagyításkor is valódi részletet mutat.
- A Mentés a feldolgozott képet menti, amit éppen látsz.

## Vízjel-nézet

A felső sávban a csepp ikonnal kapcsolható. Átvilágításos vizsgálathoz való: a halvány árnyalatkülönbségeket emeli ki, így előjön a vízjel, a biztonsági szál, és az is, ha a papírt kikaparták, elvékonyították vagy foltozták.

1. Tartsd az okmány lapját lámpa, világos ablak vagy világító képernyő elé, hogy a fény átvilágítson rajta.
2. Kapcsold be a Vízjel-nézetet. A kép szürke lesz, a halvány foltok erős kontraszttal jelennek meg.
3. Az **Erősség** csúszkával állítsd be, mennyire emelje ki. Ha a kép zajos, vedd lejjebb.

- Az egyenetlen megvilágítást az app kiegyenlíti, a sötét nyomatot (szöveg, vonalak) elhalványítja, hogy a vízjel látsszon.
- Nagyítás, mozgatás, pillanatkép és Mentés itt is működik, a Mentés a kiemelt képet menti.
- A fóliázott adatoldalon (kártya, polikarbonát lap) nincs papírvízjel, ott ez a nézet keveset mutat. A belső papírlapokon és a papíralapú okmányokon hasznos.
- A túl erős, kiégett háttérfény elnyomja a vízjelet: tompább, egyenletes fény jobb.
- Ez vizuális segéd, nem ítélet: a látott vízjelet hasonlítsd a Mintaokmány-tár képéhez vagy a PRADO leírásához.

## Sorvezető

A felső sávban a vonalzó ikonnal kapcsolható. Egy egyenes vonal jelenik meg a képen, amely a képhez tapad: nagyításkor és mozgatáskor ugyanott marad az okmányon. Élő és rögzített képen is működik, de rögzített képen pontosabb.

- A két **karikát** húzva állítod be a vonal két végét, a középső **pöttyel** az egész vonalat tolod arrébb.
- Tedd egy szövegsor aljára: az eredeti nyomat betűi mind a vonalon ülnek, az utólag beírt karakterek kilógnak vagy megdőlnek.
- **Nullázás:** rögzíti a vonal irányát (például az okmány szélén). Ha ezután a vonalat egy másik sorra vagy a fotó szélére teszed, a felirat az eltérést mutatja fokban (Δ). Így látszik, ha egy sor vagy a fotó nem párhuzamos az okmány szélével.
- **Párhuzamos:** egy második, azonos irányú vonalat ad, a pöttyével állítod a távolságát. Sorközök és két él párhuzamosságának ellenőrzésére.
- **Vízszintes:** visszateszi a vonalat a kép közepére.
- Nullázás nélkül a szög a telefon képernyőjéhez képest értendő, ezért önmagában nem sokat mond: mindig az okmány egy éléhez viszonyíts. A vonal a mentett képre nem kerül rá.

## Stabilizálás és folyékony kép

A szűrők sorában két kapcsoló van:

- **Stabil** (alapból be): nagyításnál a kéz remegését digitálisan ellensúlyozza az élő képen. A lassú, szándékos mozgást követi, a gyors remegést kiveszi. 1× nagyításnál nem dolgozik, mert ott nincs tartalék a kép szélén. A rögzített képet és a mentést nem érinti. Egyszínű felületen, ahol nincs mihez igazítani, magától kikapcsol.
- **60 fps:** a kamera kisebb felbontáson, de másodpercenként kétszer annyi képkockával megy, ezért a mozgás folyékonyabb. Az ára, hogy erős nagyításnál és a rögzített képen kevesebb a részlet. Apró részletek vizsgálatához kapcsold ki. Bekapcsoláskor az app kiírja, milyen felbontást és képkockaszámot adott a telefon, mert nem minden modell és objektív tud 60-at. A beállítást az app megjegyzi.

## Állvány-mód

A szűrők sorában az **Állvány** kapcsolóval indul. Akkor használd, ha a telefon fixen áll (állványon, tartóban vagy egy polc szélén), és az okmányokat alá teszed. Két kezed szabad marad.

1. Rögzítsd a telefont, kapcsold be az Állvány-módot, és hagyd üresen alatta a felületet egy pillanatra. Az app megjegyzi a hátteret, és szól, ha kész.
2. Tedd be az okmányt, és vedd ki a kezed a képből. Amikor a kép megnyugszik, az app magától rögzít (a legélesebb képkockát tartja meg).
3. A rögzített képet nagyíthatod, vizsgálhatod. Ha elveszed az okmányt, az app visszavált élő képre, és várja a következőt.

- Ha üres állapot nélkül cserélsz okmányt, az új okmányt is rögzíti.
- Ha kézzel visszaváltasz élő képre, amíg az okmány ott van, nem rögzít újra, csak ha változik a kép.
- A lassú fényváltozáshoz igazodik. Ha a telefont elmozdítod vagy objektívet váltasz, kapcsold ki és be, hogy újra megjegyezze a hátteret.
- Egyszínű, az okmánytól elütő háttéren működik a legjobban. Ha a kezed mozdulatlanul a képben marad, azt is okmánynak nézheti.

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
- Az app nem küld el semmit sehova. Az app fájljai, a keret beállítása (méret, elforgatás), a 60 fps kapcsoló állása és az általad betöltött mintaképek a telefonon tárolódnak, hogy internet nélkül is elinduljon. A vizsgált okmányról készült képet az app nem tárolja.
- Képernyőképet az app nem tud megakadályozni.

## Tudnivalók

- A nagyítás digitális. Az app a legnagyobb elérhető felbontást kéri a kamerától, hogy nagyításkor is éles maradjon.
- Zseblámpa-gomb csak ott jelenik meg, ahol a böngésző engedi. iPhone Safariban általában nincs.
- Új verzió feltöltése után az app a következő indításkor frissül.
