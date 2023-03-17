n = int(input())
line = n * 2 - 1
star = '*'
space = ' '
for i in range(n, 0, -1):
    if i == n:	## 첫번째 줄은 항상 별이 하나
        print(space * (line//2), end = '')
        print(star)
    elif i == 1:	## 마지막 줄은 항상 별이 line개
        print(star*line)
    else:	## 나머지
        print(space * (i - 1) + star, end = '' )
        print(space * (line - i * 2) + star)