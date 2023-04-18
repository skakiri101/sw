'''
2023-04-18
남태호
3장 연습문제 7번
두 정수 입력 x>y-x//y, x<y->x+y, x==y->x*y
단,나눗셈 몫 계산할 때 y는 0 안됨
#문제분석
    1.변수-num1(x),num2(y)
    2.수식 num1>num2, num1==num2, num1<num2
#알고리즘
    1.변수선언
        num1,num2 정수 입력
    2.논리(선택)
        if num1>num2:
            if num1==0:
                print("0으로 나눌 수 없습니다.")
            else:
                print(num1/num2)
        elif num1<num2:
            print(num1+num2)
        elif num1==num2:
            print(num1*num2)
        else:
            print("에러")
'''

num1=int(input("x의 값을 입력해주세요 : ")) #정수1로 입력
num2=int(input("y의 값을 입력해주세요 : ")) #정수2로 입력

if num1>num2:
    if num2==0:
        print("0으로 나눌 수 없습니다.")
    else:
        print("{}//{}={}".format(num1,num2,num1//num2))
elif num1<num2:
    print("{}+{}={}".format(num1,num2,num1+num2))
elif num1==num2:
    print("{}*{}={}".format(num1,num2,num1*num2))
else:
    print("에러")

 