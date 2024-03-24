n=int(input("Enter the number of elements in the array:"))
arr={}
for i in range(0,n):
    arr[i]=int(input("Elements of the array:"))
print("Elements of the array in even position:")
for i in range (1,n,2):
    print(arr[i])
