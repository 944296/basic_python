#문자데이터 => str타입 자료형
#표현방법 = > '문자', "문자", '''문자''', """문자"""
#이름 데이터 저장하기
name = '마징가'
name= "마징가"
name= "maginga"
#name 변수를 통해서 데이터 출력
print(f"name => {name}")


#str에서 문자 1개만 출력하기
#인덱싱(indexing)

#"m  a  g i  n  g  a"
# 0  1  2  3  4  5 6
# -7 -6 -5 -3 -2 -1
 
 
#변수명[인덱스]

print(name[0], name[-7])


#실습 "good luck~!" 문자열에서 luck만 출력하기

a = "good luck~!"
print(a[5],a[6],a[7],a[8])

#슬라이싱 => 문자열에서 구간(범위) 정해서 문자열 잘라내기
#=> 변수명[시작인덱스:끝인덱스+1]
#=> 변수명[시작인덱스: ] 끝까지
#=> 변수명[ :끝인덱스+1] 처음부터 즉 0번부터
#=> 변수명[ : ] 처음부터 끝까지
print(a[5:8])
print(a[5:9])
print(a[-6:-2])
print(a[5:-2])

#실습 "merry christmas~ 2022 12 24^^"
b="merry christmas~ 2022 12 24^^"
#1. 년월일만 출력하기
print(b[-12:-2])
#2. christmas~ 출력하기
print(b[6:16])
#3. 2022 12 24^^ 출력하기
print(b[-12:])
#4. "merry"출력하기
print(b[:5])

#실습--------------------------------------
strnumber = "CODE_123456789"
#             01234567890123
#1. "13579"만 출력
print(strnumber[5],strnumber[7],strnumber[9],strnumber[11],strnumber[13])
#연속되지 않지만 규칙이 있음 => 슬라이싱
#변수명[시작인덱스:끝인덱스+1:규칙/간격]
print(strnumber[5:14:2], strnumber[5::2])

#실습-----------------------------------------
#생년월일 계절을 한번에 입력받아서 년, 월, 일, 계절을 
#4개의변수에 저장하기

#입력받기 
birth=input("생년월일과 계절을 입력하세요.")
#입력받은 데이터의 타입 확인
print(f'타입:{type(birth)}')
#년,월,일,계절을 문자열에서 추출해서 변수에 저장
year=birth[:4]
month=birth[4:6]
day=birth[6:8]
season=birth[-2:]
print("%s년 %s월 %s일 %s계절에 태어남" %(year,month,day,season))
print(f"{year}년 {month}월 {day}일 {season}에 태어남.")

print(f"년 추출 : {year}")
print(f"월 추출 : {month}")
print(f"일 추출 : {day}")
print(f"계절 추출 : {season}")
