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
- Az app nem küld el semmit sehova. Az app fájljai, a keret beállítása (méret, elforgatás) és az általad betöltött mintaképek a telefonon tárolódnak, hogy internet nélkül is elinduljon. A vizsgált okmányról készült képet az app nem tárolja.
- Képernyőképet az app nem tud megakadályozni.

## Tudnivalók

- A nagyítás digitális. Az app a legnagyobb elérhető felbontást kéri a kamerától, hogy nagyításkor is éles maradjon.
- Zseblámpa-gomb csak ott jelenik meg, ahol a böngésző engedi. iPhone Safariban általában nincs.
- Új verzió feltöltése után az app a következő indításkor frissül.
