import math

a, b = input().split()

ans = 'No'
if float.is_integer(math.sqrt(int(a + b))) == True:
  ans = 'Yes'

print(ans)
