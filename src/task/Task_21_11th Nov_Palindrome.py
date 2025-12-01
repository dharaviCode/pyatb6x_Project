#Palidrome of String
#Example Walkthrough
#Let’s take the word "level":
#Forward: "level"
#Backward: "level"
#Both are identical → Palindrome ✅
#Now, "hello":
#Forward: "hello"
#Backward: "olleh"
#Not the same → Not a palindrome ❌

input_string = input("Enter a string: ")
reverse_string = input_string[::-1] # [::-1] reverses the string. [start : end : step]

def palindrome(input_string):

     if (input_string == reverse_string):
        return "Palindrome"
     else:
        return "Not Palindrome"


result = palindrome(input_string)
print(result)

###################################################################

text = input("Enter a word: ")

reverse_text = ""  # empty string to store reversed word

# Loop through each character in reverse order
for char in text:
    reverse_text = char + reverse_text

if text == reverse_text:
    print("It is a palindrome!")
else:
    print("It is NOT a palindrome!")


