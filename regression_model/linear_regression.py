from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from preformatting_data import preformat
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np


data = preformat(pd.read_csv('../medics_1.csv', delimiter=',', encoding='utf-8'))


x = data[["возраст", "сад", "дад", "чсс", "рн", "фракция_изгнания", "холестерин",
          "креатинин_крови", "мочевина", "скф_расч", "имт", "толщина_паренхимы_почек",
          "количество_шунтов", "длительность_аик", "длительность_операции", "время_пережатия_аорты",
          "объем_кровопотерии", "объем_гемотрансфузии", "объем_инфузий", "диурез", "объем_кровопотерии",
          "хбп", "сахарный_диабет", "гб", "аик", "переливание_крови_и_аик"]]

x_train, x_test, y_train, y_test = train_test_split(x, data["калий"],
                                                    test_size=0.15, random_state=42)

preprocessor = ColumnTransformer(
    transformers=[
        ('hbp_category', OneHotEncoder(), ['хбп']),
        ('diabetes_category', OneHotEncoder(), ['сахарный_диабет']),
        ('hypertonic_category', OneHotEncoder(), ['гб']),
        ('aik_category', OneHotEncoder(), ['аик']),
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
print("R-squared:", round(r2, 2))
print("Mean Squared Error:", round(mse, 2))
cv_scores = cross_val_score(model, x, data["калий"], cv=5, scoring='neg_mean_squared_error')
print("Cross-Validation Mean Squared Error:", round(-cv_scores.mean(), 2))
y_pred = model.predict(x_test)
rounded_predictions = np.round(y_pred).astype(float)
print(rounded_predictions)
