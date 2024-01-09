# 메뉴로 숫자를 입력받아 처리하는 프로그램 작성
# 1. 숫자 추가 / 2. 숫자 출력 / 3. 합계 / 4. 값으로 삭제 / 999. 종료

numbers = []
while True:
    print("------메뉴를 선택하세요------")
    print('1. 추가 / 2. 출력 / 3. 합계 / 4. 삭제 / 5. 평균 / 6. 자리바꾸기 / 999. 종료')
    pick_num = input("입력할 번호 -> ")
    
    if pick_num == '1':
        plus_num = int(input("추가할 숫자 -> "))
        numbers.append(plus_num)
    elif pick_num =='2':
        print(numbers)
    elif pick_num =='3':
        print('합계 : ',sum(numbers))
    elif pick_num =='4':
        minus_num = int(input("제거할 숫자 ->"))
        if minus_num in numbers:
            numbers.remove(minus_num)
            print("숫자를 제거했습니다.")
        else:
            print('리스트에서 입력하신 숫자를 찾지 못했습니다.')
    elif pick_num =='5':
        print(sum(numbers)/len(numbers))
        print("바꿀 숫자 두 가지의 순서를 입력하세요")
        print(numbers)
        first_num = int(input('첫 번째 숫자의 순서'))
        second_num = int(input('두 번째 숫자의 순서'))
        extra_num = numbers[first_num]
        numbers[first_num] = numbers[second_num]
        numbers[second_num] = extra_num
        print(numbers)
    elif pick_num == '999':
        print('프로그램을 종료합니다.')
        break