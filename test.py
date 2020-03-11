import unittest
from script import *


class RuleCheckTestcase(unittest.TestCase):

    def test_rule_check_ball(self):
        rule1 = rule_check([8, 4, 9, 1], [5, 6, 0, 4], [1, 1, 0, 0, 2, 1, 1, 0, 1, 1])
        self.assertEqual(rule1, (0, 1))

    def test_rule_check_strike(self):
        rule2 = rule_check([2, 3, 4, 5], [2, 3, 5, 4], [0, 0, 2, 2, 2, 2, 0, 0, 0, 0])
        self.assertEqual(rule2, (2, 2))


if __name__ == '__main__':
    unittest.main()
