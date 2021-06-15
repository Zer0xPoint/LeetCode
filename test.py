import sys
from collections import Counter

nums = [1, 2, 3, 4]
nums.reverse()
print(nums)

d = dict()
d[1] = 1
print(d)

for i in range(10, 5, -1):
    print(i)

print(0 // 3)
nums[0], nums[1], nums[2], nums[3] = nums[3], nums[2], nums[1], nums[0]
print(nums)

n = 321312
while n > 0:
    print(n % 10)
    n //= 10

print(-sys.maxsize)

print(Counter("aasdgawef"))

print("123123".join("asdasd"))
