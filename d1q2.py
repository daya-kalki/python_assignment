grade = input("Enter the Grade: ")
salary = float(input("Enter the Salary: "))

if grade == 'A' or grade == 'a' :
    bonus = 0.05 * salary
elif grade == 'B'or grade == 'b':
    bonus = 0.1 * salary
else:
    print("Invalid grade entered")
    exit()

if salary < 10000:
    bonus += 0.02 * salary

total_salary = salary + bonus
print("Bonus=", bonus)
print("Total salary", total_salary)
