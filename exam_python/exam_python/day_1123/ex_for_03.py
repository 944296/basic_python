#for 반복문 실습
#-------------------------------------------------
#실습) 숫자 1부터 50까지 화면에 세로방향으로 출력
nums=list(range(1,51))
for value in nums:
    print(value)

#range()함수 : 수의 범위를 생성하는 객체------------
#              <class 'range'>
#              range(1, 51)
# 원소/데이터 : 변수명[인덱스]

for num in range(1,51):
    print(num, end=' ')     # 옆으로 출력

#실습) 2 ~ 9단 구구단 출력

dan = input("알고싶은 단 입력:(예 : 2~9) ").strip()    # 공백제거

if len(dan)>0:
    dan=int(dan)    # str타입을 int타입으로 형변환
    for n in range(1,10):
        if n<9:
            print(f'{dan}*{n}={dan*n}', end=' ') # 가로로 출력
        else:           
            print(f'{dan}*{n}={dan*n}')
else:
    print("입력한 데이터가 없습니다.")

    