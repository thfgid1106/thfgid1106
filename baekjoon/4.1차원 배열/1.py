N = int(input())
score = list(map(int, input().split()))

for i in range(N):
    score[i] = score[i]/max(score) * 100
print(score)