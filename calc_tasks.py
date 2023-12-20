import pandas as pd


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


def correct_hbp(data):
    for index, row in data.iterrows():
        hbp = row["хбп"]
        skf = row["скф_расч"]
        if 60 <= skf <= 89:
            data["хбп"][index] = 2
        if 30 <= skf < 60:
            data["хбп"][index] = 3
        if 15 <= skf < 30:
            data["хбп"][index] = 4
        if skf < 15:
            data["хбп"][index] = 5
    return data


def check_hbp_diagnosis(data):
    for index, row in data.iterrows():
        hbp = row["хбп"]
        skf = row["скф_расч"]
        if skf > 90:
            if hbp != 0:
                return False
        if 60 <= skf < 90:
            if data["хбп"][index] != 1:
                return
        if 30 <= skf < 60:
            if data["хбп"][index] != 3:
                return False
    return True
