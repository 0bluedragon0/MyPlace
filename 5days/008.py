"""
1. 값 추가 -> print('숫자 입력:')
2. 리스트 출력
999. 종료 -> 감사합니다.
"""
num_list = []

while True:
    print("1. 값 추가")
    print("2. 리스트 출력")
    print("3. 리스트 총합")
    print("4. 리스트 평균")
    print("999. 종료")
    select = input("번호 선택 : ")
    if select == '999':
        print('감사합니다.')
        break
    elif select == '1':
        add_list = int(input('리스트에 입력할 값을 입력하세요 -> '))
        num_list.append(add_list)
    elif select == '2':
        print(num_list)
    elif select == '3':
        sum_list = sum(num_list)
        print(sum_list)
    elif select == '4':
        print(f'입력한 수들의 평균 = ',int(sum(num_list)/len(num_list)))
    else:
        print('메뉴를 정확하게 입력하세요')