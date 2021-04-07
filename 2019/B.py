import math
import sys

N = int(input())

if N == math.floor(N * 1.08):
  print(N)
  sys.exit(0)

for x in range(math.floor(N * 0.9), N):
  if math.floor(x * 1.08) == N:
    print(math.floor(x))
    break
  if x == N - 1:
    print(':(')
