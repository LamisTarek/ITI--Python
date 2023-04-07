# 5 - Write a function which has an input of a string from user then it will
# return the same string reversed

def string_reverse(str):
    return str[::-1]

my_str = input("Enter a string: ")
res= string_reverse(my_str)
print(res)