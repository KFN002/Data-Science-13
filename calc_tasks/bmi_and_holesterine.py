import pandas as pd
from preformatting_data import *
from graphics import *

data = preformat(pd.read_csv('../medics_1.csv', delimiter=',', encoding='utf-8'))

# переводим данные в числа для удобства работы
data['имт'] = pd.to_numeric(data['имт'], errors='coerce')

# создаем категориальный столбец для удобства работы и подсчета
data['кат_холестерин'] = (data['холестерин']
                          .apply(lambda x: 'холестерин_превышен' if x >= 6 else 'холестерин_не_превышен'))

# находим данные для имт выше нормы
data_with_excess_bmi = data.loc[data['имт'] >= 25]

# выявляем зависимость имт и повышенного уровня холестерина
data_grouped = round(data_with_excess_bmi['кат_холестерин'].value_counts(normalize=True).mul(100), 2)

# для полного понимания строим ящик с усами, смотрим на зависимость
viz_data_box(data_with_excess_bmi, 'кат_холестерин', 'имт')
print(data_grouped)

cross_table = pd.crosstab(data['инфаркт_миокарда'], data['длительность_операции'])
print(round(cramers_v(cross_table), 4))




