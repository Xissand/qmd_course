## Задание по Wannier
Структура:
- cp2k.inp: входной файл для CP2K
- h.out: log CP2K
- H2_08_1600-HOMO_centers_s1-1_0.xyz: центр Ванье по версии CP2K
- H2_08_1600-WFN_00001_1-1_0.cube: волновая функция
- wannier.py: обработка - код для расчета центра Ванье по файлу с волновой функцией
- center.txt: вывод wannier.py