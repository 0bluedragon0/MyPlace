# 두 숫자를 입력받아 큰 수를 가리는 함수

def big_num(a:int, b:int):
    if a>b:
        return a
    else:
        return b
        

# 숫자를 입력받아 절댓값을 계산하는 함수

def Juldae(a1:int):
    if a1<0:
        a1 = a1 * (-1)
        return a1
    return a1