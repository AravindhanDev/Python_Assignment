def checkIfAmstrongNumber(num):
    temp = num
    sum = 0
    while num > 0:
        lastDigit = num % 10
        sum = sum + (lastDigit ** 3)
        num //= 10
    return "Amstrong number" if temp == sum else "Not an amstrong number"

num = int(input("Enter number "))
result = checkIfAmstrongNumber(num)
print(result)