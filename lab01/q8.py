# 8 - Write a program that prints the number of times the string 'iti' occurs in

def count_iti(str):
    count = str.lower().count("iti")
    print("iti appeared :", count)

my_str= input("Please Enter ur sentence: ")
count_iti(my_str)