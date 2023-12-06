import pandas as pd
from scipy.stats import shapiro

from graphics import *
from preformatting_data import *

data = preformat(pd.read_csv('../medics_1.csv', delimiter=',', encoding='utf-8'))

# берем данные, где нет хбп, строим график скаттер для выявления зависимости
data_without_hbp = data.loc[data['хбп'] == 0]
viz_data_scatter(data_without_hbp, 'возраст',
                 'толщина_паренхимы_почек')

# посмотрим на взаимосвязь используя аналитические методы:
if shapiro(data['возраст'])[1] > 0.05 and shapiro(data['толщина_паренхимы_почек'])[1] > 0.05:
    print(data[['толщина_паренхимы_почек', 'возраст']].corr(method='pearson'))
else:
    print(data[['толщина_паренхимы_почек', 'возраст']].corr(method='spearman'))
