# for 반복문 다루기
nums=[11,22,33,44,55,66,77,88,99]

#1부터 10000까지 => range()
bignums=range(10001) # 0 ~ 10000
bignums=range(1,10001) # 1 ~ 10000
print(type(bignums), bignums, bignums[0], bignums[-1])
print(bignums[:3])


#리스트, 튜플, 딕셔너리, 집합, 문자열 => 갯수파악 len()
#요소 갯수 = > 인덱스범위 0 ~ 요소갯수-1
#인덱스 범위: range(0,len(nums))  0 <= ~ < len(nums)

#짝수 인덱스 요소만 출력해주세요----------------------------------
#방법1
for idx in range(0,len(nums)):
    if not idx%2: # 0 이라면 False(인덱스가 짝수인것만 출력)
        print(nums[idx])

#방법2
for idx in range(0, len(nums),2):
    print(nums[idx])

#2의배수 출력---------------------------------------------------
# for i in range(0,11):
#     print(f"2*{i}={2*i}")

# for i in range(0,11):
#     print(f"3*{i}={3*i}")

# for i in range(0,11):
#     print(f"4*{i}={4*i}")

#2단 ~ 9단 구구단 출력-------------------------------------------------
for dan in range(2,10): #2 ~ 9
    print(f"----{dan}단-----")

    for num in range(1,10): #1~ 9
        print(f'{dan}*{num}={dan*num:2}') #예쁘게 찍기

#숫자문자열을 정수로 형변환하기-----------------------------------------
nums=["1",'3','8','10','2','5','9']
#ums[0]= int(nums[0]) #문자열 -> int 형변환

for idx in range(len(nums)): #인덱스 구하기
    nums[idx]=int(nums[idx])
print(nums)





