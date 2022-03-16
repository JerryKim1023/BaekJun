N = int(input())
M = list(map(int,input().split()))

scores = []
M.sort(reverse=True)
for i in range(len(M)):
    score = M[i]/M[0]*100
    scores.append(score)


answer = sum(scores)/N

print(answer)