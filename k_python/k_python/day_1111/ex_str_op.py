#문자열 str 타입 연산 수행
name = 'hong'
gender= "M"

#산술연산 수행----------------------------------------
#덧셈(+) : str + str = 문자열 연결
print(f'{name} + {gender} = {name+ gender}')
#str + int 안됨!!!! 오직 str + str 만!!!
#str 타입으로 형변환해서 덧셈 가능 => str(데이터)
print(f'{name} + {str(2022)} = {name+ str(2022)}')

#뺄셈(-) : str - str = 지원되지 않는 기능
#print(f'{name} - {gender} = {name- gender}')
 
#곱셈(*) : str * int = str을 지정된 정수만큼 반복
print(f'{name} * {5} = {name*5}')

#나머지(%): 문자열 안에 변수값 설정에 사용
# %알파벳 1개 => %d 정수, %f 실수, %s 문자열
print('%s, %d, %s' %(name, 12, gender))
print('%s, %s, %s' %(name, 12, gender))

#실습------------------------------------------------
#출력 => =================================
#                My Program
#       ==================================
a = "="
b = "My Program"
print(f'{ a * 30} ')
print(f'\t{b}')
print(f'{ a * 30} ')

print(f'==============================\n\tMy Program\n==============================')

print("="*30)
print("\tMy Program")
print("="*30)

print(("="*30 ) + "\n\tMy Program\n" + ("="*30))

#멤버 연산자------------------------------------------------------
#요소 in 그룹 : 요소가 그룹에 존재 하는지 true/False
#요소 not in 그룹 : 요소가 그룹에 존재하지 않으면 true/false
data = "Good"
print(f'G in {data}: {"G" in data}')
print(f'g in {data}: {"g" in data}')

print(f'G in {data}: {"G" not in data}')
print(f'g in {data}: {"g" not in data}')

print((20).real)

