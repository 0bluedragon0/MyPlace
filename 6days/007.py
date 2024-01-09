# 숫자를 입력받아 CR(합계, 평균)UD
#메뉴를 띄운다(1 : 숫자 추가, 2 : 숫자 출력, 999 : 종료)
# 코드는 수동적이어야 한다.
numbers = []
while True:
    print("===메뉴 선택===")
    print("1 : 추가, 2 : 합계, 3: 평균, 4: 리스트 출력, 5 : 삭제, 999 : 종료")
    select = input("번호를 입력하세요 : ")
    if select == '1':
        num = int(input('숫자 입력 : '))
        numbers.append(num)
    elif select == '2':
        print(f'합계 : {sum(numbers)}')
    elif select == '3':
        print(f'평균 : {sum(numbers)/ len(numbers)}')
    elif select =='4':
        print(numbers)
    elif select =='5':
        val = int(input('삭제할 값 입력 : '))
        if val in numbers:
            numbers.remove(val)
        else:
            print("입력하신 값이 리스트에 없습니다.")
    elif select=='999':
        print('이용해주셔서 감사합니다.')
        break
        