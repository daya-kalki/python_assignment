import random
lower_bound = int(input("Enter the lower limit:")) 
upper_bound = int(input("Enter the upper limit:")) 
dif= upper_bound - lower_bound
random_nums=[]
if dif<10:
    print("Entered limit not valid!!")

else:
    for i in range(10):
        random_num = [random.randint(lower_bound, upper_bound)]
        random_nums.append(random_num)

print(random_nums)
