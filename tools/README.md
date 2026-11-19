# PRADO-index gyűjtő (prado_index.py)

Az app a PRADO-gombok mellett zárójelben mutatja, hány **érvényes (vissza nem vont)** okmányminta van
az adott országnál és kategóriában. Ezt a `prado-index.json` fájlból veszi, amelyet ez a program készít.

A PRADO a felhőszolgáltatók gépeit (például a GitHubét) letiltja, ezért a gyűjtő a saját
számítógépedről fut, otthoni internetről.

## Mit csinál
1. Lekéri a PRADO összes kiállító országát.
2. Országonként végignézi az összes okmánymintát, és az adatlapjáról kiolvassa, érvényes-e
   („Valid: yes/no”, „Not valid after”).
3. Kategóriánként megszámolja az érvényes és az összes mintát.
4. A kész indexet feltölti a GitHubra; az app a következő indításkor már ezt használja.

Az első futás hosszú (több ezer adatlap, 1–2 óra), utána a már ismert minták eredményét
megjegyzi (`prado-cache.json`), így a heti futás néhány perc.

## Szükséges
- Python 3.8 vagy újabb (csak az alapkönyvtárat használja).
- Egy GitHub-token, amely csak ehhez a tárolóhoz ad írási jogot, a `github-token.txt` fájlban
  a program mellett. Ezt a fájlt soha ne töltsd fel sehova (a `.gitignore` kizárja).

## Futtatás
    python3 prado_index.py                        # minden ország, feltöltéssel
    python3 prado_index.py --orszag HUN,SRB --nincs-feltoltes   # próba, feltöltés nélkül

Ha a PRADO túl sok országnál nem elérhető, a program nem tölt fel semmit, a régi index marad.
