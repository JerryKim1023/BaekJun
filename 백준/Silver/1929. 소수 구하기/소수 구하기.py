M,N = input().split()

def new_check(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True        


for i in range(int(M),int(N)+1):
    if new_check(i) == True:
        print(i)
    