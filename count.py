evenCount = 0
oddCount = 0
while True:
    number = int(input("Enter number "))
    if (number == 0): break
    if number % 2: evenCount += 1 
    else: oddCount += 1 

print(f"Even numbers count is {evenCount}\nOdd numbers count is {oddCount}")