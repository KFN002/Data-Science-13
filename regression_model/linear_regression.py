from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_percentage_error
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from preformatting_data import preformat
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np


'''
['креатинин_крови', 'мочевина', 0.6123963707140346]
['сад', 'дад', 0.5821269994760774]
['скф_расч', 'имт', 0.5142950927003834]
['хбп', 'креатинин_крови', 0.3506494153082033]
['хбп', 'мочевина', 0.3421063061559164]
['гб', 'дад', 0.27427148830414894]
['скф_расч', 'толщина_паренхимы_почек', 0.27343796703861056]
['дад', 'холестерин', 0.26991301505829995]
['возраст', 'хбп', 0.23383385766528345]
['чсс', 'скф_расч', 0.21538077267756897]
['гб', 'сад', 0.2147059905254671]
['хбп', 'калий', 0.20657549665296474]
['имт', 'толщина_паренхимы_почек', 0.20656930131402937]

['креатинин_крови', 'мочевина', 0.6123963707140346, 1.5619558227364968e-17]
['сад', 'дад', 0.5821269994760774, 1.2821930198709196e-15]
['скф_расч', 'имт', 0.5142950927003834, 5.593224509466298e-12]
['хбп', 'креатинин_крови', 0.3506494153082033, 6.722014138762309e-06]
['хбп', 'мочевина', 0.3421063061559164, 1.1577974937472592e-05]
['гб', 'дад', 0.27427148830414894, 0.000508853828832257]
['скф_расч', 'толщина_паренхимы_почек', 0.27343796703861056, 0.0005301017738373294]
['дад', 'холестерин', 0.26991301505829995, 0.0006293247152767451]
['возраст', 'хбп', 0.23383385766528345, 0.003203636427098366]
['чсс', 'скф_расч', 0.21538077267756897, 0.006748272893214418]
['гб', 'сад', 0.2147059905254671, 0.006927144547113888]
['хбп', 'калий', 0.20657549665296474, 0.00943820187204469]
['имт', 'толщина_паренхимы_почек', 0.20656930131402937, 0.009440387686745485]
'''

data = preformat(pd.read_csv('../medics_1.csv', delimiter=',', encoding='utf-8'))


x = data[["возраст", "дад", "время_пережатия_аорты", "объем_кровопотерии",
          "есть_хроническое_заболевание", "переливание_крови_и_аик", "чсс", "мочевина",
          "имт", "длительность_аик", "объем_инфузий"]]


x_train, x_test, y_train, y_test = train_test_split(x, data["калий"],
                                                    test_size=0.13, random_state=42)

preprocessor = ColumnTransformer(
    transformers=[
        ('ill_category', OneHotEncoder(), ["есть_хроническое_заболевание"]),
        ('aik_blood_category', OneHotEncoder(), ['переливание_крови_и_аик'])
    ],
    remainder='passthrough'
)
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

model = LinearRegression()
model.fit(x_train, y_train)


y_pred = model.predict(x_test)
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print("R-squared:", round(r2, 4))
print("Mean Squared Error:", round(mse, 2))
cv_scores = cross_val_score(model, x, data["калий"], cv=5, scoring='neg_mean_squared_error')
print("Cross-Validation Mean Squared Error:", round(-cv_scores.mean(), 2))
y_pred = model.predict(x_test)
rounded_predictions = np.round(y_pred, 3).astype(float)
print(rounded_predictions)
print(f"Percentage mean absolute error: {round(mean_absolute_percentage_error(y_test, y_pred) * 100, 2)}%")
