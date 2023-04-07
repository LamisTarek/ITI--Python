# 2 - Write a function that accepts two arguments (length, start) to generate
# an array of a specific length filled with integer numbers increased by one
# from start.

def generate_array(length, start):
    arr = []
    for i in range(length):
        arr.append(start+i)
    return arr

my_arr = generate_array(5,20)
print(my_arr)
