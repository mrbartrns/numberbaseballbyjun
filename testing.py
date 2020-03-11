from script import *


def num_check(num, answer_array_f):
    if 0 <= num < 10:
        answer_array_f.append(num)
        # 첫째 짜리에 0을 입력받을 경우, 다시 끄집어냄
        if answer_array_f[0] == 0:
            answer_array_f.pop()
            return -1
        # 위의 조건을 모두 만족시, array의 길이와 중복되는 숫자 검사
        else:
            # count_array는 숫자의 종류를 저장하는 배열로 rule_array와 동일한 역할을 하지만 길이가 다름
            count_array = []
            for i in range(10):
                count_array.append(answer_array_f.count(i))
            # 중복시 숫자를 끄집어냄
            for i in count_array:
                if i == 2:
                    answer_array_f.pop()
                    return 1
            return 0
    else:
        return 2


answer = []
num_flag = True
while num_flag:
    try:
        num = int(input('숫자를 입력하세요: '))
        num_checking = num_check_test(num, answer)
        if num_checking == -1:
            print('첫째 자리에는 0이 입력될 수 없습니다.')
        elif num_checking == 0:
            pass
        elif num_checking == 1:
            print('중복되는 숫자를 입력할 수 없습니다.')
        elif num_checking == 2:
            print('0보다 크거나 같고 10보다 작은 수를 입력하세요.')
        if len(answer) == 4:
            num_flag = False
    except ValueError:
        print('숫자만 입력할 수 있습니다.')
