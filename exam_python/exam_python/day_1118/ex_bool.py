# 논리 자료형 bool type (불)
# - 저장하는 데이터 : True, False
# - bool타입으로 형변환해주는 함수 : bool(데이터)
#---------------------------------------------------
# bool타입 데이터 저장
isrun = False
isok = False

#데이터를 bool타입으로 형태 변환시키기
#숫자데이터 => bool타입으로 변환
#False = 0, True => 나머지 숫자들
isnumber=bool(5)
print(isnumber)

isnumber=bool(-3)
print(isnumber)

isnumber=bool(0)
print(isnumber)


isnumber=bool(0.1)
print(isnumber)

isnumber=bool(1.23)
print(isnumber)

isnumber=bool(0.0)
print(isnumber)

#문자열 str => bool 형변환
#True => 공백문자라도 있으면 True
#False => 아무것도 없는것 '' ""
ismessage=bool(" ")
print(ismessage)

ismessage=bool("한글")
print(ismessage)


ismessage=bool("")
print(ismessage)

#List/Tuple => bool 형변환
#True => 요소가 1개라도 있는 경우
#False => 요소가 하나도 없는 경우
nums=[]
datas=()
print(bool(nums), bool(datas))
print(bool([1]), bool((1)))

#dict/set => bool 형변환
#True => 요소가 1개라도 있는 경우
#False => 요소가 하나도 없는 경우
print(bool({}), bool(set()))
print(bool({"a":10}), bool({1}))



