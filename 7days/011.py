numbers = []
index = 0

def Plus_num():
    add_num = int(input("추가할 값을 입력하세요 ->"))
    numbers.append(add_num)
    
def Enter_list():
    print(numbers)
    
def Update_num():
    original_value = int(input("업데이트할 숫자를 입력하세요 ->"))
    for num in numbers:
        if original_value == num:
            update_value = int(input("새롭게 업데이트할 값을 입력하세요"))
            numbers = update_value
        index = index + 1
    if original_value != num:
        print("찾으시는 숫자가 없습니다.")
        
def delete_num():
    origin_del_num = input("삭제할 숫자를 입력하세요")
    for num2 in numbers:
        if origin_del_num == num2:
            numbers.remove(origin_del_num)
            print("삭제되었습니다.")
            break
    if origin_del_num != num2:
        print("찾으시는 숫자가 없습니다.")    

while True:
    print("### Menu - Select ###")
    print("1. 추가 / 2. 목록 / 3. 업데이트 / 4. 삭제 / 999. 종료")
    select_num = input("번호를 입력하세요 -> ")
    if select_num == '1':
        Plus_num()
    elif select_num == '2':
        Enter_list()
    elif select_num == '3':
        Update_num()
    elif select_num == '4':
        delete_num()
    elif select_num == '999':        
        print("프로그램을 종료합니다.")
        break
    