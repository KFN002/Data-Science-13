import pandas as pd
from graphics import *
from preformatting_data import *

data = preformat(pd.read_csv('../medics_1.csv', delimiter=',', encoding='utf-8'))

data_without_hbp = data.loc[data['хбп'] == 0]
viz_data_scatter(data_without_hbp, 'возраст',
                 'толщина_паренхимы_почек')
