import pandas as pd
from graphics import *
from preformatting_data import *
from scipy.stats import shapiro, pearsonr, chi2_contingency
import numpy as np

data = preformat(pd.read_csv('../medics_1.csv', delimiter=',', encoding='utf-8'))

# строим ящик с усами для выявления зависимости между инфарктом ранее и длительностю операции
viz_data_box(data, 'инфаркт_миокарда', 'длительность_операции')

cross_table = pd.crosstab(data['инфаркт_миокарда'], data['длительность_операции'])
print(round(cramers_v(cross_table), 4))

