#How to check on a given input, if the first character is a vowel in lowercase letters. See below for uppercase version.

word = input("Enter the word you would like to check: ")

if word[0] in 'aeiou':
    print("The first character is a lowercase vowel!")

elif word[0] in 'AEIOU':
        print("The first character is an uppercase vowel!")
else:
    print("Sorry, but the first character is not a lowercase vowel!")