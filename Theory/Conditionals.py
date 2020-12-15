def plus(a,b):
    if type(b) is int or type(b) is float:
        return a+b
    else:
        return None

print(plus(12,1.2))

# type(형)이 int or float 이면 a+b
# def 선언에 if 문을 넣어 condition 한다. 
# print 해줘야 할 것 실수 하지 않기!
 