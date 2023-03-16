#맴버 연산자
# a in A => a가 A에 포함되면 True/ 그렇지 않으면 False
# a not in A => a가 A에 포함되지 않으면 True/ 그렇지 않으면 False
#-------------------------------------------------------------------------------

#Hello 단어 있고, 사용자가 입력한 알파벳이 Hello 단어에 포함되는지 결과를 출력

print("a" in "Hello")
print("lo" in "Hello")
print("h" in "Hello")

print("lo" in list("Hello")) 
print("l" in list("Hello"))
print("o" in list("Hello"))

#실습) 점수를 입력받고 학점을 A~F에서
#  해당점수의 학점을 출력하세요.

jumsu = int(input("점수를 입력하세요: "))
grade=''

if jumsu>=90:
    grade="A"
    #print(f"{jumsu}는 A학점입니다.")
elif jumsu>=80:
    grade="B"
    #print(f"{jumsu}는 B학점입니다.")
elif jumsu>=70:
    grade="C"
    #print(f"{jumsu}는 C학점입니다.")
elif jumsu>=60:
    grade="D"
    #print(f"{jumsu}는 D학점입니다.") 
elif jumsu>=50:
    grade="E"
    #print(f"{jumsu}는 E학점입니다.")
else:
    grade="F"
    #print(f"{jumsu}는 F학점입니다.")
print(f"{jumsu}는 {grade}학점")

#(실습) 
member=["마징가","홍길동","베트맨","세종대왕","나"]
ismember=False

name=input("이름을 입력하세요: ")

if name in member:
    ismember=True
#else:
#    ismember=False
print(f"{name}은 우리맴버 : {ismember}")
 
#실습)----------------------------------------------------------------------
#nums=[16,3,7,9,12]
#사용자로부터 숫자를 입력받고 존재하지않는 숫자면
#추가해주시고, 존재하지않는 숫자면 "이미존재합니다"라고
#출력해주세요.

nums=[16,3,7,9,12]
num=int(input("숫자를 입력하세요: "))

if num in nums:
    print("이미존재합니다")
else:
    nums.append(num) #리스트 추가 메소드 => .append()
print(nums)

nums.insert(0,1) # => 지정된 위치에 추가해주는 메서드 (0번 자리에 1을 넣겠다.)
print(nums)
nums.append(5) # => 제일 뒤에 추가해주는 메서드
print(nums)


#실습-------------------------------------------------------------------------
#nums=[16,3,7,9,12]
#사용자로부터 숫자를 입력받고 존재하지않는 숫자면
#추가해주시고, 존재하지않는 숫자면 "이미존재합니다"라고
#출력해주세요.
#단 가장 작은값보다 크고, 가장 큰 값보다 작은 경우만 추가

#방법1
nums=[16,3,7,9,12]
num=int(input("숫자를 입력하세요: "))

if (num not in nums) and (num<max(nums)) and (num>min(nums)):
    nums.append(num)
else:
    print("이미존재합니다")

#방법2
if num not in  nums:
    if num<max(nums) and num>min(nums):
        nums.append(num)
else:
    print("이미 존재")





