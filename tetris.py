import sys

workspace = (3, 5)
pl_Q = [((2, 2), 1)]
pl_L = [((3, 2), 1), ((2, 2), 2)]

pl_Q_cap = 0
pl_L_cap = 0
WS_cap = workspace[0] * workspace[1]
for i in pl_Q:
    pl_Q_cap += i[0][0] * i[0][1] * i[1]
for i in pl_L:
    pl_L_cap += (i[0][0] + i[0][1] - 1) * i[1]

pl_cap = pl_L_cap + pl_Q_cap
if pl_cap > WS_cap:
    print("False")
    sys.exit()
else:
    print("First stage done")
# создаем координаты


class WorkspaceClass:
    def __init__(self, a, b):
        self.max_len = a
        self.max_width = b
        self.len = [0] * a
        self.wid = [0] * b

    def pl_Q(self, length, width):
        set_x = self.wid.index(min(self.wid))
        set_y = self.len.index(min(self.len))

        print(set_x, set_y)

        if length < self.max_len and width < self.max_width:
            pass
        else:
            return False
        # если фигура больше поля - возвращает False - проверка на размер в рамках ориджина
        print('check1')
        # ищем место для фигуры - влезает по горизонтали и по вертикали, \
        # по горизонтали минимальное значение координаты и влезает, по \
        # вертикали - аналогично. сначала - проверка на горизонталь, \
        # если нет - ориджин по вертикали +1 и повтор проверки
        while (set_x + length) > self.max_len:
            set_y += 1
            set_x = self.len[self.len.index(set_y)]

        for _ in range(length):
            self.len[set_x + _] += length
        for _ in range(width):
            self.wid[set_y + _] += length


tetris = WorkspaceClass(workspace[0], workspace[1])

tetris.pl_Q(2, 2)
tetris.pl_Q(2, 2)
