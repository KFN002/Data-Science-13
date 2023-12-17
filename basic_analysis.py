from tools import *
from graphics import *
import pandas as pd
from preformatting_data import preformat

"""
Базовый анализ факторов возникновения ОПП у пациентов (те, которые считаются важными)
"""

data = preformat(pd.read_csv('medics_1.csv', delimiter=',', encoding='utf-8'))

# посмотрим на названия столбцов
print(data.columns)
print('-------------------------------------------------')

# выведем первые несколько элементов, чтобы ознакомиться с датасетом
print(data.head())
print('-------------------------------------------------')

# обратим внимания на типы данных
print(data.info())

print('-------------------------------------------------')

# построение матрицы корреляций
plt.figure(figsize=(16, 16))
sns.set(style="whitegrid")
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, cmap='coolwarm')
plt.show()

for factor1 in ["хбп", "возраст", "сахарный_диабет", "гб", "сад", "дад", "чсс", "рн", "фракция_изгнания", "холестерин",
                "креатинин_крови", "мочевина", "скф_расч", "калий", "имт", "толщина_паренхимы_почек"]:
    # посмотрим на базовы метрики факторов
    print(pd.DataFrame(data[factor1].describe().T))
    print('-------------------------------------------------')
    # визуализируем данные:
    if factor1 in ["хбп", "сахарный_диабет", "гб"]:
        viz_data_pie(data, factor1)
    viz_data_hist_s(data, factor1)
