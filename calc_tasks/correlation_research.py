from preformatting_data import *
import pandas as pd
from scipy.stats import pearsonr, spearmanr

data = preformat(pd.read_csv('../medics_1.csv', delimiter=',', encoding='utf-8'))

columns_to_research = [
    "возраст",
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
    "толщина_паренхимы_почек",
    "количество_шунтов",
    "длительность_аик",
    "длительность_операции",
    "время_пережатия_аорты",
    "объем_кровопотерии",
    "объем_гемотрансфузии",
    "объем_инфузий",
    "диурез"
]

df_new = data[columns_to_research]  # отбираем столбцы для рассчётов

crosstab = df_new.corr()  # создаём таблицу корреляций

correlations = []

# отбираем ячейки с корреляцией более 0.2
for x in columns_to_research:
    for y in columns_to_research:
        cell = crosstab[x][y]

        if cell >= 0.5 and cell != 1:
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
print(["фактор1", "фактор2", "корреляция"])
print(*correlations, sep="\n")
print()

# получаем p-value для факторов с наибольшей корреляцией

res = []

for fac1, fac2, corr in correlations:
    res.append([fac1, fac2, corr, pearsonr(data[fac1], data[fac2]).pvalue])

print(["фактор1", "фактор2", "корреляция", "p-value"])
print(*res, sep="\n")

'''
['фактор1', 'фактор2', 'корреляция', 'p-value']
['длительность_аик', 'время_пережатия_аорты', 0.9003435304377455, 6.993373227871792e-58]
['количество_шунтов', 'время_пережатия_аорты', 0.6200713806266671, 4.7327351704677334e-18]
['креатинин_крови', 'мочевина', 0.6123963707140346, 1.5619558227364968e-17]
['количество_шунтов', 'длительность_операции', 0.5894649921982215, 4.593629804366926e-16]
['сад', 'дад', 0.5821269994760774, 1.2821930198709196e-15]
['скф_расч', 'имт', 0.5142950927003834, 5.593224509466298e-12]
['количество_шунтов', 'длительность_аик', 0.5103597305171141, 8.607445801968889e-12]
Среди наибольших корреляций p-value меньше 0.05, а значит можно сделать вывод: 
что корреляция является статистически значимой, следовательно это имеет реальный смысл

'''