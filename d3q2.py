s = input("Enter a string: ")
words = s.split()
if len(words) == 0:
    print("Output: 0")
else:
    last_word = words[-1]
    print("Output:", len(last_word))
