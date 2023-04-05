def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
    return True

m = int(input("Enter lower interval: "))
n = int(input("Enter upper interval: "))

print("Prime numbers between", m, "and", n, "are:")
for i in range(m, n+1):
    if is_prime(i):
        print(i, end=" ")

print("\nEven numbers between", m, "and", n, "are:")
for i in range(m, n+1):
    if i % 2 == 0:
        print(i, end=" ")
