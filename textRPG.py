char_lv = 1
char_hp = 50
char_atk = 10
char_def = 10
char_statepoint = 0

mon_grade = 1
mon_hp = 50
mon_atk = 7
mon_def = 7

while True:
    print("무엇을 하시겠습니까?")
    print("1. 전투 / 2. 포인트분배 / 3. 상점 / 999. 종료")
    selectnum = int(input("번호를 입력하세요 -> "))
    if selectnum == 1:
        print('난이도를 설정하세요')
        battle_lv = int(input("번호 입력 : "))
    
    elif selectnum == 999:
        print('게임을 종료합니다.')
        break
