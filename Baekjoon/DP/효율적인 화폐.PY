n,m=map(int, input().split()) #3, 7
array=[]
for i in range(n):
    array.append(int(input())) #2, 3, 5

d=[10001]*(m+1) 
d[0]=0
for i in range(n):
    for j in range(array[i],m+1):
        if d[j-array[i]] != 10001: 
            d[j]=min(d[j], d[j-array[i]]+1) 
#결과 출력
if d[m] == 10001: #최종적으로 m원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])

