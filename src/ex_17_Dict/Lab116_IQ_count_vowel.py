input_string = "hello, world!"
# a,e, i,o,u.
# vowel ?

vowel_list = ['a', 'e', 'i', 'o', 'u']
vowel_counter = 0
result = list()

for char in input_string:
    if char in vowel_list:
        vowel_counter = vowel_counter + 1
        result.append(char)


print(result)
print(vowel_counter)

