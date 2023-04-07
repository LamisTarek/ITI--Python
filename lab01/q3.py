# 3 - Fill an array of 5 elements from the user, Sort it in descending and
# ascending orders then display the output

def sort_arr(n):
    arr= []
    for i in range(n):
        element=int(input("Enter elemnet {}:".format(i+1, n)))
        arr.append(element)
    return arr

my_arr=sort_arr(5)
print("Array: ",my_arr)
print("Ascending Array", sorted(my_arr))
print("Descending Array", sorted(my_arr, reverse= True))



