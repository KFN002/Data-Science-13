import pandas as pd
from graphics import *
from preformatting_data import *

data = preformat(pd.read_csv('../medics_1.csv', delimiter=',', encoding='utf-8'))

viz_data_box(data, 'инфаркт_миокарда', 'длительность_операции')
