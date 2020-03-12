import random
from function import *

init_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
SCRIPT_VALUE_DIC = {'1': '첫', '2': '두', '3': '세', '4': '네'}


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
    def __init__(self, test_array_f):
        self.rule_array = []
        for i in range(4):
            self.rule_array.append(test_array_f[i])

    def __repr__(self):
        return str(self.rule_array)

    def __len__(self):
        return len(self.rule_array)

    def rule_append(self, answer_array_f):
        for i in answer_array_f:
            self.rule_array.append(i)

    # __init__ 과 따로 두어야 하는 이유는 한 턴이 끝난 후 배열이 초기화 되어야 하기 때문임.
    def reset(self, test_array_f):
        self.rule_array = []
        for i in range(4):
            self.rule_array.append(test_array_f[i])


# 숫자의 갯수 저장
class NumberIndex:
    def __init__(self):
        self.number_array = []

    def num_append(self, rule_array_f):
        for i in range(10):
            self.number_array.append(rule_array_f.count(i))

    def __repr__(self):
        return str(self.number_array)

    def __len__(self):
        return len(self.number_array)

    def reset(self):
        self.number_array = []


def game_over():
    print('게임이 종료됩니다. 플레이 해주셔서 감사합니다.')


# 게임을 실행하는 함수
def play_game():
    welcome()
    round_on = True
    num_flag = True
    test_array = QuestionNumber()
    answer_array = AnswerNumber()
    rule_array = Rule(test_array.test_array)
    number_array = NumberIndex()
    round_count = 0
    # 한세트의 게임이 끝날때 까지 진행
    while round_on:
        script_key = 1
        round_count += 1
        round_string = f'시도 횟수: {round_count}회'
        print(round_string)
        # Todo: 지워야 함!
        print(test_array.test_array)
        # 숫자 4개를 받을 때 까지 진행
        while num_flag:
            try:
                script_value = SCRIPT_VALUE_DIC[str(script_key)]
                script_value_input_string = f'{script_value}번째 값을 입력하세요:'
                print(script_value_input_string, end=' ')
                num = int(input())
                num_checking = num_check(num, answer_array.answer_array)
                if num_checking == -1:
                    print('첫째 자리에는 0이 입력될 수 없습니다.')
                elif num_checking == 0:
                    script_key += 1
                    pass
                elif num_checking == 1:
                    print('중복되는 숫자를 입력할 수 없습니다.')
                elif num_checking == 2:
                    print('0보다 크거나 같고 10보다 작은 수를 입력하세요.')
                if len(answer_array) == 4:
                    num_flag = False
            except ValueError:
                print('숫자만 입력할 수 있습니다.')
        rule_array.rule_append(answer_array.answer_array)
        number_array.num_append(rule_array.rule_array)
        rule_check_test = rule_check(test_array.test_array, answer_array.answer_array, number_array.number_array)
        if rule_check_test == -1:
            print('OUT')
        elif rule_check_test[0] == 0:
            print('%dB' % rule_check_test[1])
        elif rule_check_test[1] == 0:
            print('%dS' % rule_check_test[0])
        elif rule_check_test[0] != 0 and rule_check_test[1] != 0:
            print('%dS %dB' % (rule_check_test[0], rule_check_test[1]))

        # 4 strike 달성 시:
        if rule_check_test[0] == 4:
            conguratulation_string = f'축하합니다. 당신은 {round_count}번의 시도 끝에 맞추셨습니다.'
            print(conguratulation_string)
            y_n_string = input('게임을 종료합니까? 종료하려면 Y를, 다시 시작하려면 N을 누르세요: ')
            regame = replay(y_n_string)
            if regame == 0:
                round_on = False
            elif regame == -1:
                round_on = True
                num_flag = True
                round_count = 0
                test_array.reset()
                answer_array.reset()
                rule_array.reset(test_array.test_array)
                number_array.reset()

        else:
            round_on = True
            num_flag = True
            answer_array.reset()
            rule_array.reset(test_array.test_array)
            number_array.reset()


if __name__ == "__main__":
    play_game()
