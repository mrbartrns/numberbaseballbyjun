import random

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

    def __repr__(self):
        return str(self.test_array)

    def __len__(self):
        return len(self.test_array)

    def reset(self):
        self.test_array = random.sample(init_array, 4)


class AnswerNumber:
    """
    이 클래스는 플레이어가 숫자를 맞추는데 사용되는 클래스입니다.
    """

    def __init__(self):
        self.answer_array = []

    def __repr__(self):
        return str(self.answer_array)

    def __len__(self):
        return len(self.answer_array)

    def reset(self):
        self.answer_array = []


class Rule:
    """
    이 클래스는 게임의 규칙을 만들어 나가는데 필요한 클래스입니다.
    """

    # append를 따로 해야 하는 이유는, rule_array와 test_array는 구별되어야 하기 때문
    def __init__(self):
        self.rule_array = []
        for i in range(4):
            self.rule_array.append(test_array.test_array[i])

    def __repr__(self):
        return str(self.rule_array)

    def __len__(self):
        return len(self.rule_array)

    def rule_append(self):
        for i in answer_array.answer_array:
            self.rule_array.append(i)

    # __init__ 과 따로 두어야 하는 이유는 한 턴이 끝난 후 배열이 초기화 되어야 하기 때문임.
    def reset(self):
        self.rule_array = []
        for i in range(4):
            self.rule_array.append(test_array.test_array[i])


# 숫자의 갯수 저장
class NumberIndex:
    def __init__(self):
        self.number_array = []

    def num_append(self):
        for i in range(10):
            self.number_array.append(rule_array.rule_array.count(i))

    def __repr__(self):
        return str(self.number_array)

    def __len__(self):
        return len(self.number_array)


# 숫자를 입력받는 함수
def num_input(answer_array_f):
    num_flag = True
    while num_flag:
        num = int(input('숫자를 입력하세요: '))
        num_check(num, answer_array_f)
        if len(answer_array_f) == 4:
            num_flag = False
    # 숫자를 받은 즉시 number_array를 만든다.
    rule_array.rule_append()
    number_array.num_append()


# 숫자의 범위 지정 및 자릿수 검사
def num_check(num, answer_array_f):
    if 0 <= num < 10:
        answer_array_f.append(num)
        # 첫째 짜리에 0을 입력받을 경우, 다시 끄집어냄
        if answer_array_f[0] == 0:
            print('첫째 자리에는 0이 입력될 수 없습니다.')
            answer_array_f.pop()
        # 위의 조건을 모두 만족시, array의 길이와 중복되는 숫자 검사
        else:
            # count_array는 숫자의 종류를 저장하는 배열로 rule_array와 동일한 역할을 하지만 길이가 다름
            count_array = []
            for i in range(10):
                count_array.append(answer_array_f.count(i))
            # 중복시 숫자를 끄집어냄
            for i in count_array:
                if i == 2:
                    print('중복되는 숫자를 입력할 수 없습니다.')
                    answer_array_f.pop()
    else:
        print('0보다 크거나 같고 10보다 작은 수를 입력하세요.')


# strike인지 ball인지 out인지 체크해주는 함수
def rule_check(test_array_f, answer_array_f, number_array_f):
    count_2 = number_array_f.count(2)
    strike_count = 0
    ball_count = 0
    if count_2 == 0:
        print('OUT')
    else:
        for i in range(4):
            if test_array_f[i] == answer_array_f[i]:
                strike_count += 1
                ball_count = count_2 - strike_count
        if strike_count == 0:
            print('%dB' % ball_count)
        elif ball_count == 0:
            print('%dS' % strike_count)
        elif strike_count != 0 and ball_count != 0:
            print('%dS %dB' % (strike_count, ball_count))

# Todo: 시도횟수 count 만들기, try 문으로 str 입력받지 못하게 하기


# 아직 사용하면 안됨!
test_array = QuestionNumber()
answer_array = AnswerNumber()
rule_array = Rule()
number_array = NumberIndex()
