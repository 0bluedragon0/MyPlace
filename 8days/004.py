# 정수변수를 2개 만들어, 나눗셈 결과를 출력하시오
# 예외처리가 필요하면 예외처리하시오

try:
    fir_num = 20
    sec_num = 5

    def nanugi():
        total = fir_num/sec_num
        trash = fir_num%sec_num
    
        return total, trash
except:
    print("0으로 나눌 수 없습니다.")