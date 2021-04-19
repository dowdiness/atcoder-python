N = int(input())
s = []
for i in range(N):
  s.append(int(input()))

s.sort()

# 一番小さな10で割れない数を求める
odd = 99
for i in s:
  if i % 10 != 0 and odd > i:
    odd = i

orisum = sum(s)

while sum(s) % 10 == 0:
  if len(s) > 0:
    s.pop(0)
  else:
    break

ans = sum(s)
if orisum - odd > ans and ans != 0:
  ans = orisum - odd

print(ans)
