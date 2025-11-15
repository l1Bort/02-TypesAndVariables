###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
number_of_letters = max(0, abs(last_letter_code - first_letter_code - 1))
print(f'Between {first} and {last} is {number_of_letters} letters')

# Liczy to odstęp między literami jężeli A jest 65 a B jest 66 to między nimi nie ma żadnej litery więc wynik to 0 dlatego odejmujemy 1d