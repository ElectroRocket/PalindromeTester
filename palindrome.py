word = input("Enter Word: ")
if(str(word) == str(word)[::-1]):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
