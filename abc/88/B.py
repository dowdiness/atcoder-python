N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
alice = 0
bob = 0
for index, card in enumerate(a):
  if (index % 2 == 0):
    alice += card
  else:
    bob += card

print(alice - bob)
