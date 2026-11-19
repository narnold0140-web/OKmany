@echo off
rem Okmanyvizsgalo: PRADO-index frissitese (a Feladatutemezo hetente futtatja)
cd /d "%~dp0"
echo ===== %date% %time% ===== >> naplo.txt
python prado_index.py >> naplo.txt 2>&1
