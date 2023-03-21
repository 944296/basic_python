#SCOPE - 범위
#=> 변수의 사용 가능한 범위
#--------------------------------------------------------------------
#전역변수 Global Variable : 파이썬 파일 안에 모든곳에서 사용 가능한 변수
year=2022
msg='None'
#매개변수 month
def addYear(month):
    global year    # 전역변수 값 변경시 반드시 알림!!!
    year=year+1    # 이부분만 있으면 year 출력 오류 뜸
    msg='Happy'      
    print(year,month,msg) # 함수 내 msg 우선 사용!!


print('befor:',year)
addYear(12)
#print(year,month) =>  month땜에 오류. => 함수에서 사용되는 변수 매개변수, 함수 내부의 변수는 함수에서만 사용 되는 변수 => "지역변수"
# 함수에 포함된 지역변수는 함수 밖에서 사용 불가.
print('after:', year)



for _ in range(0):   #range(0)이라서 실행 안됨!!   
    total=10

if False:            #False이기때문에 절대 실행 안됨!!
    msg='Good Luck'

#print(year, total, msg)