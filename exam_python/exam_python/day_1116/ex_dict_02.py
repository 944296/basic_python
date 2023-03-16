#딕셔너리 dict 데이터 타입
#-----------------------------
#실습) 홍길동, 31, 세일즈맨, 남성
# 데이터에 의미와 함께 저장하세요.

datas = {"name":"홍길동", "age":31, "job":"세일즈맨", "gender":"남성"}

#실습) 성별 데이터를 삭제

del datas["gender"]
print(datas)

#실습) 이름이 마징가 변경

datas["name"] = "마징가"
print(datas)

#실습) 전화번호 010-1111-2222 추가

datas["phone_number"]="010-1111-2222"
print(datas)

#딕셔너리 정렬하기--------------------------------------
#정렬 메서드 없음 => 내장함수 sorted() 사용
datas1=sorted(datas)
print(datas1, max(datas))

