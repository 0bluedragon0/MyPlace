todos=[]
# 할 일 - 할 일 번호, 할 일, 완료
todo1 = {"tno" : 1, "title" : "자바공부", "finish" : False}
todo2 = {"tno" : 2, "title" : "스프링공부", "finish" : False}
todo3 = {"tno" : 3, "title" : "파이썬공부", "finish" : False}

todos.append({"tno" : 1, "title" : "자바공부", "finish" : False})
todos.append({"tno" : 2, "title" : "스프링공부", "finish" : False})
todos.append({"tno" : 3, "title" : "파이썬공부", "finish" : False})

tno = 4

def print_todos():
    for item in todos:
        print(item)

def add_todo():
    title = input('할 일 입력 : ')
    todos.append({"tno":tno,'title': title, 'finish' : False})
    tno = tno + 1

def toggle_finish():
    pass

def delete_todo():
    pass


while True:
    print('### 할 일 관리 ###')
    print('1:목록 / 2:추가 / 3:변경 / 4: 삭제 / 999.종료')
    select = input('메뉴 선택 : ')
    if select == '1':
        print_todos()
    elif select == '2':
        add_todo()
    elif select == '3':
        toggle_finish()
    elif select == '4':
        delete_todo()
    elif select == '999':
        print("이용해주셔서 감사합니다.")
        break

