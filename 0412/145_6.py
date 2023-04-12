'''
2023-04-12
남태호
#문제분석
    변수-정수1(num1),정수2(num2)
#알고리즘
    1.변수선언
        -num1,num2에 정수 입력
    2.논리(선택 if~elif~else)
        if num1%2==0 and num2%2==0:
            print("{}+{}={}".format(num1,num2,num1+num2))
        elif num1%2==1 and num2%2==0:
            print("첫 번째 정수를 짝수로 입력하세요.")
        elif num1%2==0 and num2%2==1:
            print("두 번째 정수를 짝수로 입력하세요.")
        else: 
            print("두 숫자 모두를 짝수로 입렵하세요.")
'''

num1=int(input("첫 번째 정수를 입력하세요 :")) #정수 입력
num2=int(input("두 번째 정수를 입력하세요 :")) #정수 입력

if num1%2==0 and num2%2==0:
    print("{}+{}={}".format(num1,num2,num1+num2))
elif num1%2==1 and num2%2==0:
    print("첫 번째 정수를 짝수로 입력하세요.")
elif num1%2==0 and num2%2==1:
    print("두 번째 정수를 짝수로 입력하세요.")
else:
    print("두 숫자 모두를 짝수로 입렵하세요.")
