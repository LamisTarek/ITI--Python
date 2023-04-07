# 1 - Write a program that counts up the number of vowels [a, e, i, o, u] contained in the string
word = input ("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0
for char in word:
    if char.lower() in vowels:
        count+= 1
print("Number of vowels is", count)
