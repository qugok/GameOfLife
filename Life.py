class Cell:
    """
    класс клетки поля
    """
    __CELLS__ = {
        0: ".",
        ".": 0,
        1: "#",
        "#": 1,
        2: "F",
        "F": 2,
        3: "C",
        "C": 3
    }
    """
    словарь, соединяющий номера типов, и их отображение\n
    0 - пустая клетка\n
    1 - скала\n
    2 - пользоваетельское водоплавающее 1 (рыба)\n
    3 - пользоваетельское водоплавающее 2 (креветка)
    """

    __CELLS_STILL_ALIVE__ = {
        2: (2, 3),
        3: (2, 3),
    }
    """
    нижниие и верхние границы выживания соответствующего водоплавающего
    """

    __CELLS_BORN__ = {
        2: 3,
        3: 3
    }
    """
    условия зарождения соответствующего водоплавающего
    """

    def __init__(self, gut):
        """
        созданиие клетки
        :param gut: число, либо символ  из словаря __SELLS__, характеризующий клетку
        """
        if type(gut) == str:
            self._fill = self.__CELLS__[gut]
        else:
            self._fill = gut

    def __str__(self) -> str:
        return self.__CELLS__[self._fill]

    def __eq__(self, other) -> bool:
        return self._fill == other._fill

    def step(self, neighbours):
        """
        функция получения следующего состояния клетки
        :param neighbours: соседи данной клетки
        :return: клетку, которая будет находится на этом месте на следующем ходу
        """
        if self._fill == 1:  # скала
            return self
        if self._fill == 0:  # пустая клетка
            for (number, condition_born) in self.__CELLS_BORN__.items():
                if condition_born == neighbours.count(Cell(number)):
                    return Cell(number)
            return self
        # иначе пользоваетельское водоплавающее
        (low_alive_limit, high_alive_limit) = self.__CELLS_STILL_ALIVE__[
            self._fill]
        if low_alive_limit <= neighbours.count(
                Cell(self._fill)) <= high_alive_limit:
            return self
        return Cell(0)

    def add_animal(self, name: str, condition_born: int, low_alive_limit: int,
                   high_alive_limit: int):
        """
        добавление нового типа врдоплавающего\n
        рекамендуется делать это до созданиия объектов типа Cell
        :param name: символ, обазначающий это водоплавающее
        :param condition_born: условие зарождения
        :param low_alive_limit: нижняя граница выживания (колличество соседе того жн типа)
        :param high_alive_limit: верхняя граница выживания (колличество соседе того жн типа)
        """
        number = len(self.__class__.__CELLS_BORN__)
        self.__class__.__CELLS__[number] = name
        self.__class__.__CELLS__[name] = number
        self.__class__.__CELLS_BORN__[number] = condition_born
        self.__class__.__CELLS_STILL_ALIVE__[number] = (
            low_alive_limit, high_alive_limit)


class Game:
    """
    класс игры

    включает в себя поле на конкретном ходу
    """

    __neighboursCoordinates__ = [
        (0, 1),
        (0, -1),
        (1, 0),
        (1, 1),
        (1, -1),
        (-1, 0),
        (-1, 1),
        (-1, -1)
    ]
    """
    координаты соседей клетки
    """

    def __init__(self, field=None):
        """
        создание игры из поля
        :param field: собственно поле
        """
        self._field = []
        for row in field:
            new_row = []
            for element in row:
                new_row.append(Cell(element))
            self._field.append(new_row)

    def __str__(self) -> str:
        """
        отрисовка текущего состояния поля
        :return: поле в виде строки
        """
        return ''.join(
            [(''.join([str(t) for t in r])) + '\n' for r in self._field])

    def step(self, count: int = 1):
        """
        обновляем состояние поля при шаге
        :param count: колличество шагов
        """
        if count == 0:
            return
        new_field = []
        for i in range(0, len(self._field)):
            new_row = []
            for j in range(0, len(self._field[i])):
                neighbours = []
                for x, y in self.__neighboursCoordinates__:
                    if len(self._field) > i + x >= 0 and len(
                            self._field[i]) > j + y >= 0:
                        neighbours.append(self._field[i + x][j + y])
                new_row.append((self._field[i][j]).step(neighbours))
            new_field.append(new_row)
        self._field = new_field
        self.step(count - 1)
