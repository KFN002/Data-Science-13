from preformatting_data import *
import pandas as pd
from scipy.stats import pearsonr, spearmanr

data = preformat(pd.read_csv('../medics_1.csv', delimiter=',', encoding='utf-8'))

columns_to_research = [
    "возраст",
    "сахарный_диабет",
    "гб",
    "хбп",
    "сад",
    "дад",
    "чсс",
    "рн",
    "фракция_изгнания",
    "холестерин",
    "креатинин_крови",
    "мочевина",
    "скф_расч",
    "калий",
    "имт",
    "толщина_паренхимы_почек"
]

df_new = data[columns_to_research]  # отбираем столбцы для рассчётов

crosstab = df_new.corr()  # создаём таблицу корреляций

correlations = []

# отбираем ячейки с корреляцией более 0.2
for x in columns_to_research:
    for y in columns_to_research:
        cell = crosstab[x][y]

        if cell >= 0.2 and cell != 1:
            correlations.append([x, y, cell])

correlations = sorted(correlations, key=lambda x: x[2], reverse=True)

correlations = correlations[::2]

# Записываем в файл для удобства
# with open("correlations_table.txt", "w", encoding="utf-8") as f:
#    print(crosstab.to_string(), file=f)
# with open("correlations.txt", "w", encoding="utf-8") as f:
#     print(*correlations, sep="\n", file=f)

print(crosstab.to_string())
print()
print(*correlations, sep="\n")
print()

# получаем p-value для факторов с наибольшей корреляцией

res = []

for fac1, fac2, corr in correlations:
    res.append([fac1, fac2, corr, pearsonr(data[fac1], data[fac2]).pvalue])

print(*res, sep="\n")

'''
['креатинин_крови', 'мочевина', 0.6123963707140346, 3.108015793279446e-07]
['сад', 'дад', 0.5821269994760774, 4.051251704686385e-15]
['скф_расч', 'имт', 0.5142950927003834, 3.5234271093181755e-12]
Среди наибольших корреляций p-value не меньше 0.05, а значит можно сделать вывод: 
что корреляция не является статистически значимой, следовательно это просто особенность данных

'''