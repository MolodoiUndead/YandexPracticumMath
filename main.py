import matplotlib.pyplot as plt

#Task 1
def task_1():
    data = [1, 2.5, 2, 3.2, 3, 3.4, 4, 4.1, 4, 4.3, 5.7, 5.2, 5.2, 5.1, 5]
    plt.hist(data)
    plt.show()

#task_1()

def task_2():

    data_1 = [6, 6, 6, 4, 3, 7, 1, 6, 7, 4, 1, 5, 7, 1, 5, 1, 5, 1, 1, 7]
    data_2 = [4, 9, 5, 8, 6, 8, 6, 3, 5, 9, 9, 8, 4, 7, 6, 9, 6, 7, 7, 6]

    bins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    plt.hist(data_1, bins)
    plt.hist(data_2, bins)
    plt.show()

task_2()