import unittest
from script import *
from function import *
import random


class RuleCheckTest(unittest.TestCase):

    def test_rule_check_ball(self):
        rule1 = rule_check([8, 4, 9, 1], [5, 6, 0, 4], [1, 1, 0, 0, 2, 1, 1, 0, 1, 1])
        self.assertEqual(rule1, (0, 1))

    def test_rule_check_strike(self):
        rule2 = rule_check([2, 3, 4, 5], [2, 3, 5, 4], [0, 0, 2, 2, 2, 2, 0, 0, 0, 0])
        self.assertEqual(rule2, (2, 2))

    def test_rule_check_out(self):
        rule3 = rule_check([8, 4, 9, 1], [5, 6, 0, 3], [1, 1, 0, 1, 1, 1, 1, 0, 1, 1])
        self.assertEqual(rule3, -1)

    def test_num_check1(self):
        num1 = num_check(0, [])
        self.assertEqual(num1, -1)

    def test_num_check2(self):
        num2 = num_check(1, [1])
        self.assertEqual(num2, 1)

    def test_num_check3(self):
        num3 = num_check(1, [2, 3])
        self.assertEqual(num3, 0)

    def test_num_check4(self):
        num4 = num_check(10, [3, 0, 7])
        self.assertEqual(num4, 2)

    def test_replay_check1(self):
        rep1 = replay('Y')
        self.assertEqual(rep1, 0)

    def test_replay_check2(self):
        rep2 = replay('y')
        self.assertEqual(rep2, 0)

    def test_replay_check3(self):
        rep3 = replay('N')
        self.assertEqual(rep3, -1)

    def test_replay_check4(self):
        rep4 = replay('n')
        self.assertEqual(rep4, -1)


if __name__ == '__main__':
    unittest.main()
