my_arr=[2,33,21,4,6,88,7,3,3]
n=len(my_arr)
for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if my_arr[j]<my_arr[min_index]:
            min_index=j
    my_arr[i],my_arr[min_index]=my_arr[min_index],my_arr[i]
print(my_arr)
