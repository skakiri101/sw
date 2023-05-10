'''
2023-05-07
남태호
1부터 100까지의 합을 구하는 프로그램(10을 기준으로 합계를 출력). (while 반복문 이용)
1. 조건 추출
    num%10==0: 일때
2.연계된 논리 결정
    while num<=100:
3.논리구조도
    num = 1  # 시작하는 숫자
    sum = 0  # 합계

    while num<=100:
        sum+=num  
        if num%10==0:
            print("1-{} : {}".format(num,sum))
        num+=1
'''

num = 1  # 시작하는 숫자
sum = 0  # 합계

while num<=100:
    sum+=num  
    if num%10==0:
        print("1-{} : {}".format(num,sum))
    num+=1