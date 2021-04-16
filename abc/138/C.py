N = int(input())
v = list(map(int, input().split()))

v.sort()

l = len(v)

while l > 1:
  v[:2] = [(v[0] + v[1]) / 2]
  l -= 1
print(v[0])
