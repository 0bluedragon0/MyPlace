# bool
b1, b2, b3, b4 = True, True, True, False
# and : 모두 다 참이어야 한다.
# or : 하나만 참이면 된다.
print(b1 and b2 and b3)
print(b1 and b2 and b4)
print(b1 or b2 or b4)

nai = 30
gender = '여자'
city = '인천'
# 나이가 20이상이고 성별은 여자
nai >= 20 and gender == '여자'

# 나이가 20이상이고 성별은 여지인 사람 또는 인천에 사는 사람
(nai>=20 and gender == '여자')or city == '인천'
# 35세 남자 인천거주
nai >= 20 and gender == '남자' and city == '인천'