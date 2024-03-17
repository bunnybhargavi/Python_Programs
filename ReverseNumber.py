num=int(input("Enter any number:"))
rev_num=0
while(num>0):
    rev_num= rev_num*10 + num%10
    num=num//10
print("Reverse of the given number is ",rev_num)
