N = int(input())
bag = 0

while N >= 0:
    if N % 5 == 0:
        bag += N//5
        print(bag)
        break
    N -= 3  #3키로 봉지의 최솟값을 올려주면서 5키로 봉지의 값을 찾아감.
    bag += 1
else:
    print(-1)


#18    4
# 4   -1
# 6    2
# 9    3
#11    3
