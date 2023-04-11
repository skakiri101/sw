'''
2023-04-11
남태호
사칙연산
'''

num1=int(input('정수1: ')) #정수1 입력
num2=int(input('정수2: ')) #정수2 입력
op=input('연산자: ') #연산자 입력

if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
else:
    print(num1/num2)