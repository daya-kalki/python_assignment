a = input("Enter binary number a: ")
b = input("Enter binary number b: ")
c = input("Enter binary number c: ")
a = int(a, 2)
b = int(b, 2)
c = int(c, 2)
max_num = max(a, b, c)
max_bin = bin(max_num)[2:]
print("The greatest binary number is:", max_bin)
