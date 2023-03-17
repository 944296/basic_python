n=int(input())
nums=list(input().split())
a=[]
for i in range(n):
    a.append(int(nums[i]))
print(min(a),max(a))