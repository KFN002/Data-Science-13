import pandas as pd
from scipy.stats import ttest_ind, shapiro, mannwhitneyu, chi2_contingency
from preformatting_data import preformat


'''
H0: Между группами с опп и без него нет разницы в аик и переливании крови
'''

data = preformat(pd.read_csv('../medics_1.csv', delimiter=',', encoding='utf-8'))

data["развитие_опп"] = data["развитие_опп"].apply(lambda x: 'да' if x == 1 else 'нет')


# подсчет метрик
contingency_table = pd.crosstab(data["развитие_опп"], data['переливание_крови_и_аик'])
chi2, p_value, _, _ = chi2_contingency(contingency_table)

# выводим метрики
print(f'Chi2: {round(chi2, 4)}')
print(f'P-value: {round(p_value, 4)}')

print('------------------------')

if p_value < 0.05:
    print("Отвергаем нулевую гипотезу, различия между группами существуют.")
else:
    print("Не получилось отвергнуть нулевую гипотезу, различия между группами не существенны.")
