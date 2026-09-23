list = [1,2,3,3,2,1,6,5]
xor = 0

for i in list:  
    xor ^= i

rightmostBit = xor&-xor
a = 0
b = 0

for n in list:
    if n & rightmostBit:
        a^=n
    else:
        b^=n

print(a,b)