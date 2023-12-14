import pandas as pd
from graphics import *
from preformatting_data import *
from calc_tasks import *

data = preformat(pd.read_csv('medics_1.csv', delimiter=',', encoding='utf-8'))

print(data.head(100))

for elem in data.columns:
    print(elem)
    print(data[elem])
    print(f'max_{elem}: {max(data[elem])}')
    print(f'min_{elem}: {min(data[elem])}')

print(data.columns)

# выполнение задач с подсчётами

calc_chronic_ratio(data)


# графический анализ

viz_data_hist(data, 'аик', 'объем_гемотрансфузии')
viz_data_box(data, 'пол', 'возраст')
