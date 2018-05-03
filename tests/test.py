import unittest

from Life import Cell
from Life import Game


class TestCellMethods(unittest.TestCase):

    def test_equal(self):
        for i in Cell.__CELLS__:
            c1 = Cell(i)
            c2 = Cell(Cell.__CELLS__[i])
            c3 = Cell(i)
            self.assertEqual(c1, c2)
            self.assertEqual(c2, c3)
            self.assertEqual(c3, c1)

    def test_step(self):
        neighbours = [Cell(1), Cell(2), Cell(3)]
        self.assertEqual(Cell(0), Cell(2).step(neighbours))
        self.assertEqual(Cell(0), Cell(3).step(neighbours))
        neighbours.append(Cell(2))
        self.assertEqual(Cell(2), Cell(2).step(neighbours))
        neighbours.append(Cell(3))
        self.assertEqual(Cell(3), Cell(3).step(neighbours))
        neighbours.append(Cell(3))
        self.assertEqual(Cell(1), Cell(1).step(neighbours))
        self.assertEqual(Cell(3), Cell(0).step(neighbours))
        neighbours.append(Cell(2))
        self.assertEqual(Cell(2), Cell(0).step(neighbours))
        self.assertEqual(Cell(2), Cell(2).step(neighbours))
        self.assertEqual(Cell(3), Cell(3).step(neighbours))
        neighbours.append(Cell(2))
        self.assertEqual(Cell(0), Cell(2).step(neighbours))
        self.assertEqual(Cell(3), Cell(3).step(neighbours))
        neighbours.append(Cell(3))
        self.assertEqual(Cell(0), Cell(3).step(neighbours))


class TestGameMethods(unittest.TestCase):
    def tests_step(self):
        field = [
            [2, '#', 1, '.', 0],
            ['.', 2, 'F', 0, '#'],
            [2, 3, 'C', 'C', '.']
        ]
        current = "F##..\n.FF.#\nFCCC.\n"
        next_field = ".##..\nFF..#\n..C..\n"
        game = Game(field)
        self.assertEqual(current, str(game))
        game.step()
        self.assertEqual(next_field, str(game))


if __name__ == '__main__':
    unittest.main()
