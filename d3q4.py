g=input("Enter a string: ")
v=input("Enter a charecter to be deleted: ")
def delchar(s, c):
    if len(c) != 1:
        return s
    result = ""
    for char in s:
        if char != c:
            result += char
    return result
r=delchar(g, v)
print(r)
