### ПРОЕКТ 13ОЙ КОМАНДЫ ПО АНАЛИЗУ ДАННЫХ

#Задачи:
> Блок 1: Первичный анализ данных, обработка данных

1. Большая часть заданий в preformatting.py - preformat()

2. Провести аналитический и графический анализ данных - basic_analysis.py

> Блок 2: Аналитические и графические задачи

1. Посчитать процент пациентов с хроническими заболеваниям
(сахарный диабет, гипертония, хроническая болезнь почек) для
групп “есть ОПП/нет ОПП”- calc_tasks.py

2.  Ввести новый фактор (описать и обосновать выбор фактора и его
значений) на основе столбца “Индекс массы тела”. Посчитать
количество пациентов, имеющих проблемы с сердцем (выбор
перечня проблем должен быть описан и обоснован) для каждой
группы. Сделать вывод. - preformatting.py - preformat()

3. Исследовать зависимость длительности операции от факта
перенесенного в прошлом инфаркта миокарда - surgery_duration_and_heart_attack.py

4. Верно ли, что у пациентов с ИМТ выше нормы будет повышенный
уровень холестерина? - bmi_and_holesterine.py

5. Верно ли, что даже без хронических болезней почек с возрастом
толщина паренхимы почек уменьшается - parenhima_thickness_decrease.py

6. Проверить адекватность поставленного диагноза по стадии
хронической болезни почек (найти параметр, по которому ставится
диагноз, использовать данные из внешних источников) - heart_problems_by_bmi.py

7. Исследовать корреляцию между параметрами. Для наиболее
сильных корреляций обосновать, имеет ли это реальный смысл или
же просто особенность данных - correlation_research.py

- Итоги в презентации

> Блок 3: Гипотезы

- Проверка гипотез - влияние факторов на возникновение ОПП

1. Все в папке hypotheses: 
- hypothesis_nominal - номинальные
- hypothesis_most_factors - большинство количественных
- остальные файлы с говорящими названиями - факторы, рассмотрение которых в гипотезах захотели выделить

- Найдена связь с опп среди: объем_инфузий, объем_кровопотерии, калий, чсс

> Блок 4: Построение и работа с регрессионной моделью

1. Построение модели - regression_model/linear_regression.py

 Метрики модели:

- R-squared: 0.1217

- Mean Squared Error: 0.16

- Прогнозные значения для калия: [4.39  4.431 4.35  4.523 4.412 4.492 4.392 4.551 4.396 4.372 4.554 4.488 4.393 4.315 4.425 4.465 4.434 4.336 4.348 4.547 4.414]

- Разница прогнозных значений нашей модели и константной: [0.39  0.431 0.35  0.523 0.412 0.492 0.392 0.551 0.396 0.372 0.554 0.488 0.393 0.315 0.425 0.465 0.434 0.336 0.348 0.547 0.414]

- Percentage mean absolute error: 7.99%



> Блок 5: Итоги

1. Описание итогов

2. Дэшборд

3. Презентация







