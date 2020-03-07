import random


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
        self.init_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 한번 뽑은 숫자는 다시 나오게 하면 안되므로, 배열에서 제외되야 함.

    def __repr__(self):
        return str(self.init_array)


class AnswerNumber:
    """
    이 클래스는 플레이어가 숫자를 맞추는 클래스입니다.
    """


class Rule:
    """
    이 클래스는 게임의 규칙을 통해 해결해나가는 과정을 구현하는 클래스입니다.
    """
