from unittest import TestCase

from src.main.part4.jumper import Jumper


class JumperTest(TestCase):

    def test_solution0(self):
        expected = Jumper.jumps(3, 1)
        actual = 3
        self.assertEqual(expected, actual)

    def test_solution1(self):
        expected = Jumper.jumps(3, 2)
        actual = 2
        self.assertEqual(expected, actual)

    def test_solution2(self):
        expected = Jumper.jumps(3, 3)
        actual = 1
        self.assertEqual(expected, actual)

    def test_solution3(self):
        expected = Jumper.jumps(16808, 282475250)
        actual = 16808
        self.assertEqual(expected, actual)

    def test_solution4(self):
        expected = Jumper.jumps(458777924, 7237710)
        actual = 2802257
        self.assertEqual(expected, actual)

    def test_solution5(self):
        expected = Jumper.jumps(823564441, 115438166)
        actual = 15497286
        self.assertEqual(expected, actual)
