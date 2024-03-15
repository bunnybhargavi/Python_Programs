n=int(input("Enter the number of terms :"))
t1=0
t2=1
nextterm=t1+t2
print("Fibonacci Series is :",t1,"\n",t2)
for i in range(1,n+1):
    print(nextterm)
    t1=t2
    t2=nextterm
    nextterm=t1+t2
    
