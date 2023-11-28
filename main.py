import pandas as pd


data = pd.read_csv('medics_1.csv', delimiter=',', encoding='utf-8')
data.columns = [col.lower().replace(' ', '_') for col in data.columns]
data["развитие_опп"] = data["развитие_опп"].apply(lambda x: 1 if x == 'есть' else 0)
for elem in data.columns:
    print(elem)
    print(data[elem])