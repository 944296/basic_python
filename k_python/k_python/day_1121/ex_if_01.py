#제어문 - 조건문 if문
#-조건식에 따라서 실행되는 코드가 정해짐
#--------------------------------------------------
#다양한 데이터 자료형으로 조건식

num = []

print( num, bool(num))

if num:
    print("True인 경우 실행되는 코드1")
    print("True인 경우 실행되는 코드2")
else:
    print("False")
    print("거짓")

print("------end------")

#숫자가 짝수인지 홀수인지에 따라서
#짝수면 "짝수입니다.",
#홀수면 "홀수입니다." 출력하세요.
#----------------------------------------------------
# 2 4 6 8 10 ....=> %2 => 0
# 1 3 5 7 9 .... => %2 => 1

num=12

if num%2 == 0:
    print(f"{num}은 짝수입니다.")
else:
    print(f"{num}은 홀수입니다.")

#실습) 숫자를 입력받아서 해당 숫자가 3의 배수인지 아닌지 출력해주세요.

num=int(input("숫자를 입력하세요: ").strip())

if num%3 == 0:
    print(f"{num}은 3의 배수입니다.")
else:
    print(f"{num}은 3의 배수가 아닙니다.")

#숫자가 양수인지, 음수인지, 0인지 식별해서 출력하세요.
# num>0 num<0 num==0 => 다중조건(조건이 여러개)

#조건문 안에 조건문 ==> 중첩 조건문/중첩 if문 ---------
num = 7

if num>0:
    print(f"{num}은 양수")
else:
    if num<0:
        print(f"{num}은 음수")
    else:
        print(f"{num}은 영")


# if num>0:
#     print(f"{num}은 양수")

# if num<0:
#     print(f"{num}은 음수")    

# if num==0:
#     print(f"{num}은 영")

#다중조건문 ---------------------------------------------
if num>0:
    print(f"{num}은 양수")
elif num<0:
    print(f"{num}은 음수")
else:
    print(f"{num}은 영")