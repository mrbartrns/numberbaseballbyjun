# 두 배열을 합친다면 하나의 for 문으로 해결도 가능
test1 = [1, 2, 3, 4]
test2 = [5, 6, 7, 4]
test3 = [1, 2, 3, 4, 5, 6, 7, 4]
test4 = []

for i in range(0, 10):
    test4.append(test3.count(i))

if test4.count(1) == 8:
    print('OUT')

'''
룰 OUT 구현 및 strike와 ball 구현하는 방법 생각해보기
OUT일 경우 count 하여 1의 갯수가 8개인경우 해당
strike일 경우 1의 갯수가 7개 이하 및 index가 동일해야함
ball일 경우 1의 갯수가 7개 이하 및 index가 동일하지 않아야함
'''
import random
import unittest

init_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def welcome():
    """
    Welcome message at beginning of game with basic win conditions
    :return: None
    """
    welcome_string = "LET'S NUMBER BASEBALL BEGINS!"
    print("\n" + "#" * len(welcome_string))
    print(f"{welcome_string}")
    print("#" * len(welcome_string) + "\n")
    print(" - 게임의 룰은 간단합니다; \
4개의 무작위한 숫자가 주어질 것입니다.")
    print(" - 숫자의 범위는 0에서 9까지이며, 숫자는 중복되지 않습니다.")
    print(" - 숫자의 위치와 종류를 모두 맞추게되면 승리하게 됩니다!\n")
    rule = "게임 규칙 설명:"
    print(f"{rule}")
    print("S (Strike): 숫자가 존재하고 그 숫자의 위치가 정확함")
    print("B (Ball): 숫자가 존재하나 그 숫자의 위치가 틀림")
    print("OUT (Out): 숫자가 배열에 존재하지 않음")


class QuestionNumber:
    """
    이 클래스는 랜덤한 숫자를 배열로 만들어 저장하는 클래스입니다.
    """

    def __init__(self):
        self.test_array = random.sample(init_array, 4)

        # 만약 0이 맨 앞자리에 올 경우, 숫자를 다시 추첨함.
        while True:
            if self.test_array[0] == 0:
                self.test_array = random.sample(init_array, 4)
            else:
                break

    # test_array의 요소를 보여주는 함수
    def __repr__(self):
        return str(self.test_array)

    # test_array의 길이를 보여주는 함수
    def __len__(self):
        return len(self.test_array)


class AnswerNumber:
    """
    이 클래스는 플레이어가 숫자를 맞추는데 사용되는 클래스입니다.
    """

    def __init__(self):
        self.answer_array = []

    def enqueue(self, baseball_num):
        assert type(baseball_num) is int, '0보다 크거나 같은 정수를 입력하세요!'
        self.answer_array.append(baseball_num)

    def pop(self):
        self.answer_array.pop(0)

    # answer_array의 요소를 보여주는 함수
    def __repr__(self):
        return str(self.answer_array)

    # answer_array의 길이를 보여주는 함수
    def __len__(self):
        return len(self.answer_array)


class Rule:
    """
    이 클래스는 게임의 규칙을 통해 해결해나가는 과정을 구현하는 클래스입니다.
    """

    # Todo: pass부분 꼭 지울것!

    def __init__(self):
        self.rule_array = []
        for _ in range(4):
            self.rule_array.append(test_array.test_array[_])

    # __init__ 과 따로 두어야 하는 이유는 한 턴이 끝난 후 배열이 초기화 되어야 하기 때문임.
    def rule_append(self):
        for _ in answer_array.answer_array:
            self.rule_array.append(_)

    def __repr__(self):
        return str(self.rule_array)

    def __len__(self):
        return len(self.rule_array)


class NumberIndex:
    def __init__(self):
        self.number_array = []
        self.Index_array = []
        for _ in range(10):
            self.number_array.append(rule_array.rule_array.count(_))

    def __repr__(self):
        return str(self.number_array)

    def __len__(self):
        return len(self.number_array)


def num_input():
    i = 0
    while True:
        num = int(input('숫자를 입력하세요: '))
        answer_array.enqueue(num)
        if answer_array.answer_array[0] == 0:
            print('첫째 자리에는 0이 입력될 수 없습니다.')
            answer_array.pop()
        else:
            i += 1
        if i == 4:
            break


# 아직 사용하면 안됨!
test_array = QuestionNumber()
answer_array = AnswerNumber()
rule_array = Rule()
number_array = NumberIndex()
print(test_array)
num_input()
print(answer_array)
print(rule_array)
print(number_array)
