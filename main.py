import pandas as pd
from tools import *

data = pd.read_csv('medics_1.csv', delimiter=',', encoding='utf-8')

# Перевод строк в фомат pep 8
data.columns = [col.lower().replace(' ', '_') for col in data.columns]

# Переводим str вида float во float
columns_to_convert = ["мочевина,_",
                      "хлориды",
                      "кальций",
                      "триглицериды",
                      "лпонп",
                      "лпнп",
                      "ачтв",
                      "толщина_паренхимы_почек"]

for column in columns_to_convert:
    data[column] = data[column].apply(convert_to_float).astype(float)

# Меняем есть на 1 и нет на 0 для удобства работы
data["развитие_опп"] = data["развитие_опп"].apply(lambda x: 1 if x == 'есть' else 0)
# Меняем хбп на 1 2 3 для удобства работы
data["хбп"] = data["хбп"].apply(lambda x: 0 if x == 'Пациенты без ХБП' else (1 if x == 'Стадия C1-C2' else 3))

for elem in data.columns:
    print(elem)
    print(data[elem])
    print(f'max_{elem}: {max(data[elem])}')
    print(f'min_{elem}: {min(data[elem])}')

# Удаление полностью совпадающих строк (не может быть два+ полностью идентичных человека)
data = data.drop_duplicates()

# Удалние пропусков, так как в медецине остальные параметры не всегда предсказуемы (т.е. медиана и тд не подойдет)
data = data.dropna()


