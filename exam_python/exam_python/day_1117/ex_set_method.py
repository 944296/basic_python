# set 자료형 메서드
#-----------------------------------------------
#아래 문자열에서 중복 알파벳은 제거 후 저장하기
msg= "Merrychristmas Happy new year"
msg=msg.replace(" ","")
print(msg)

data= set(msg)
print(data)

# set 자료형에 요소 추가 메서드 => set.add(요소)
data.add("Q") # str
print(data) 
print(list("Hab")) # 리스트로 만들어줌..
#print(data.add(["Hab"])) # add매서드는 하나만 넣을수있음, 리스트형 불가능

# set 자료형에 여러개의 요소 추가 메서드 => set.update(요소)
data.update(["A","Hab","Happy"])
print(data)

nums={1,4,2,3}
nums.add(1) # int
nums.update([5,3,6,6,6,6,6,6,6,2])
print(nums)

#요소 제거하는 메서드 => set.remove(요소)
nums.remove(4)
print(nums)
#nums.remove(7)
#print(nums)

#요소를 꺼내는 메서드 = > set.pop() 
num=nums.pop() #랜덤으로 추출
print(num)

#---------------------------------------------------------
#멤버 연산자
# A in B     => A가 B에 존재하면 True/없으면 False
# A not in B => A가 B에 존재하면 False/ 없으면 True

print(f" 3 in [1,2,3] => { 3 in [1,2,3] }")
print(f" 7 in [1,2,3] => { 7 in [1,2,3] }") 


print(f" H in 'Hello' => { 'H' in 'Hello' }")
print(f" b in 'Hello' => { 'b' in 'Hello' }")

print(f" A in { {'A':10, 'B':30} } => { 'A' in {'A':10, 'B':30} } ")
print(f" 10 in { {'A':10, 'B':30} } => { 10 in {'A':10, 'B':30} } ")

