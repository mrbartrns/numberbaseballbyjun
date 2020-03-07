import random


class QuestionNumber:
    """
    이 클래스는 랜덤한 숫자를 배열로 만들어 저장하는 클래스입니다.
    """

    def __init__(self):
        self.init_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 한번 뽑은 숫자는 다시 나오게 하면 안되므로, 배열에서 제외되야 함.

    def __repr__(self):
        return str(self.init_array)


testunit = QuestionNumber()
print(testunit.init_array)

flag = True
random_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
test_array = random.sample(random_array, 4)
print(test_array)