list1 = [15, 20, 30, 90]
# list1의 길이를 재라 -> len()X

#a = 0
#for x in list1:
#    a += 1
#print(a)

# list1의 합계를 출력하시오

#Total = 0
#for x in list1:
#    Total = Total + x
#print(Total)

# list1의 평균(합계/개수)를 출력하시오

sum = 0
much = 0
for x in list1:
    sum = sum + x
    much += 1
print(f'평균은 ',sum/much)
    