#list 자료형으로 코드 작성하기

#실습1) 입력받은 데이터를 저장후 최댓값, 최소값 찾아서 출력하기
#조건) 숫자 5개 입력 받음 , input() 1번만 사용
# 생각 1 : input() 내장함수 사용
# 생각 2 : 타입이 전부 str타입 => int타입으로 형변환
# 생각 3 : 하나의 str로 숫자 문자열 => 문자열 나누기 split()
# 생각 4 : 내장함수 => len():요소 수, max():최대값, min():최소값

#1.입력받기
nums=input("숫자 5개 입력: (예:5, 7, 3, 1, 8)")
print(nums)
#2.데이터 쪼개기 및 확인
nums=nums.split(",") # 타입 = List
print(type(nums))
#3.데이터 공백제거 및 타입변환
print(type(nums[0])) # 타입 = str
# nums[0].strip()
# nums[0]=nums[0].strip()
# nums[0]=int(nums[0])
nums[0]=int(nums[0].strip())
nums[1]=int(nums[1].strip())
nums[2]=int(nums[2].strip())
nums[3]=int(nums[3].strip())
nums[4]=int(nums[4].strip())


print(type(nums[0]))

#4.리스트 요소 중 가장 큰 수치, 가장 작은 수치 출력
#내장함수 => max(), min()
firstvalue=max(nums) # 한 값중 최대값은 오류, 리스트값중 최댓값.
lastvalue=min(nums)
print(f"리스트 nums의 최댓값 : {firstvalue}, 최소값:{lastvalue}")




