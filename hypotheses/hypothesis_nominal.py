import pandas as pd
from scipy.stats import ttest_ind, shapiro, mannwhitneyu, chi2_contingency
from preformatting_data import preformat


'''
H0: Между группами с опп и без него нет разницы в соответствующем номинальном факторе нет
'''

data = preformat(pd.read_csv('../medics_1.csv', delimiter=',', encoding='utf-8'))

data["развитие_опп"] = data["развитие_опп"].apply(lambda x: 'да' if x == 1 else 'нет')


# подсчет метрик
for factor in ["имт_кат", "хбп", "гб", "сахарный_диабет", "переливание_крови_и_аик", "есть_хроническое_заболевание"]:

    contingency_table = pd.crosstab(data["развитие_опп"], data[factor])
    chi2, p_value, _, _ = chi2_contingency(contingency_table)

    # выводим метрики
    print(f'Chi2: {round(chi2, 4)}')
    print(f'P-value: {round(p_value, 4)}')

    if factor == 'имт_кат':
        factor = 'повышенного имт'
    if p_value < 0.05:
        print(f"Отвергаем нулевую гипотезу, различия между группами существуют в наличии {factor}.")
    else:
        print(f"Не получилось отвергнуть нулевую гипотезу, различия между группами в наличии {factor} не существенны.")
    print('-------------------------------')
