#Author: Krishaay J
#Date Written: 18 January 2019
word = input("Enter Word: ")
if(str(word) == str(word)[::-1]):
    print("Word is a palindrome")
else:
    print("Word is not a palindrome")
