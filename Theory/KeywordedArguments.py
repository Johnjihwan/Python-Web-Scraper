def plus(a,b):
    return a-b;

result = plus(b=30,a=1)
print(result)
#plus 인자의 위치에 관계없이 이름에 따라 결정됨.

def say_hello(name, age, are_from, fav_food):
    return f"Hello {name} you are {age} you are from {are_from} you like {fav_food}"

hello = say_hello("jihwan", "17", "korea", "kimchi")
print(hello)
#formating: return f"sentence{string}";