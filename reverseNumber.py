def reverseNumbers(num):
    outputNum = 0
    while num != 0: # 1234, 123, 12, 1, 0
        lastDigit = num % 10 # 4, 3, 2, 1
        outputNum = (outputNum * 10) + lastDigit # 4, 43, 432, 4321
        num //= 10
    return outputNum # 4321

# 1 - 2 - 3 - 4 (number)
# 4 - 3 - 2 - 1 (reversedNumber)

num = int(input("Enter number "))
result = reverseNumbers(num)
print(f"Reversed number is {result}")
