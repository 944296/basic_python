#메모리와 변수
#메모리 : 데이터를 저장하는 공간
#변  수 : 데이터가 저장된 메모리 주소를 가지고 있음
#      => 참조하고 있음
#      => 주소로 메모리를 찾아가서 데이터를 읽기/변경
#----------------------------------------------------
name = "Hong"
age = 20

# 여러개 변수에 한꺼번에 데이터 저장하는 방법

# 언패킹
name, age = ("마징가", 20)
print(f"name => {name} | {type(name)} , age => {age} | {type(age)} ")

data1=("원더우먼","히어로")
data2="원더우먼","히어로"                                                
print(f"data1 => {data1} | {type(data1)} ")
print(f"data2 => {data2} | {type(data2)} ")
print(data1[0],data2[0])

kor, eng = 99, 88
print(kor, eng)
print(type(kor))
kor, eng, math, art = [99, 88, 100, 81]
print(type(kor))                                                 


#data3=[1,2,3] #리스트
#data4=1,2,3   #튜플
#kor, eng, math, art = [99, 88, "A", 81]  #각각


#변수와 복사-----------------------------------------------------------------------------------
year = 2022
data = year

nums=[["A"],1,2,3]
back=nums
nums_copy=nums.copy()                                                   #얕은복사: 리스트안에 리스트는 카피해도 중복됨.

print("nums[0]=", nums[0], "nums_copy[0]=", nums_copy[0])
print("id(nums)=", id(nums), "id(nums_copy)=", id(nums_copy))

nums[0][0]=11

print("nums[0]=", nums[0], "nums_copy[0]=", nums_copy[0])
print("id(nums)=", id(nums), "id(nums_copy)=", id(nums_copy))  

nums[:]

a=3
b=5
a,b=b,a
print(a,b)