import random
n1=random.random()
n2=random.randint(0,100)
print("Random Integers between 0 and 1:",n1)
print("Random Integer between 0 and 100:",n2)
#creating a list using random numbers
rand_list=[]
for i in range(0,5):
    n=random.randint(1,50)
    rand_list.append(n)
print("List of random integers:",rand_list)
