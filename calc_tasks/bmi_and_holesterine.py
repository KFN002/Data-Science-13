import pandas as pd
from preformatting_data import *
from graphics import *

data = preformat(pd.read_csv('../medics_1.csv', delimiter=',', encoding='utf-8'))
data['имт'] = pd.to_numeric(data['имт'], errors='coerce')
data['кат_холестерин'] = (data['холестерин']
                          .apply(lambda x: 'холестерин_превышен' if x >= 6 else 'холестерин_не_превышен'))
data_with_excess_bmi = data.loc[data['имт'] >= 25]
data_grouped = round(data_with_excess_bmi['кат_холестерин'].value_counts(normalize=True).mul(100), 2)
viz_data_box(data_with_excess_bmi, 'кат_холестерин', 'имт')
print(data_grouped)




