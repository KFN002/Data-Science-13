import pandas as pd
from scipy.stats import ttest_ind, shapiro, mannwhitneyu
from preformatting_data import preformat

'''
H0: Между группами с опп и без него нет разницы в холестерине
'''

data = preformat(pd.read_csv('../medics_1.csv', delimiter=',', encoding='utf-8'))

# разделение групп на опп и без него
with_opp = data[data['развитие_опп'] == 1]
without_opp = data[data['развитие_опп'] == 0]

# подсчет метрик в зависимости от распределения
if shapiro(with_opp["холестерин"])[1] >= 0.05 and shapiro(without_opp["холестерин"])[1] >= 0.05:
    t_stat, p_value = ttest_ind(with_opp['холестерин'], without_opp['холестерин'], equal_var=False)
else:
    t_stat, p_value = mannwhitneyu(with_opp['холестерин'], without_opp['холестерин'])

# выводим метрики
print(f'T-statistic: {round(t_stat, 4)}')
print(f'P-value: {round(p_value, 4)}')

print('------------------------')

if p_value < 0.05:
    print("Отвергаем нулевую гипотезу, различия между группами существуют.")
else:
    print("Не получилось отвергнуть нулевую гипотезу, различия между группами не существенны.")
