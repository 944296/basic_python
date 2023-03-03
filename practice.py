from requests import get

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

# # input 함수/ type 함수
# age = input("How old are you?")
# print("user answer", age)

'''
# library
# random 모듈에서 randint 함수를  import해줘
from random import randint

pc_chioce = randint(1, 100)
playing = True

while playing:
    user_choice = int(input("choose number(1-100):"))
    if user_choice == pc_chioce:
        print("you win")
        playing = False
    elif user_choice > pc_chioce:
        print("Lower!")
    elif user_choice < pc_chioce:
        print("higher!")
'''

# data structures
# 1.list[]
days_of_week = ["Mon", "Tue", "Wed", "Thur", "Fri"]
# function vs methods: tring/number등의 데이터에대한 funtion
name = "nick"
print(name.upper())
# list에대한 method
print(days_of_week.count("Wed"))
days_of_week.reverse()
days_of_week.append("Sat")
print(days_of_week)
# 인덱스로 특정 아이템에 접근
print(days_of_week[0])

# 2.tuple(),(불변, immutable)=> method 별로 없음.
days = ("Mon", "Tue", "Wed", "Thur", "Fri")
print(days[-1])

# 3.Dicts{key:value}
player = {
    "name": "nick",
    "age": 12,
    "alive": True,
    "fav_food": ["🍕", "🍔"]
}
print(player.get("age"))
print(player["fav_food"])
print(player)
player.pop("age")
print(player)
player["xp"] = 1500
print(player)
# list에 대한 method사용 가능
player["fav_food"].append("🌭")
print(player["fav_food"])

# for(loop)
websites = ["google.com", "https://twitter.com",
            "facebook.com", "https://tiktok.com"]
results = {}
for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"  # string안에 변수 넣는법
    response = get(website)  # requests module 설치!!!
    if response.status_code == 200:
        results[website] = "ok"
    else:
        results[website] = "failed"
print(results)
