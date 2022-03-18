N = int(input())
Origin_N = N
count = 0
while True:
    a = Origin_N//10    #10의 자리수
    b = Origin_N%10     #1의 자리수
    c = (a+b)%10   #a+b의 1의 자리수
    
    new_N = b*10 + c
    count += 1
    if N == new_N:
        break
    else:
        Origin_N = new_N
print(count)