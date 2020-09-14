def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print("Enter the number:")
x = factorial(int(input()))
print("The factorial is ",x)