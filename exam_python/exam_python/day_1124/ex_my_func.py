#--------------------------------------------------------------
#기    능: 2개 숫자를 덧셈 후 반환하는 기능
# 함수명 : plus
#매개변수: num1, num2
#반 환 값: 덧셈값
#---------------------------------------------------------------
def plus(num1,num2):
    value=num1+num2
    return value

print(plus(1,2))
#--------------------------------------------------------------
#기    능: 2개 숫자를 뺄셈 후 반환하는 기능
# 함수명 : minus
#매개변수: num1, num2
#반 환 값: 뺄셈값
#---------------------------------------------------------------
def minus(num1,num2):
    value=num1-num2
    return value
    
print(minus(2,1))
#--------------------------------------------------------------
#기    능: 2개 숫자를 곱셈 후 반환하는 기능
# 함수명 : multi
#매개변수: num1, num2
#반 환 값: 곱셈값
#---------------------------------------------------------------
def multi(num1,num2):
    value=num1*num2
    return value
    
print(multi(1,2))
#--------------------------------------------------------------
#기    능: 2개 숫자를 나눗셈 후 반환하는 기능
# 함수명 : division
#매개변수: num1, num2
#반 환 값: 나눗셈값
#---------------------------------------------------------------
def division(num1,num2):
    if num2>0:
        return num1/num2
    else:
        return None

    #return num1/num2 if num2>0 else None
    
#print(division(10,0)) => 에러 뜸 => if절 써야

#----------------------------------------------------------------
# <나의 계산기>
#----------------------------------------------------------------
# 1. 입  력
# 2. 덧  셈
# 3. 뺄  셈
# 4. 곱  셈
# 5. 나눗셈
# 6. 종  료
#----------------------------------------------------------------

def printMenu():
    print('-'*14)
    print('<나의 계산기>')
    print('-'*14)
    print('1. 입력')
    print('2. 덧셈')
    print('3. 뺼셈')
    print('4. 곱셈')
    print('5. 나눗셈')
    print('6. 종료')
    print('-'*14)


isCheck=False
while True:
    printMenu()

    choice=input("메뉴 선택(1~6):").strip()
    if choice=='6':
        print("나의 계산기 프로그램은 종료합니다.")
        break
    elif choice=='1':
        nums=input('숫자 2개 입력:(예: 1, 7)').strip()
        num1, num2 =nums.split(',')
        num1, num2 =int(num1), int(num2)
        print(f'num1 :{num1} / {type(num1)} , num2 :{num2} / {type(num2)}')
        isCheck=True
    elif choice=='2': #덧셈
        if isCheck:
            print(f'{num1}+{num2}={plus(num1,num2)}')
        else:
            print('입력된 데이터가 없습니다.')
    elif choice=='3': #뺄셈
        if isCheck:
            print(f'{num1}-{num2}={minus(num1,num2)}')
        else:
            print('입력된 데이터가 없습니다.')
    elif choice=='4': #곱셈
        if isCheck:
            print(f'{num1}*{num2}={multi(num1,num2)}')
        else:
            print('입력된 데이터가 없습니다.')
    elif choice=='5': #나눗셈
        if isCheck:
            print(f'{num1}/{num2}={division(num1,num2)}')
        else:
            print('입력된 데이터가 없습니다.')
    


    
        
        

