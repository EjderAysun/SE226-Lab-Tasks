n = int(input("Enter the value of n: "))
x = int(input("Enter the value of x: "))

factorial = lambda i : 1 if i <= 1 else i * factorial(i-1)
exp = lambda n, i : (n ** i)

result = sum(list(map(lambda i : exp(n, i) / factorial(i), range(1, x + 1)))) + 1

print("Result: %s" %result)