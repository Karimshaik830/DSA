my_arr=[1,2,44,55,22,77,555,33,0]
n=len(my_arr)
for i in range(n-1):
    curr_index=i
    curr_element=my_arr[i]
    for j in range(n-i-1,-1,-1):
        if my_arr[j]>curr_element:
            my_arr[j+1]=my_arr[j]
            curr_index=j
        else:
            break
    my_arr[curr_index]=curr_element
print(my_arr)