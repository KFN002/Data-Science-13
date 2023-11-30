import seaborn as sns
import matplotlib.pyplot as plt


def viz_data_hist(data, column1, column2):
    plt.figure(figsize=(12, 6))
    sns.histplot(data[column1], kde=True, color='blue', label=column1)
    sns.histplot(data[column2], kde=True, color='orange', label=column2)
    plt.title(f'Гистограмма для {column1} и {column2}')
    plt.legend()
    plt.show()


def viz_data_box(data, column1, column2):
    plt.figure(figsize=(12, 6))
    sns.boxplot(x=column1, y=column2, data=data)
    plt.title(f'Boxplot для {column1} и {column2}')
    plt.show()

