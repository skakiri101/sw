'''
2023-05-07
남태호
10개의 숫자를 입력받아 0보다 큰 수에 대해서만 전체 합과 평균을 출력하는 프로그램(while 반복문 이용)
1. 조건 추출
    0보다 큰 10개의 숫자
2.연계된 논리 결정
    while i <= 10:
3.논리구조도
    i=1 #초기화
    sum=0 #합계 초기화
    y=10 #양수 개수 초기화

    while i <= 10:
        num=int(input("합계 구할 숫자 입력 : "))
        if num > 0:
            sum+=num
            i+=1
        else:
            y-=1
            i+=1

    if y > 0:
        avg=sum/y
        print("0보다 큰 수의 합계 :", sum)
        print("0보다 큰 수의 평균:", avg)
    else:
        print("입력받은 숫자 중 0보다 큰 수가 없습니다.")
'''

i=1 #초기화
sum=0 #합계 초기화
y=10 #양수 개수 초기화

while i <= 10:
    num=int(input("합계 구할 숫자 입력 : "))
    if num > 0:
        sum+=num
        i+=1
    else:
        y-=1
        i+=1

if y > 0:
    avg=sum/y
    print("0보다 큰 수의 합계 :", sum)
    print("0보다 큰 수의 평균:", avg)
else:
    print("입력받은 숫자 중 0보다 큰 수가 없습니다.")
