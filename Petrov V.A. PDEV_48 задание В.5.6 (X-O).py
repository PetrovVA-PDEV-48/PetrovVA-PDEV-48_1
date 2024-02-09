
# Игра классическая, 3х3 клетки, значит Х ходит первым, количество возможных ходов 9
# Решение реализовано только для этого частного случая, проверка на выигрыш начиная с 5 хода

print("Сыграем в крестики-нолики? Для хода введите координаты клетки через пробел,")
print("где первая цифра ее место по вертикали а вторая по горизонтали, например 2 2")

# матрица результата игры M удобная для пользователя:

M = [
      ['y|x:', '1', '|', '2', '|', '3']
    , ['1   ', ' ', '|', ' ', '|', ' ']
    , ['--- ', '--', '', '--', '', '--']
    , ['2   ', ' ', '|', ' ', '|', ' ']
    , ['--- ', '--', '', '--', '', '--']
    , ['3   ', ' ', '|', ' ', '|', ' ']
]

for i in range(6):
  for j in range(6):
      print(M[i][j], end = " ")
  print()

L = []  # Список всех ходов - уже заполненных клеток матрицы:

def winner_check(L, N):    # Функция проверки выигрыша
    if N % 2:
        s = 0
    else:
        s = 1
    l_row = []   # Список ходов игрока в строки
    l_col = []   # Список ходов игрока в столбцы
    cntd_1 = 0   # Счетчик ходов игрока по диагонали сверху вниз
    cntd_2 = 0   # Счетчик ходов игрока по диагонали снизу вверх
    for i in range(s, N + 1, 2):              # Проверка ходов игрока в строки
        for j in range(1):
            l_row.append(L[i][j])
            if 3 in [l_row.count(1), l_row.count(2), l_row.count(3)]:
                return True
    for i in range(s, N + 1, 2):              # Проверка ходов игрока в столбцы
        for j in range(1, 2):
            l_col.append(L[i][j])
            if 3 in [l_col.count(1), l_col.count(2), l_col.count(3)]:
                return True
    for i in range(s, N + 1, 2):              # Проверка ходов игрока по диагоналям
        if L[i] in [[1, 1], [2, 2], [3, 3]]:
            cntd_1 += 1
        if L[i] in [[1, 3], [2, 2], [3, 1]]:
            cntd_2 += 1
        if cntd_1 == 3 or cntd_2 == 3:
            return True
    else:
        return False

for i in range(1, 10):
    if i % 2:
        move = list(map(int, input("Ход игрока «Х» ").split()))
    else:
        move = list(map(int, input("Ход игрока «O» ").split()))
    while move[0]>3 or not move[0] or move[1]>3 or not move[1]:  # Проверка корректности ввода
            print("некорректные координаты, введите их правильно: ")
            move = list(map(int, input().split()))
    while move in L:  # сравнение координат с данными матрицы (есть ли там знак)
            print("Эта клетка уже заполнена, сделайте ход в другую: ")
            move = list(map(int, input().split()))
    L.append(move)
    if i % 2:
        M[move[0]*2-1][move[1]*2-1] = 'X'
    else:
        M[move[0]*2-1][move[1]*2-1] = 'O'
    for i in range(6):
        for j in range(6):
            print(M[i][j], end = " ")
        print()
    N = len(L)    # число ходов
    if 4 < N <= 9:
        winner_check(L, N)
        if winner_check(L, N):
            if N % 2:
                print("игрок «Х» победил, поздравляем!")
            else:
                print("игрок «О» победил, поздравляем!")
            break
        else:
            if N == 9:
                print("Ничья, победила дружба (здравый смысл)!")
