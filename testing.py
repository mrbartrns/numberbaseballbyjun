from script import *
from function import *

s_val = 0
SCRIPT_VALUE_DIC = {'1': '첫', '2': '두', '3': '세', '4': '네'}


# Todo: 'n번째 숫자를 입력하세요.'로 변경하기
def play_game_test():
    welcome()
    round_on = True
    test_array = QuestionNumber()
    answer_array = AnswerNumber()
    rule_array = Rule(test_array.test_array)
    number_array = NumberIndex()
    while round_on:
        num_flag = True
        script_key = 1
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
        break


play_game_test()