#리스트 인덱싱 & 슬라이싱


#실습1) nums=[1,3,5,7,9,11,13,15]
#             0 1 2 3 4 5 6  7
#짝수 요소만 출력
nums=[1,3,5,7,9,11,13,15]
print(nums[::2])
#제일 첫번째, 마지막요소 제외한 나머지 출력
print(nums[1:-1])
#nums=[1,3,"A",15]로 출력
nums[2:7]="A"
print(nums)

#실습2) bools=[False, True, False, False, True, False, False, True]
#True 데이터만 출력
bools=[False, True, False, False, True, False, False, True]
print(bools[1],bools[4],bools[-1])
print(bools[1::3])

#실습3)datas=[[11],2,3,[44,55,[66,77,[88]]],9,10]
# 88 데이터 출력
datas=[[11],2,3,[44,55,[66,77,[88]]],9,10]
print(datas[3][2][2])
# [77, [88]] 데이터 출력
print(datas[3][2][1:])
# [9, 10] 데이터 출력
print(datas[4:])