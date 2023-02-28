# # variables
# a = 2  # 0x0001
# b = 3  # 0x0002
# c = a + b  # 0x0003
# print(c)

# # data type: number, "text", boolean(True, False)
# my_name = "nick"
# age = 12
# dead = False
# print("Hello my name is", my_name, "and i am", age)

# # function
# def say_hello():
#     print("Hello how r u?")

# say_hello()
# print("hello world")

# # parameters(arguments): function안에서만 쓸 수 있는 variable
# def say_hello(user_name):
#     print("hello", user_name)

# say_hello("nick")
# say_hello("lyn")

# # multiple parameters
# def say_hello(user_name, user_age):
#     print("name is", user_name, "age is", user_age)

# say_hello("nick", 12)
# say_hello("lyn", 21)

# # Default parameter(argument)
# def say_hello(user_name="anonymous"):
#     print("Hello", user_name)

# say_hello("nick")
# say_hello() #에러가 아닌 기본값 출력

# # return: 함수의 바깥으로 값을 보낼 수 있게...
# def tax_calc(money):
#     return money * 0.35


# def pay_tax(tax):
#     print("thanks you for paying", tax)

# # == pay_tax(tax_calc(15000000000))
# to_pay = tax_calc(15000000000)
# pay_tax(to_pay)

# # 문자열안에 변수넣기
# my_name = "nick"
# my_age = 12
# my_color_eyes = "brown"
# print(f"I'm {my_name}, my age is {my_age}, my eyes color is {my_color_eyes}")

# input 함수/ type 함수
age = input("How old are you?")
print("user answer", age)
