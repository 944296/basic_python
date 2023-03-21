# 출력함수 print() 사용법
#--------------------------------------------
# 실제 데이터 출력
print(2022)
print("happy")
# 변수명 출력
age=10
msg= "happy new year"
print(age)
print(age, msg, 2023)

#형식의 문자열 출력
#형식지정자 => %알파벳1개
# %d - 정수(decimal)
# %f - 실수 (float)
# %s - 문자열 (string)

a = 12
b = 5
print("a+b=", a+b)
print("a+b=%d"%(a+b))
print("%d+%d=%d" %(a,b,a+b))
print("%d/%d=%d" %(a,b,a/b))
print("%s/%s=%s" %(a,b,a/b))
print("%s" %a)

# F문자열 출력----------
# F" ~ ", f" ~ "
name="hong"
age=12
print(f"이름: {name}, 나이: {age}")





