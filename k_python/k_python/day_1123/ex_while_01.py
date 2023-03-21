#while 반복문
#-반복의 횟수가 고정이 아닌경우 사용 하는 반복문
#-단순 카운팅용 반복문
#-필수조건) 반복을 중단 할 수있는 코드 필수
#-----------------------------------------------------

#무한 반복문 ------------------------------------------
#반드시 반복을 종료할 수있는 코드 또는 업데이트 필수
# while 1:         # 1=True
#     print('1')
# while ' ':
#     print('1')

#while 반복문 - (1) 반복 카운팅-------------------------
#20번 "Hello World" 출력하기
count=1
while count<=20:
    print("Hello World")
    count=count+1  # 필수부분 - 해당코드가 없으면 무한반복

count=20
while count>0:
    print("Hello World")
    count=count-1

for n in range(20):
    print("Hello World")

# break => for/while 반복문에서 반복을 중단시키는 키워드
#---------------------------------------------------------------
# 1부터 100까지 숫자를 하나씩 더해서
# 덧셈의 결과가 71보다 작을때까지만 더해주세요.

num=1
total=0

while num<=100:
    total=total+num
    print(f'num => {num}, total=>{total}')
    if total>=71: break   #실행구문이 하나뿐이면 옆에 적어도됨.
    num=num+1             # total>=71이 true이면 즉시 나가는 break 실행/ total>=71이 false이면 num=num+1 돌리기

print(f'total=>{total}, num => {num}')


total=0
for num in range(1,101):
    total=total+num
    if total>=71: break

# continue 계속해서....=>for/while 반복문에서 
#                       아래 코드 실행하지 않고, 
#                       제일 위에 코드로 돌아감
#-------------------------------------------------------------------------------------------------------------
# 1 ~ 20 까지 출력
num=1
while num<=20:
    print(num)
    num=num+1
# 1 ~ 20에서 2의 배수 빼고 출력 

#방법1
num=1
while num<=20:
    if num%2: #2의 배수가 아니면
        print(num) #출력
    num=num+1

#방법2
num=0
while num<=20:
    num=num+1    #num%2가 false이면 num=num+1 돌리기 
    if not num%2: continue   # num%2가 true일때 continue 
    print(num)

# num=1                                
# while num<=20:
#     if not num%2: continue  
#     print(num)
#     num=num+1                                  

isEnd=False                                      
for n in  [1,2,3]:
    if isEnd: break   #isEnd=True가 되서 break 
    for n2 in [11,22,33]:
        if n2>=20:     #n2>=20이면  22일때
            isEnd=True #isEnd=True가 되고
            break      #break    
        print(f'n2=>{n2}') #n2>=20이 아니면  11일때 => n2=11
    print(f'n=>{n}') # => n=1


# for n2 in [11,22,33]:
#     if n2>=20: 
#         break
#     print(f'n2=>{n2}')
    
# print("나의 계산기")
# while True:
#     print("1.게임")
#     print("2.빙고")
#     print("3.종료")
#     select=input("메뉴를 선택하세요")
#     if select == "3":

#         break