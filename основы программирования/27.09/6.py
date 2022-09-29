def factorial(n):
    end = 1
    for i in range(1, n + 1):
        end *= i
    return end
print(factorial(int(input('n: '))))
