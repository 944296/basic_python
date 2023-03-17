a=['SUN','MON','TUE','WED','THU','FRI','SAT']
b=[31,28,31,30,31,30,31,31,30,31,30,31]
x,y=map(int,input().split())
day=0
for i in range(x-1):
    day+=b[i]
day=(day+y)%7 #1일때 월,0일때 일
print(a[day])