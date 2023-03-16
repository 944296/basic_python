#for 반복문 - 리스트 컨프리핸션(내포)

#nums리스트의 요소들을 nums2에 담겠습니다.
#단, nums요소들의 값에 3을 곱한 값으로 담아주세요.

nums=[1,2,3]            #단순 list와 for문
nums2=[]

for n in nums:
    nums2.append(n*3)

nums3=[n*3 for n in nums] #리스트 컨프리핸션(for문 한줄로)

print(f'nums2 => {nums2}')
print(f'nums3 => {nums3}')

# list와 for문 if문  --------------------------------------------------------
#nums의 요소값이 짝수인것만  nums2에 3을 곱해서 넣어주세요.

#방법1)
nums=[1,2,3,4,5,6,7]            
nums2=[]

for n in nums:
    if not n%2: #2로 나눈 나머지 값 0(False),1(True)
        nums2.append(n*3)


#방법2) # if문(한줄로)
nums3=[n*3 for n in nums if not n%2 ]  #  for문에서 n을 꺼내서 -> if문에서 참이면 -> n*3 
#      ---/ ------------/ -----------                            if문에서 거짓이면 -> 1번으로 이동
#      3    1            2


print(f'nums2 => {nums2}')
print(f'nums3 => {nums3}')


# list와 for문 if-else문 --------------------------------------------------------
#nums의 요소값이 짝수인것은  nums2에 3을 곱해서 넣어주세요.
#nums의 요소값이 홀수인것은  그대로 리스트에 추가하세요.

#방법1)
nums=[1,2,3,4,5,6,7]            
nums2=[]

for n in nums:
    # if n%2:               # 홀수면(n%2가 1,True이면)
    #     nums2.append(n)   # 그대로 append
    # else:                 # 짝수면
    #     nums2.append(n*3) # n*3 append
    nums2.append( n if n%2 else n*3)


#방법2) # if-else문
nums3=[n if n%2 else n*3 for n in nums]  
#      -----------------/ ------------
#               2              1

print(f'nums2 => {nums2}')


