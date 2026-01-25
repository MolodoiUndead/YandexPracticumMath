import matplotlib.pyplot as plt
import numpy as np


# Task 1
def task_1():
    """Гистограмма"""
    data = [1, 2.5, 2, 3.2, 3, 3.4, 4, 4.1, 4, 4.3, 5.7, 5.2, 5.2, 5.1, 5]
    plt.hist(data)
    plt.show()


def task_2():
    """Гистограмма с двумя наборами данных"""
    data_1 = [6, 6, 6, 4, 3, 7, 1, 6, 7, 4, 1, 5, 7, 1, 5, 1, 5, 1, 1, 7]
    data_2 = [4, 9, 5, 8, 6, 8, 6, 3, 5, 9, 9, 8, 4, 7, 6, 9, 6, 7, 7, 6]

    bins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    plt.hist(data_1, bins)
    plt.hist(data_2, bins)
    plt.show()


def task_3():
    """Гистограмма с двумя наборами данных с прозрачностью"""
    data_1 = [6, 6, 6, 4, 3, 7, 1, 6, 7, 4, 1, 5, 7, 1, 5, 1, 5, 1, 1, 7]
    data_2 = [4, 9, 5, 8, 6, 8, 6, 3, 5, 9, 9, 8, 4, 7, 6, 9, 6, 7, 7, 6]

    bins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    plt.hist(data_1, bins, alpha=0.5)
    plt.hist(data_2, bins, alpha=0.5)
    plt.show()


def task_4():
    """Гистограмма с тремя наборами данных с подписями"""
    mass_data_1 = [8.9, 9.8, 9.9, 10.2, 9.2, 9.6, 10.0, 8.6, 10.5, 10.6, 9.5, 10.4, 10.4, 10.5, 9.3, 10.9, 8.4, 9.9,
                   11.0, 10.0]
    mass_data_2 = [7.6, 5.9, 6.6, 7.1, 6.3, 6.8, 6.9, 8.2, 6.2, 8.6, 6.1, 6.8, 7.0, 8.2, 7.8, 8.1, 9.3, 5.4, 7.7, 7.8]
    mass_data_3 = [7.9, 9.9, 9.4, 9.7, 9.0, 9.6, 9.2, 8.5, 7.6, 8.8, 8.2, 8.8, 9.0, 10.9, 8.9, 7.9, 9.4, 7.8, 8.1, 8.8]

    bins = 10

    # Построение гистограмм с подписями
    plt.hist(mass_data_1, bins, alpha=0.5, label='Данные о массе 1')
    plt.hist(mass_data_2, bins, alpha=0.5, label='Данные о массе 2')
    plt.hist(mass_data_3, bins, alpha=0.5, label='Данные о массе 3')

    # Добавление легенды
    plt.legend()

    # Отображение графика
    plt.show()


def task_5():
    """Векторы"""
    #вектор
    v = np.array([0, 8, 56, 11])
    print(v)

    #нулевой вектор
    a = np.zeros(4)
    print(a)

    #сложение векторов
    january = np.array([648, 371, 338.4, 512, 0, 437, 11])
    february = np.array([112, 380, 516, 294, 108, 380, 65])
    march = np.array([506, 0, 412, 98, 304, 811, 56])
    s = january + february + march
    print(s)

    #сложение векторов с числами
    a = np.array([-2.7, 6, 5.14, 48])
    b = np.array([3.5, 0.17, 8.4, 0])
    print(a - 1.7 - b + 3)

def task_6():
    """Умножение и деление вектора на скаляр"""
    productivity = np.array([3.7, 4.8, 4.2, 7.2, 7.6])
    first = 1.25 * productivity
    second = 1.1 * productivity
    print(first)
    print(second)

    a = np.array([60000, 100000, 80000, 65000, 73000])
    print(a / 15)
    print(a / 10)


# task_1()
# task_2()
# task_3()
# task_4()
# task_5()
# task_6()