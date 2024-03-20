num=int(input("Enter any number:"))
if (num>1):
    for i in range (2,(num//2)+1):
        if(num%2==0):
            print(num,"is Not a Prime Number")
            break;
    else:
        print(num,"is a Prime Number")
else:
    print(num,"is a Prime Number")
    
        
