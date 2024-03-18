num=int(input("Enter any number:"))
rev_num=0
org_num=num
while(num>0):
    rev_num= rev_num*10 + num%10
    num=num//10
if(org_num==rev_num):
    print("Entered number is a PALINDROME")
else:
    print("Enterd number is NOT a Palindome")
