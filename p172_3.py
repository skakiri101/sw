'''
2023-05-07
남태호
3의 배수의 총합이 입력된 숫자를 넘었을 때의 N값과 총합계, N 값이 몇 번째인지를 구하는 프로그램(while 반복문 이용)
1. 조건 추출
    입력받은 숫자가 3의 배수보다 작을 때 반복문 중단
2.연계된 논리 결정
    while i<=num:
3.논리구조도
    num=int(input("사용자 입력 : "))
    i=0 #배수 초기화
    sum=0 #합계 초기화
    repeat=0 #반복 횟구 초기화

    while True:
    i+=3
    sum+=i
    repeat+=1
    if sum>num:
        break

print("{}을 넘었을 때의 값 : {}".format(num,i))
print("{}을 넘었을 때까지의 총합계 : {}".format(num,sum))
print("{}을 넘었을 때까지 몇 번째 3의 배수인가 : {}".format(num,repeat))
'''

num=int(input("사용자 입력 : "))
i=0 #배수 초기화
sum=0 #합계 초기화
repeat=0 #반복 횟구 초기화

while True:
    i+=3
    sum+=i
    repeat+=1
    if sum>num:
        break

print("{}을 넘었을 때의 값 : {}".format(num,i))
print("{}을 넘었을 때까지의 총합계 : {}".format(num,sum))
print("{}을 넘었을 때까지 몇 번째 3의 배수인가 : {}".format(num,repeat))