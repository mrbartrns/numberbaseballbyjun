# Function.py의 코드는 return값이 존재해야 함.


# 숫자의 범위 지정 및 자릿수 검사
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


# strike인지 ball인지 out인지 체크해주는 함수
# Todo: return값이 -1일경우, 상수이므로 Tuple로 받지 않으면 오류가 났었음.
def rule_check(test_array_f, answer_array_f, number_array_f):
    print(answer_array_f)
    count_2 = number_array_f.count(2)
    strike_count = 0
    if count_2 == 0:
        return -1, 0
    else:
        for i in range(4):
            if test_array_f[i] == answer_array_f[i]:
                strike_count += 1
        ball_count = count_2 - strike_count
        return strike_count, ball_count


def replay(y_n):
    while True:
        try:
            if y_n == 'Y' or y_n == 'y':
                return 0
            elif y_n == 'N' or y_n == 'n':
                return -1
            else:
                raise TypeError
        except TypeError:
            print('Y(y) 또는 N(n)만을 입력하세요.')


