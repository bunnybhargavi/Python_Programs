import math
n=int(input("Enter the number of digits in number:"))
num=int(input("Enter a Number:"))
sum=0
orgnum=num
while(num>0):
    r=num%10
    sum +=pow(r,n)
    num=num//10
if(orgnum==sum):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
    
