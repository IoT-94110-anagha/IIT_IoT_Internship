
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for ch in s.lower():
        if ch in vowels:
            count += 1
    return count



def count_consonants(s):
    vowels = "aeiou"
    count = 0
    for ch in s.lower():
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count



def vowel_consonant_ratio(vowels, consonants):
    if consonants == 0:
        return "Consonants count is zero, ratio not possible"
    return vowels / consonants



string = input("Enter a string: ")

v = count_vowels(string)
c = count_consonants(string)
ratio = vowel_consonant_ratio(v, c)

print("Number of vowels:", v)
print("Number of consonants:", c)
print("Ratio of vowels to consonants:", ratio)
