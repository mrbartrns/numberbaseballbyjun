import random


class QuestionNumber:
    """
    이 클래스는 랜덤한 숫자를 배열로 만들어 저장하는 클래스입니다.
    """

    def __init__(self):
        self.init_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.test_array = random.sample(self.init_array, 4)
        first_zero = True
        while first_zero:  # 만약 0이 맨 앞자리에 올 경우, 숫자를 다시 추첨함.
            if self.test_array[0] == 0:
                self.test_array = random.sample(self.init_array, 4)
            else:
                first_zero = False
        # random module을 사용하지 않고 구현하는 방법 알아보기.

    def __repr__(self):
        return str(self.test_array)


testunit = QuestionNumber()
print(testunit.test_array)

# Todo: 0이 앞으로 올 경우, 다시 수를 추첨하는 방식 고려중
