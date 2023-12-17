import tools
from tools import *
import pandas as pd


def preformat(df: pd.DataFrame):
    # Перевод строк в фомат pep 8
    df.columns = [col.lower().strip().replace(' ', '_') for col in df.columns]

    # форматирование неправильных данных в header для удобной работы
    df.columns = list(map(lambda x: x.replace(',', '').replace('.', ''), df.columns))

    # Переводим str и object вида float во float
    columns_to_convert = ["мочевина",
                          "хлориды",
                          "кальций",
                          "триглицериды",
                          "лпонп",
                          "лпнп",
                          "ачтв",
                          "толщина_паренхимы_почек",
                          "калий",
                          "натрий",
                          "рн",
                          "ве",
                          "нсо3",
                          "ро2",
                          "рсо2",
                          "оксигем",
                          "общсо2",
                          "гемоглобин",
                          "лейкоциты_крови",
                          "чсс",
                          "мо",
                          "дд_лж_см",
                          "сд_лж_см",
                          "кдр_правого_желудочка",
                          "размер_левого_предсердия",
                          "холестерин",
                          "общий_белок",
                          "имт",
                          "скф_расч"]

    for column in columns_to_convert:
        df[column] = df[column].apply(convert_to_float).astype(float)

    # Меняем есть на 1 и нет на 0 для удобства работы
    df["развитие_опп"] = df["развитие_опп"].apply(lambda x: 1 if x == 'есть' else 0)

    # Меняем хбп на 1 2 3 для удобства работы
    df["хбп"] = df["хбп"].apply(lambda x: 0 if x == 'Пациенты без ХБП' else (1 if x == 'Стадия C1-C2' else 3))

    # Удаление полностью совпадающих строк (не может быть два+ полностью идентичных человека)
    df = df.drop_duplicates()

    # Удалние пропусков, так как в медецине остальные параметры не всегда предсказуемы (т.е. медиана и тд не подойдет)
    df: object = df.dropna()

    catigory = ["развитие_опп",
                "хбп",
                "пол",
                "гб",
                "сахарный_диабет",
                "стенокардия",
                "инфаркт_миокарда",
                "мерцательная_аритмия",
                "желудочковая_экстрасистолия",
                "а-в_блокада",
                "блокада_ножек_пучка_гиса",
                "хсн",
                "нк",
                "ар",
                "аик",
                "количество_шунтов"]

    # Заменение супервыбросов медианой по столбцу(удаление невозможно из-за их большого числа)
    for i in df.columns:
        if not (i in catigory):
            zeroable = ["длительность_аик", "время_пережатия_аорты", "объем_гемотрансфузии"]
            if not (i in zeroable):
                q_low = df[i].quantile(q=0.001)
                q_hi = df[i].quantile(q=0.999)
                def f(x):
                    if (x < q_low) | (x > q_hi):
                        return tools.normtype(x, df[i].median())
                    else:
                        return x

                df[i] = df[i].apply(f)
            else:
                not_zero = df[i][df[i] != 0]
                q_low = not_zero.quantile(q=0.001)
                q_hi = not_zero.quantile(q=0.999)

                def f(x):
                    if ((x < q_low) | (x > q_hi)) & (x != 0):
                        return tools.normtype(x, not_zero.median())

                    else:
                        return x

                df[i] = df[i].apply(f)


                # добавление нового столбца
    df['переливание_крови_и_аик'] = df['аик'] & df['объем_гемотрансфузии']

    # добавление столбца есть_хроническое_заболевание
    # (Рассматриваем сахарный диабет, гипертонию, и хроническую болезнь почек)
    df["есть_хроническое_заболевание"]\
        = [1 if row["сахарный_диабет"] == 1 or row["гб"] == 1 or row["хбп"] == 1 or row["хбп"] == 3 else 0
           for i, row in df.iterrows()]

    return df
