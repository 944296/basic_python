#리스트 자료형의 연산 => 덧셈, 곱셈
#덧셈: 리스트 + 리스트만 가능
#곱셈 :리스트 * 정수만 가능

#str타입 보기
msg1="hello~"
msg2="2023"

print(msg1 + msg2)
print(msg1 *5 )

#list타입 보기
nums1=[1,3,5]
datas=["A","B","C"]
etc=[False, 4.7, [11,22]]

print(nums1 + datas)
print(nums1 + etc)
print(nums1 + nums1)

print(nums1 * 3)
print(nums1 * 10)
