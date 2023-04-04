def calculate_interest(principal, years, gender, senior_citizen):
    if senior_citizen:
        rate_of_interest = 0.15
    elif gender == 'f':
        rate_of_interest = 0.12
    else:
        rate_of_interest = 0.1

    interest = principal * rate_of_interest * years
    return interest

principal = float(input("Enter the principal amount: "))
years = float(input("Enter the no of years: "))
gender = input("Gender (m/f): ")
senior_citizen = input("Is customer senior citizen (y/n): ")

if senior_citizen.lower() == 'y':
    senior_citizen = True
else:
    senior_citizen = False

interest = calculate_interest(principal, years, gender, senior_citizen)

print("Interest:", interest)
