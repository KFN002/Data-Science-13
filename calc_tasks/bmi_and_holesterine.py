from scipy.stats import pointbiserialr

from preformatting_data import *
from graphics import *

data = preformat(pd.read_csv('../medics_1.csv', delimiter=',', encoding='utf-8'))

# переводим данные в числа для удобства работы
data['имт'] = pd.to_numeric(data['имт'], errors='coerce')

# создаем категориальный столбец для удобства работы и подсчета
data['кат_холестерин'] = (data['холестерин']
                          .apply(lambda x: 1 if x >= 6 else 0))

# находим данные для имт выше нормы
data_with_excess_bmi = data.loc[data['имт'] >= 25]

# выявляем зависимость имт и повышенного уровня холестерина
data_grouped = round(data_with_excess_bmi['кат_холестерин'].value_counts(normalize=True).mul(100), 2)

# для полного понимания строим ящик с усами, смотрим на зависимость
viz_data_box(data_with_excess_bmi, 'кат_холестерин', 'имт')
print(data_grouped)

print('----------------------------------------')

# посмотрим на взаимосвязь используя аналитические методы:
correlation_coefficient, p_value = pointbiserialr(data_with_excess_bmi['кат_холестерин'], data_with_excess_bmi['имт'])

print(f"Point-Biserial Correlation Coefficient: {round(correlation_coefficient, 4)}")
print(f"P-value: {round(p_value, 4)}")

print('----------------------------------------')

result = correlation_ratio(data_with_excess_bmi['кат_холестерин'], data_with_excess_bmi['имт'])
print(f"Correlation using ETA: {round(result, 4)}")

'''
Ответ: Нет, связь между уровнем холестерина и имт выше нормы не доказана
'''





