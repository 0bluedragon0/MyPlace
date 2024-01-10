# 1에서 10까지의 합계 : 55
#total = 0
#for x in range(1,11):
#    total = total + x
#print(total)
#
## 1에서 10까지의 3의 배수 출력
#for x1 in range(1,11):
#    if x1%3==0:
#        print(x1)

# 1~10사이의 3의 배수의 합계
#total = 0
#for x2 in range(1,11):
#    if x2% 3==0:
#        total = total + x2 
#print(total)   

#1~100사이의 7과 5의 공배수를 출력

for x3 in range(1,100):
    if x3%7==0 and x3%5==0:
        print(x3)
        
# 1 ~ 100사이의 5의배수와 7의 배수를 출력 단, 공배수는 제외
for x4 in range(1,101):
    if x4 % 5 == 0 or x4 % 7 == 0:
        if x4 % 5 == 0 and x4 % 7 == 0:
            continue
        else:
            print(x4, end=" ")
            
        
        