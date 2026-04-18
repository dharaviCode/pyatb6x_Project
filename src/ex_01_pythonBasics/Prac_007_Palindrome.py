text = input('Enter a string: ')

reverse_text = text[::-1] #this will convert the string to reverse - string slicing
print(reverse_text)
if text == reverse_text :
    print("palindrome")
else:
    print("not palindrome")

input = input('Enter a number: ')
number = str(input)
reverse_number = number[::-1] #String slicing
print(reverse_number)
print(type(reverse_number))
if reverse_number == input:
    print("palindrome")
else:
   print("not palindrome")




