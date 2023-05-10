'''
2023-05-10
남태호
'''
num=int(input("사용자 입력 : "))
sum=0 #합계
cnt=0 #3의 배수의 갯수
i=0

while True:
    i=i+3
    sum=sum+i
    cnt=cnt+i
    if sum>num:
        break

print("{}을 넘었을 때 숫자:{}".format(num,i))
print("{}을 넘었을 때 까지의 합계:{}".format(num,sum))
print("{}을 넘었을 때 까지 몇 번째 3의 배수인가:{}".format(num,cnt))