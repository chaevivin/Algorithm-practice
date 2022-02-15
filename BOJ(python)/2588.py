num1 = int(input())
num2 = int(input())

mul3 = num1 * (num2 % 10)
mul4 = num1 * int(((num2 % 100) - (num2 % 10)) / 10)
mul5 = num1 * (int(num2 / 100))

print(mul3)
print(mul4)
print(mul5)
print(mul3 + (mul4 * 10) + (mul5 * 100))
