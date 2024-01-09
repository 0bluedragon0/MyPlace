jumin = '961011-1021023'
gender = jumin[7]

# 남자인지 여자인지
if gender == '1':
    print('남자')
else:
    print('여자')
    
# 둘 중에 하나 if문을 한 줄로 -> 삼항연산자
# 복잡한 조건 삼항연산은 쓰지 말자 -> 스파게티 코드
print("남자" if gender =='1' else "여자")

# gender가 1 또는 3 또는 5면 남자, 2, 4, 6이면 여자
"남자" if gender == '1' or gender =='3' or gender=='5' else "여자"
"남자" if gender in ('1', '2', '3') else "여자"

# 주민번호로 나이 출력하기
# 1. 올해의 연도
# 2. 태어난 연도
# 3. 주민번호 앞 2자리를 슬라이싱한다. -year
# 4. 주민번호 7번째가 '1' 또는 '2' -> '19' + year
# 5. 주민번호 7번째가 '3' 또는 '4' -> '20' + year
# 3. 올해의 연도 - int(태어난 연도)
import datetime.datetime.date
this_year = datetime.datetime.now().year
year = jumin[0:2]
if jumon[7] in ('1', '2'):
    year = '19' + year
elif jumin[7] in ('3', '4'):
    year = int('20' + year)
print(f'{this_year-year}세')
