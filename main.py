import numpy as np

def calculate_currents(resistances, emfs, configuration):
    num_components = len(resistances) + len(emfs)  # Общее количество компонентов в схеме
    matrix = np.zeros((num_components, num_components))  # Матрица коэффициентов
    vector = np.zeros(num_components)  # Вектор правой части (ЭДС)

    # Заполнение матрицы коэффициентов для каждого соединения
    for i in range(len(resistances)):
        # Добавляем сопротивление в матрицу
        matrix[i][i] = resistances[i]
        # Заполняем строки с учетом конфигурации источников питания
        for j in range(len(emfs)):
            if configuration[i][j] == 1:
                matrix[i][len(resistances) + j] = -1
                matrix[len(resistances) + j][i] = -1

    # Заполнение вектора правой части ЭДС
    for i in range(len(emfs)):
        vector[len(resistances) + i] = emfs[i]

    # Решаем систему линейных уравнений
    currents = np.linalg.solve(matrix, vector)

    return currents[:len(resistances)]  # Возвращаем только токи через резисторы


# Пример использования

resistances = [5, 10, 15, 20]

emfs = [18, 6]

configuration = [
    [1, 0],  # Резистор 1 соединен с ЭДС 1
    [0, 1],  # Резистор 2 соединен с ЭДС 2
    [1, 1],  # Резистор 3 соединен с обоими источниками
    [0, 0],  # Резистор 4 не подключен к источникам
]


# Вычисление токов
currents = calculate_currents(resistances, emfs, configuration)

# Вывод результатов
print("Токи через резисторы:")
for i, current in enumerate(currents, start=1):
    print(f"Ток через резистор {i}: {current:.2f} A")
