# 변수 생성
age = 19
jumsu = 79.8
value = -500

 # 글자 데이터일 경우 '글자', "글자", '''글자''', """글자"""

name = 'hong'
msg = "good luck"
comment = '''오늘은 화요일 입니다. 내일은 수요일 입니다. 
벌써 11월 9일입니다.'''

# 메모리에 저장된 데이터 읽어와서 화면에 출력
# => 출력기능 함수 print(출력데이터)
print(name)
print(age)
print(age, name, comment)

#데이터가 저장된 주소 확인 함수 
# => id(변수명), id(데이터)

print(id(age))
print(id('hello'))

# 동일 데이터 저장 변수들
num1=12
num2=12
print(id(num1), id(num2), id(12))
