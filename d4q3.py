def remove_duplicates(lst):
    return list(set(lst))
n = int(input("Enter the number of elements in list: "))
lst = []
for i in range(n):
    elem = int(input(f"Enter element{i+1}: "))
    lst.append(elem)
new_lst = remove_duplicates(lst)
print("Non-duplicate items:", new_lst)
