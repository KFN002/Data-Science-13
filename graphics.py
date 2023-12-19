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


def viz_data_scatter(data_frame, column1, column2):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=column1, y=column2, data=data_frame, edgecolor="w", s=100)
    plt.show()


def viz_data_kde(data, column):
    sns.set(style="whitegrid")
    sns.kdeplot(data=data, x=column, fill=True)
    plt.show()


def viz_data_hist_s(data, column):
    sns.set(style="whitegrid")
    sns.histplot(data=data, x=column, kde=True)
    plt.show()


def viz_data_pie(data, column):
    sns.set(style="whitegrid")
    data[column].value_counts().plot(kind='pie', autopct='%1.1f%%', legend=False)
    plt.show()
