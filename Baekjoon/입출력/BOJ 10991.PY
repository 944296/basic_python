n = int(input())
star = '* '	## 별-공백
space = ' '
for i in range(n,0,-1):
    print(space * (i - 1), end='')
    print(star * (n - (i - 1)))
