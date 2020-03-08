# 두 배열을 합친다면 하나의 for 문으로 해결도 가능
test1 = [1, 2, 3, 4]
test2 = [5, 6, 7, 4]
test3 = [1, 2, 3, 4, 5, 6, 7, 4]
test4 = []

# def rule(test1, test2):
def rule():
    """
    test_array 와 answer_array 요소를 각각 비교,(전체를 통채로 비교해서는 안됨)
    """


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