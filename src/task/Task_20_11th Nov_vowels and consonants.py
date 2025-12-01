# Count vowels and consonants in a String

input_string = "hello, world!"
# a,e, i,o,u - vowels
# h, l, w, r, d - consonants
# vowel ?
#consonent ?

vowel_list = ["a", "e", "i", "o", "u"]
vowel_counter = 0
consonant_counter = 0
result_Vowels = list()
result_Consonants = list()

for char in input_string.lower(): # convert to lowercase
  if char.isalpha():         # process only letters (a–z)
    if char in vowel_list:
        vowel_counter = vowel_counter + 1
        result_Vowels.append(char)
    else:
        consonant_counter = consonant_counter + 1
        result_Consonants.append(char)

print(result_Vowels)
print(vowel_counter)
print(result_Consonants)
print(consonant_counter)

