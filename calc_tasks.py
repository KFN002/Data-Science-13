import pandas as pd
from preformatting_data import *

def calc_chronic_ratio(df: pd.DataFrame):
    '''Посчитать процент пациентов с хроническими заболеваниями для групп "есть ОПП/нет ОПП"'''
    df = df.copy()
    
    # полные группы "есть ОПП/нет ОПП"
    group_1_all = df[(df["развитие_опп"] == 1)]
    group_2_all = df[(df["развитие_опп"] == 0)]
    
    # группы "есть ОПП/нет ОПП" и есть хроническое заболевание
    group_1_chronic = df[(df["развитие_опп"] == 1) & (df["есть_хроническое_заболевание"] == 1)]
    group_2_chronic = df[(df["развитие_опп"] == 0) & (df["есть_хроническое_заболевание"] == 1)]
    
    # размерность полных групп
    count_1_all = group_1_all.shape[0]
    count_2_all = group_2_all.shape[0]
    
    # размерность группы с хроническим заболеванием
    count_1_chronic = group_1_chronic.shape[0]
    count_2_chronic = group_2_chronic.shape[0]
    
    # подсчёт процентов внутри групп
    percent_1 = count_1_chronic / count_1_all * 100
    percent_2 = count_2_chronic / count_2_all * 100
    
    print(round(percent_1, 2), round(percent_2, 2))  # 96.97 98.28
    # Процент для групп с хроническими заболеваниями: Есть опп - 96.97, Нет опп - 98.28


if __name__ == "__main__":
    data = preformat(pd.read_csv('medics_1.csv', delimiter=',', encoding='utf-8'))

    calc_chronic_ratio(data)