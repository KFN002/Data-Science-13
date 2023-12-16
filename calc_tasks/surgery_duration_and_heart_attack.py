from scipy.stats import pointbiserialr

from graphics import *
from preformatting_data import *


data = preformat(pd.read_csv('../medics_1.csv', delimiter=',', encoding='utf-8'))

# строим ящик с усами для выявления зависимости между инфарктом ранее и длительностю операции
viz_data_box(data, 'инфаркт_миокарда', 'длительность_операции')

# посмотрим на взаимосвязь используя аналитические методы:
correlation_coefficient, p_value = pointbiserialr(data['инфаркт_миокарда'], data['длительность_операции'])

print(f"Point-Biserial Correlation Coefficient: {correlation_coefficient}")
print(f"P-value: {p_value}")

result = correlation_ratio(data['инфаркт_миокарда'], data['длительность_операции'])
print(f"Correlation using ETA: {round(result, 4)}")


