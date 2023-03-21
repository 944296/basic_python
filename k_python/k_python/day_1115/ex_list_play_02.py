# List 자료형 가지고 놀기
#실습2) 3과목 점수를 입력받고 합계, 평균 계산하여 출력
# 조건) 과목별로 점수 입력받기 => input() 3번 호출
#- 생각1: input() 3번 실행
#- 생각2: 3개 문자열 데이터 생성
#- 생각3: 3개의 문자열 데이터를 하나에 담기 => list
#- 생각4: 아무것도 없는 빈 리스트 준비 => 추가 메서드 append()/insert()
#- 생각5: 숫자 문자열 => 정수로 변환 =>int()
#- 생각6: 합계 => 리스트안에 모든 요소 더하기
#         평균=> 합계/갯수 len()

# #(1) 3과목 입력받기
# kor=input("국어점수:")
# eng=input("영어점수:")
# math=input("수학점수:")
# #(2) str -> int 타입변환
# kor=int(kor)
# eng=int(eng)
# math=int(math)

#(1),(2) 3과목 입력 받고, int타입 변환
kor= int(input("국어:").strip())
eng= int(input("영어:").strip())
math= int(input("수학:").strip())

#(3)정수형태에 3과목을 합계/ 평균
total= kor+eng+math
avg= total/3
#(4) 결과출력
print(f"국어: {kor}, 영어: {eng}, 수학: {math} ,  합계: {total}, 평균: {avg}")

#방법2) list 사용해서 해결하기
#(1) 3과목 점수를 저장할 빈 리스트 변수 선언
jumsu=[]
#(2) 입력 받은 과목 점수를 리스트에 추가 => append()

# value=int(input("국어 :"))
# jumsu.append(value)

#한줄로 표현 가능
jumsu.append(int(input("국어:")))

value=int(input("영어 :"))
jumsu.append(value)

value=int(input("수학 :"))
jumsu.append(value)

print(f" 3과목 점수 => {jumsu}")

#(3) 합계,평균 구하기

total = jumsu[0]+jumsu[1]+jumsu[2]
#내장함수 sum(): 여러개 값의 합계 반환
total=sum(jumsu)
avg = total/len(jumsu)

#(4) 결과 출력
print(f"3과목 합계 : {total}점 \n 평균 : {avg:^10.1}점")