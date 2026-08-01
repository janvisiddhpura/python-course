# a function that takes a string and returns the count of vowels and consonants separately.

def count_vowels(user_input):
    # defined vowels
    vowels = "aeiouAEIOU"

    count_vowel = 0
    count_consonant = 0

    for each_char in user_input:
        if each_char.isalpha():
            if each_char in vowels:
                count_vowel += 1
            else:
                count_consonant += 1

    return count_vowel, count_consonant

vowels, consonants = count_vowels("Alex Wilson")
print(vowels,consonants)