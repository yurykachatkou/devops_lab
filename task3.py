x, y = map(int, input().split())
# Find different bits
z = x ^ y
# Count the number of different bits
bits = 0
# Add result of AND operation between z and 1. Then shifting bits.
while z > 0:
    bits += z & 1
    z >>= 1

print(bits)
