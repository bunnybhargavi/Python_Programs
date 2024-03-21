def _sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return(sum)
len=int(input("Enter the length of the array:"))
arr=[]
for i in range(0,len):
    ele=int(input("enter elements:"))
    arr.append(ele)
sum=_sum(arr)
print("Sum of Array elemants :",sum)
