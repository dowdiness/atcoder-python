N, T = map(int, input().split())
t = list(map(int, input().split()))

summery = []

for i, num in enumerate(t):
  if i == 0:
    summery.append(0)
  elif num - t[i - 1] > T:
    summery.append(T)
  else:
    summery.append(num - t[i - 1])

ans = sum(summery) + T
print(ans)
