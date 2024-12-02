# объявил функцию с параметрами
def get_matrix(n, m, value):
    # пустой список
    matrix = []
    # внешний цикл для n строк
    for i in range(n):
        # пустой список для каждой строки
        matrix.append([])
        # внутренний цикл для m столбцов
        for _ in range(m):
            # Добавляем значение в текущую строку по индексу
            matrix[i].append(value)
    # возвращение созданной матрицы
    return matrix

# примеры использования функции из задания
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
