my_arr=[2,3,4,5,6,775,344,1,45,0]
n=len(my_arr)
for i in range(n-1):
    for j in range(n-i-1):
        if my_arr[j]>my_arr[j+1]:
            my_arr[j],my_arr[j+1]=my_arr[j+1],my_arr[j]
print(my_arr)