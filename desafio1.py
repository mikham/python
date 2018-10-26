texto = 'We are having a great time in polisinos. there are very smart students here'
count_vowels = 0
count_consonants = 0
for letras in texto:
    if letras in ['a', 'e', 'i', 'o', 'u']:
        count_vowels += 1
    elif letras not in [' ', '!', '@', '.', ',']:
        count_consonants = count_consonants + 1

print ('The number of vowels in text is:'+ str(count_vowels))




