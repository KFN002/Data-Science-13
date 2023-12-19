import pandas as pd
from scipy.stats import shapiro, spearmanr, pearsonr

from graphics import *
from preformatting_data import *

data = preformat(pd.read_csv('../medics_1.csv', delimiter=',', encoding='utf-8'))

# берем данные, где нет хбп, строим график скаттер для выявления зависимости
data_without_hbp = data.loc[data['хбп'] == 0]
viz_data_scatter(data_without_hbp, 'возраст',
                 'толщина_паренхимы_почек')

# посмотрим на взаимосвязь используя аналитические методы:
if shapiro(data['возраст'])[1] >= 0.05 and shapiro(data['толщина_паренхимы_почек'])[1] >= 0.05:
    print(round(data[['толщина_паренхимы_почек', 'возраст']].corr(method='pearson'), 4))
    corr, p_value = pearsonr(data['возраст'], data['толщина_паренхимы_почек'])
else:
    print(round(data[['толщина_паренхимы_почек', 'возраст']].corr(method='spearman'), 4))
    corr, p_value = spearmanr(data['возраст'], data['толщина_паренхимы_почек'])

print('------------')
print(f"Correlation check: {round(corr, 4)}")
print(f"P-value: {round(p_value, 4)}")

'''
Ответ: Нет, связь между толщиной паренхимы почек и возрастом не доказана
'''
