def say_hello(who):
    print("Hello", who)

say_hello(True)

def plus(a,b):
    print(a+b)

plus(2,5)

def minus(a,b):
    print(a-b)

minus(3,8)

def say_bye(name = "jihwan"):
    print("hello", name)

say_bye() #초기값 부여된 name 을 출력.
say_bye("Kimchi") #두번째로 name에 Kimchi 대입하여 출력.