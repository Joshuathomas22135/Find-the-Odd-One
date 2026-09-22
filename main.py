# A Python program that uses XOR to find the one number that appears only once in a list while all matching pairs cancel out.

list = [2,1,8,8,2]

result = 0

for i in list:  
    result ^= i

print(f"List: {list}")

print(f"Odd Occurring: {result}")