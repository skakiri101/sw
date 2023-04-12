'''
2023-04-12
남태호
입력받은 두 수의 크기 비교
#문제분석
    변수-숫자1(num1),숫자2(num2)
#알고리즘
    1.변수 선언
        num1,num2 정수 입력
    2.논리(선택 if~else)
        if num1>num2:
            (참)큰 수 num1, 작은수 num2
        else:
            (거짓)큰 수 num2, 작은수 num1
'''

num1=int(input("첫 번째 숫자:")) #정수 입력
num2=int(input("두 번째 숫자:")) #정수 입력

if num1>num2: #조건
    print("두 수 중 큰 수는 {}, 작은 수는 {}이다.".format(num1,num2)) #num1이 더 클때
else:
    print("두 수 중 큰 수는 {}, 작은 수는 {}이다.".format(num2,num1)) #num2가 더 클때