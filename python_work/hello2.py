# function

def sign(num):
  if num > 0:
    return 1
  elif num == 0:
    return 0
#  else:
#    return -1
print sign(10)

pairs = [(1, 10), (2, 20), (3, 30), (4, 40)]
for (low, high) in pairs:
    print low + high

for item in pairs:
    low, high = item
    print low + high
