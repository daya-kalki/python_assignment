def interleave(s1, s2):
    result = ""
    for i in range(max(len(s1), len(s2))):
        if i < len(s1):
            result += s1[i]
        if i < len(s2):
            result += s2[i]
    return result

def count_vowels(s3):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s3:
        if char in vowels:
            count += 1
    return count

s1 = input("S1: ")
s2 = input("S2: ")
s3 = interleave(s1, s2)
vowel_count = count_vowels(s3)

print(s3)
print("Number of vowels in s3:", vowel_count)
