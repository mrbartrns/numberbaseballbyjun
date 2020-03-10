import random
import unittest

test_array1 = [1, 9, 4, 3]
answer_array1 = [1, 9, 4, 3]
number_array1 = [0, 2, 0, 2, 2, 0, 0, 0, 0, 2]


def rule_check(test_array, answer_array, number_array):
    count_2 = number_array.count(2)
    strike_count = 0
    ball_count = 0
    if count_2 == 0:
        print('OUT')
    else:
        for _ in range(4):
            if test_array[_] - answer_array[_] == 0:
                strike_count += 1
                ball_count = count_2 - strike_count
        if strike_count == 0:
            print('%dB' % ball_count)
        elif ball_count == 0:
            print('%dS' % strike_count)
        elif strike_count != 0 and ball_count != 0:
            print('%dS %dB' % (strike_count, ball_count))


rule_check(test_array1, answer_array1, number_array1)
