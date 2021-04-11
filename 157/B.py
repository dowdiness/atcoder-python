a = []
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))

aa = sum(a, [])

b = []
n = int(input())

for _ in range(n):
  b.append(int(input()))

ans = 'No'

for t in b:
  for i, j in enumerate(aa):
    if j == t:
      aa[i] = True

for n in range(3):
  if aa[n] == True and aa[3+n] == True and aa[6+n] == True:
    ans = 'Yes'
  elif aa[n*3] == True and aa[n*3+1] == True and aa[n*3+2] == True:
    ans = 'Yes'

if aa[0] == True and aa[4] == True and aa[8] == True:
  ans = 'Yes'
elif aa[2] == True and aa[4] == True and aa[6] == True:
  ans = 'Yes'

print(ans)
