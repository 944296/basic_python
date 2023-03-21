#딕셔너리 데이터 타입 (dict 타입)
#형식 : {키:값, 키2:값, ....., 키N:값}
#인덱스 없음
#키로 값을 찾아냄!
#-------------------------------------
#dict 타입 객체 생성

nums1={}
nums2={"name":'hong', 33:True, "jumsu":[4,5,2]}
nums3={("name","phone"):["kim", "010-111-222"], 1: 12} # 키가 수정되면 안되니까, 키는 튜플형태로
nums4={"datas":{"kor":10, "math":20}}


print(f"nums1=> 타입 {type(nums1)}, 요소 수: {len(nums1)}")
print(f"nums2=> 타입 {type(nums2)}, 요소 수: {len(nums2)}")
print(f"nums3=> 타입 {type(nums3)}, 요소 수: {len(nums3)}")
print(f"nums4=> 타입 {type(nums4)}, 요소 수: {len(nums4)}")

#dict 타입의 요소/원소/데이터 일기
#변수명[키]
print(nums2["name"], type(nums2["name"]))
print(nums2[33],type(nums2[33]))
print(nums2["jumsu"],type(nums2["jumsu"]))
#print(nums2["age"]) => 존재하지 않는 키는 Error
print(nums4["datas"], type(nums4["datas"]))

#nums2에서 데이터 2 출력
values=nums2["jumsu"]
print(values, type(values), len(values), values[-1])

#nums4에서 math데이터 값 출력
values=nums4["datas"]
print(values, type(values), len(values), values["math"])
print(values["math"])
print(nums4["datas"]["math"])

#-------------------------------------------------------
# 새로운 데이터 추가
#-------------------------------------------------------
nums2["age"]=12
print(nums2)

nums2["job"]="student"
print(nums2)

#-------------------------------------------------------
#값 수정/변경/업데이트
#-------------------------------------------------------
nums2["age"]=100
print(nums2)


#-------------------------------------------------------
#값/요소/데이터 삭제
#-------------------------------------------------------
del nums2["name"]
del nums2[33]
print(nums2)

del nums4
print(nums4)
