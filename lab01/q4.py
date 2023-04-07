# 4 - write a function that takes a number as an argument and if the number
# divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# divisible by both return "FizzBuzz"

def check_num(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "bizz"
    
num = int(input("Enter a number: "))
res = check_num(num)
print(res)
    
