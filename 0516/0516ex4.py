'''
2023-05-16
남태호
파일 입출력 -seek(0):파일의 처음으로 포인트 이동
            read(int n):지정된 갯수만큼 파일 읽어 오기
'''

f=open("C:/data/test.txt","r") #파일 객체 생성(읽기)

print(f.read(10),end='') #파일에서 10개의 문자 읽어서 출력(포인터가 이동)
print(f.read(10),end='')
print(f.read(10))

f.seek(0) #파일의 처음으로 포인터 이동

print(f.read(10),end='')
print(f.read(10),end='')
print(f.read(10))

f.close() #파일 종료