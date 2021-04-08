import re
# Дерево решений
def tree(x):
    if x[2] == 'sage':
        return 6
    elif x[2] == 'xbase':
        if x[0] == 'go':
            return 11
        elif x[1] == 1961:
            return 7
        elif x[1] == 2012:
            return 10
        elif x[3] == 1973:
            return 8
        else:
            return 9
    else:
        if x[4] == 1983:
            return 4
        elif x[4] == 1961:
            return 5
        elif x[0] == 'go':
            return 3
        elif x[1] == 1961:
            return 0
        elif x[1] == 1984:
            return 1
        else:
            return 2

# Транскодер
def transcode():
    pass

# Обработка таблиц
def table_process(table):
    to_delete = []  # Список для хранения индексов удаляемых строк
    # Удаление пустых строк
    for i in range(len(table)):
        if all(word is None for word in table[i]):
            to_delete.append(i)
    for i in range(len(to_delete) - 1, -1, -1):
        table.pop(to_delete[i])
    return_table = []  # Итоговая матрица

    # Заполнение матрицы
    for i in range(len(table[0])):
        to_add = []
        for j in range(len(table)):
            if i == 0:
                to_add.append(table[j][i][3:])
            elif i == 1:
                if table[j][i] == 'Y':
                    to_add.append('Да')
                else:
                    to_add.append('Нет')
            elif i == 2:
                to_add.append("{0:.0%}".format(float(table[j][i])))
            else:
                to_add.append(table[j][i][:table[j][i].find('[')])
        return_table.append(to_add)
    return return_table
