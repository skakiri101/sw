'''
2023-05-09
남태호
#문제정의
    입력받은 숫자의 팩토리얼 값 계산하기
#문제분석
    변수-정수(num),fac(팩토리얼)
#알고리즘
    1.변수 초기화
        num에 정수 입력
        fac=1
    2.프로그램 논리(반복for)
        for i in range(num,0,-1):
            fac=fac+i
'''

num=int(input("팩토리얼 숫자 입력 : "))

fac=1

for i in range(num,0,-1): #반복조건
    fac=fac*i #팩토리얼 게산

print("%d의 팩토리얼 값은: "%num,fac)