# Frequency of Characters in a String
# Write a program to count the frequency
# of each character in a given string using Dict.

#string = "automation"
# {a:2, u:1, t:2, o:2, m:1, i:1, n:1}

string = input("enter string")

#Logic building
# I/P - string e.g automation
# O/P -> dict  # {a : 2, u : 1 , t : 2 , o : 2, m : 1, i : 1, n : 1}
char_count = {}

for char in string:
    char_count[char] = char_count.get(char, 0) + 1 #dict.get(key, default) -
                                                   # Return the value for key
                                                  # if key is in the dictionary,
                                                  # else default (here default value is 0)

print(char_count)