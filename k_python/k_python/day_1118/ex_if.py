#제어문 : 실행 코드 제어
#-조건문 : 경우따른 코드 실행 여부 결정 코드
#-------------------------------------------------------
# 숫자가 양수인지 음수인지 검사후 출력해 주세요.
#양수 >0, 음수 <0
#
# num=int(input("숫자 입력:"))
num=10

if num>0:
    print(f"{num}은 양수입니다.")
else:
    print(f"{num}은 0 또는 음수입니다.")

print("-----END-------")

#  딕셔너리 안에 키 검사
jumsu={"kor":90, "eng":89}

# 딕셔너리의 키만 추출 => dict.keys()
keys=jumsu.keys()

subject="kor"

#print("math" in keys)
#print("kor" in keys)

print( subject in keys)

if subject in keys:
    print(f"{subject} => { jumsu[subject] } ")
else:
    print(f"{subject} 키는 존재하지 않습니다.")


#실습-----------------------------------------------------------------
#데이터를 입력받고 입력받은 데이터가 있다면 ok출력
#없다면 "데이터없음"출력

#data=input("입력하세요 :").strip()  # str의 공백제거 메소드 => .strip()

# if len(data)>0:
#     print("ok")
# else:
#     print("데이터없음")

#실습-------------------------------------------------------------------
#정수 데이터 입력 받은 후 정수만큼 "*"를 출력해주세요

# data=int(input("정수 데이터를 입력하세요:"))

# if data >=0:
#     print(data*'*')
# else:
#     print("데이터없음")


number="5 "
print(number.isdecimal())  # 10진수인가 => True/False  
print(number.isnumeric())  # 숫자냐 아니야 => 공백이 있으면 인식 안됨(False)

#방법1)
number=input("정수입력:").strip()   #공백제거
if (len(number)>0) and (number.isdecimal()): #정수이냐
    print("*"*int(number)) 
else:
    print("정수를 입력하세요.")

#방법2)
if (len(number)>0): #입력된 데이터가 있으면
    if number.isdecimal():  # 정수면
        print("*"*int(number))
    else:  # 정수가 아니면                                     # tab (들여쓰기) / shift+tab (빼내기)
        print("정수를 입력해라")
else: 
    print("공백이거나 입력된 데이터가 없음!")

