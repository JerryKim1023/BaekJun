n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    average = sum(nums[1:])/nums[0]
    cnt = 0
    for score in nums[1:]:
        if score > average:
            cnt += 1
    rate = cnt/nums[0]*100
    print(f"{rate:.3f}%")
