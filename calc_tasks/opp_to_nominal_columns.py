from preformatting_data import *
import pandas as pd

data = preformat(pd.read_csv('../medics_1.csv', delimiter=',', encoding='utf-8'))

dd = data.copy()

group = "развитие_опп"
nominal_columns = ["сахарный_диабет", "гб", "хбп", "имт_кат", "аик"]


res = []

for col in nominal_columns:
    cross_matrix = pd.crosstab(dd[group], dd[col])
    chi2 = chi2_contingency(cross_matrix)
    res.append([col, cramers_v(cross_matrix), chi2.pvalue])

print("P-уровень и корреляция развитие_опп - номинальные факторы")
print(["показатель", "корреляция крамера", "p-уровень"])
print(*res, sep="\n")
print()

