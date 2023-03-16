#숫자 데이터 타입
#다양한 숫자 표기법
bnum=0b11101 #2진수
onum=0o35    #8진수
dnum=29      #10진수
xnum=0x1d    #16진수
print(f'bnum: {bnum}, {bnum:#b}')
print(f'onum: {onum}, {onum:#o}')
print(f'dnum: {dnum}, {dnum:#d}')
print(f'xnum: {xnum}, {xnum:#x}')

#숫자에대한 16진수 8진수 2진수 값을 알려주는 내장함수
print(31, hex(31), oct(31), bin(31))

#산술연산자 => +, -, *, /, //, %, **

num1 = 11
num2 = 3
print(f'{num1}+{num2}={num1+num2}')
print(f'{num1}-{num2}={num1-num2}')
print(f'{num1}*{num2}={num1*num2}')
print(f'{num1}/{num2}={num1/num2}')

print(f'몫      {num1}//{num2}={num1//num2}')
print(f'나머지  {num1}%{num2}={num1%num2}')
print(f'제곱    {num1}**{num2}={num1**num2}')


#비교연산자 => >, <, >=, <=, ==, !=
print(f'{num1}>{num2} = {num1>num2}')
print(f'{num1}<{num2} = {num1<num2}')
print(f'{num1}>={num2} = {num1>=num2}')
print(f'{num1}<={num2} = {num1<=num2}')
print(f'{num1}=={num2} = {num1==num2}')
print(f'{num1}!={num2} = {num1!=num2}')


#논리연산자 
# => Left and Right : 왼쪽/오른쪽 모두 True
# => Left or Right : 왼쪽/오른쪽 중 한개이상만 True면 True
# => not Data : True > False, False > True

print(f'{num1}>{num2} and {num1} == {num2} : {(num1>num2)and(num1==num2)}')
print(f'{num1}<{num2} and {num1} == {num2} : {(num1<num2)and(num1==num2)}')
print(f'{num1}>{num2} and {num1} >= {num2} : {(num1>num2)and(num1>=num2)}')

print('-----------------------------------------------------------------')

print(f'{num1}>{num2} or {num1} == {num2} : {(num1>num2)or(num1==num2)}')
print(f'{num1}<{num2} or {num1} == {num2} : {(num1<num2)or(num1==num2)}')
print(f'{num1}>{num2} or {num1} >= {num2} : {(num1>num2)or(num1>=num2)}')


print('------------------------------------------------------------------')

print(f"not {num1}>{num2} : {not num1>num2}")
print(f"not {num1}=={num2} : {not num1==num2}")


#객체 비교연산자
# A is B     => A와 B가 같은 객체이면 True
# A is not B => A 와 B가 다른 객체이면 True

num1 = 10
num2 = num1

print(f'id(num1) : {id(num1)}, id(num2) : {id(num2)}')
print(f'num1 : {num1}, num2 : {num2}')
print(f'{num1} is {num2} : {num1 is num2}')
print(f'{num1} == {num2} : {num1 == num2}')

print("-----------------------------------------------------")
num2 = 10.0
print(f'id(num1) : {id(num1)}, id(num2) : {id(num2)}')
print(f'num1 : {num1}, num2 : {num2}')
print(f'{num1} is {num2} : {num1 is num2}')
print(f'{num1} == {num2} : {num1 == num2}')

#----------------------------------------------------------------
#형변환 type casting
# 자료형 즉 data type을 변경시켜주는 것
# 데이터 손실이 발생도 가능
# 내장 함수 => 자료형이름() int(), float(), str()...
#----------------------------------------------------------------
avg = 89.23

print(f'{avg} => {type(avg)}')

#해당 순간만 타입이 변경됨
print(f'{int(avg)} => {type(int(avg))}')

#int 타입으로 변환된 데이터를 다시 저장
#영구적으로 변경
avg=int(avg)
print(f'{avg} => {type(avg)}')

#내장함수 => bin(), oct(), hex()
number=31
print(f"{number} 2진수 => {bin(number)}")
print(f"{number} 8진수 => {oct(number)}")
print(f"{number} 16진수 => {hex(number)}")

average=98.7
#=>정수로 변환 
print(int(average))
average=int(average)

year=2022
print(float(year))
year=float(year)



num1=input("입력:")
num2=input("입력:")
#산술연산
print(f"{num1}+{num2}={num1+num2}")
#입력받은 데이터의 타입확인=>type(변수명)
print(f"num1의 타입 : {type(num1)}")
#input()함수로 입력받은 데이터는 전부 str타입
#str => int
num1=int(num1)
num2=int(num2)
print(f"{num1}+{num2}={num1+num2}")


