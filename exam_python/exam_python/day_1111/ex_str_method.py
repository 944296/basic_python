#매서드(Method)
#특정 클래스에서만 사용되는 함수
#사용 : 객체생성후 사용 가능 
#예시 : name= "hong"
#       name.메서드명()
#       name.속성명
#------------------------------------
msg = "Merri Christmas"

# "i" -> "y" 로 변경-----------------
# 방법1 : 인덱스로 변경 => 변경 불가
#msg[4] = "y"
#print(msg)

#방법2 : str타입의 전용 메서드 => replace(바꿀문자열,새로운문자열)
msg.replace("i","y")
print(msg)
#변경된 문자열은 다시 저장해야함!
msg=msg.replace("i","y")
print(msg)

#문자열에서 인덱스 찾아주는 메서드
# find(문자열) => 양수 인덱스  / 없는 경우 : -1
# index(문자열) => 양수 인덱스 / 없는 경우 : Error
print(f'{msg} => c인덱스 : {msg.find("C")}')
print(f'{msg} => c인덱스 : {msg.find("c")}')
#여러개 문자가 모인 경우에는 문자가 시작되는 인덱스 반환
print(f'{msg} => mas인덱스 : {msg.find("mas")}')
#특정문자가 여러개 존재하는 경우 => 제일먼저 발견되는 문자 인덱스
print(f'{msg} => r인덱스 : {msg.find("r")}')
#문자열의 뒤에서부터 인덱스를 찾는 경우 : rfind()메서드
print(f'{msg} => r인덱스 : {msg.rfind("r")}')

#index() 메서드로 문자의 인덱스 찾기
print(f'{msg} => c인덱스 : {msg.index("C")}')
#print(f'{msg} => c인덱스 : {msg.index("c")}')

#문자열에서 특정 문자열이 몇개잇는지 알려주는 메서드 => count()
data = "Happy Happy"
print(data.count("p"))
pcount=data.count("p")

#data문자열에서 "p"가 존재하는 갯수만큼 data를 화면에 출력해주세요.
print(data*pcount)
print(pcount)


#대소문자 변경해주는 메서드
#소문자 => 대문자로 변경 upper()
#대문자 => 소문자로 변경 lower()
print(data.upper(), data.lower())
print(data)

#앞부분/뒷부분 공백 제거하는 메서드
#strip() : 앞/뒤 공백 제거
#lnstrip() : 앞부분 공백만 제거
#rstrip() :뒷부분 공백만 제거

data1=" Happy Happy "

#내장함수 => len(변수명) => 갯수/길이를 리턴
print(f"{data1} 길이 : { len(data1) }")
data2= data1.strip()
print(f'{data2}의 길이 : {len(data2)}')
data3= data1.lstrip()
print(f'{data3}의 길이 : {len(data3)}')
data4= data1.rstrip()
print(f'{data4}의 길이 : {len(data4)}')

#문자열 쪼개기, 특정 문자를 기준으로 쪼개기 => split()
# 기본: 공백을 기준으로 문자열 나누기
data = "Happy New Year 2023"
datas=data.split()
print(datas)

data= data.replace(" ","*")
print(data)

datas=data.split("*")
print(datas)

#실습--------------------------------------
num= "010-1234-5678"
nums=num.split("-")
print(nums)

date= "2022/11/11"
dates= date.split("/")
print(dates)

#여러개의 문자열 연결하는 매서드 => join()
#형식 : 연결할문자열.join(여러개 문자열)
phone="010-1234-5678"

phone2=phone.split("-")
print(f'phone2: {phone2}')
#나누어진 전화번호 문자열 합치기/연결
new_phone="-".join(phone2)
print(f'new_phone : {new_phone}')

#실습-------------------------------------
#하고싶은말 입력받아서 출력하기

talk = input("하고싶은말 :")
print(type(talk))
print(f'talk의 길이: {len(talk)}')

#입력 받은 데이터 공백 제거하기
talk=talk.strip()
print(talk)

