import random

init_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


class QuestionNumber:
    """
    이 클래스는 랜덤한 숫자를 배열로 만들어 저장하는 클래스입니다.
    """

    def __init__(self):
        self.test_array = random.sample(init_array, 4)
        while True:  # 만약 0이 맨 앞자리에 올 경우, 숫자를 다시 추첨함.
            if self.test_array[0] == 0:
                self.test_array = random.sample(init_array, 4)
            else:
                break

    def __repr__(self):
        return str(self.test_array)


class AnswerNumber:
    """
    이 클래스는 플레이어가 숫자를 맞추는 클래스입니다.
    """

    def __init__(self):
        self.answer_array = []

    def enqueue(self, baseball_num):
        assert type(baseball_num) is int, '0보다 크거나 같은 수를 입력하세요!'
        self.answer_array.append(baseball_num)

    def __repr__(self):
        return str(self.answer_array)


test_unit = AnswerNumber()
test_unit.enqueue(3)
test_unit.enqueue(4)
test_unit.enqueue(5)
test_unit.enqueue(6)

print(test_unit)

test_unit2 = QuestionNumber()
print(test_unit2)