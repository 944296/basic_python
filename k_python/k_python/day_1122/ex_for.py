#for ~in 반복뭉
#유사하거나 동일한 코드를 줄여서 처리하는 문법
#-----------------------------------------------------------
msg="Merry Christmas 2022"
#    01234 567890123 45678

#for 원소/요소/데이터 in 여러개,인덱스 객체:
for m in msg:
    print(m,end='')
print()

#----------------------------------------------------------
# 내장함수 print(재료) <- 재료 = 매개변수 parameter
print(10,20,30,sep='*',end='\t')
print(10,20,30)

# 1~1000숫자 중에서 7의배수로 구성된 데이터
#데이터의 모든 요소를 출력하고 싶습니다
#단, 한줄에 10개씩 출력하세요

sevens=list(range(7,1001,7))

for idx in range(0, len(sevens)):
    if idx%10==9:
        print(sevens[idx], end='\n')
    else:
        print(sevens[idx], end='\t')

# print('Happy\nnew\nyear')
# print('Happy\tnew\tyear')
# print("Happy") # Happy\n 
# print("Happy","New","year") # Happy New year\n
# print("Happy","New","year",sep="-") # Happy-New-year\n
# print("Happy",end='\t') # Happy\t
# print("Happy",end='\t') # Happy\t     Happy\t
# print("Happy",end='\t') # Happy\t     Happy\t     Happy\t
# print("Happy",end='\t') # Happy\t     Happy\t     Happy\t     Happy\t
print()

sevens=[1,2,3,4,5,6,7,8,9,10]
for num in sevens:
    if num%2==0:
        print(num,end='\n') 
    else:
        print(num, end='\t')
print()

#1~100범위에서 7의배수만 데이터로담기
sevens=list(range(7,101,7))
print(f'7의배수데이터:{len(sevens)}개\n{sevens}')
print("------------------------------------------------")
for m in sevens:
    print(m)
print('------------------------------------------------')
#한줄에 다섯개씩 출력
for m in sevens:
    if m%35: #35로 나눈 값이 True이면(값이 있다면) 띄우기
        print(m, end='  ')
    else: #나머지가 0이면(false이면) 다음줄에 쓰기
        print(m, end="\n")
print()
#sevens의 인덱스 => 갯수 len(sevens)
sevens=list(range(7,101,7))
for idx in range(len(sevens)): 
    if idx%5==4:
        print(sevens[idx], end="\n")
    else:
        print(sevens[idx], end="\t")
        