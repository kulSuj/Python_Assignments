#Program to reverse a string input from user.

print "This program will reverse and print the string input by the user"
print "*"*20


user_string=raw_input("Enter a string: ")


if (user_string == ""):
  print "No input from user"
  exit(0)


reversed_string = user_string[::-1]

print ""
print "*"*10 + "Reversed String"  + "*"*10
print reversed_string


#Verifying if a string is a palindrome, any extra spaces in the string are removed.
if (user_string.replace(" ", "") == reversed_string.replace(" ", "")):
    print ""
    print "*"*10 + "It's a PALINDROME" + "*"*10
