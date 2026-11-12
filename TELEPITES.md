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
- A nagyított képet ujjal mozgathatod.
- A kerek gomb megállítja a képet (pillanatkép). Ezt tovább nagyíthatod és mozgathatod.
- Az Élő kép gomb eldobja a pillanatképet.
- A Mentés gomb csak akkor ment, ha megnyomod: megnyílik az iPhone megosztó menüje, ott válaszd a Kép mentése lehetőséget.

## Adatvédelem

- A kép csak a telefon memóriájában van, és kilépéskor vagy háttérbe váltáskor törlődik.
- Az app nem küld el semmit sehova. Az app fájljai (nem a képek) a telefonon tárolódnak, hogy internet nélkül is elinduljon.
- Képernyőképet az app nem tud megakadályozni.

## Tudnivalók

- A nagyítás digitális. Az app a legnagyobb elérhető felbontást kéri a kamerától, hogy nagyításkor is éles maradjon.
- Zseblámpa-gomb csak ott jelenik meg, ahol a böngésző engedi. iPhone Safariban általában nincs.
- Új verzió feltöltése után az app a következő indításkor frissül.
