number = 1

while number <= 10: # {
    print(number)
    number += 1
    # }

# for loops iterate over a collection

name = 'Eric'

# for each item in some collection
for letter in name:
    print(letter)

    # range doesn't include the end value
    # start is optional
for number in range(10): # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    print(number+1)

for number in range(1, 11): # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    print(number)

    # 3rd optional argument is the step by
for even in range(0, 10, 2):
    print(even)

for backwards in range(10, 0, -1):
    print(backwards)

# [ index of ]
print(name[0])

#name[0] = 'e'

for index in range(len(name)):
    print(name[index])

favorite_number = 42

favorite_color = 'blue'

print(name + "'s favorite number is " + str(favorite_number)
      + " and his favorite color is " + favorite_color)

print(f"{name}'s favorite number is {favorite_number} "
      f"and his favorite color is {favorite_color}" )

print(f"4 x 2 is {4*2}")

# [ ] creates a list, which is a collection
destinations = ['Florida', 'California', 'Arizona', 'Antarctica']

print(destinations[1:3])

for destination in destinations:
    print(destination)

print("\n".join(destinations))

print( [ number for number in range(10) if number % 2 == 0 ] )

values = []

for number in range(10):
    if number % 2 == 0:
        values.append(number)
print(values)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(alphabet[4], alphabet[17], alphabet[8], alphabet[2])
# like range, you get the start, but not the end index
print(alphabet[0:3])
print(alphabet[:3])
print(alphabet[22:26])
print(alphabet[22:])
print(alphabet[:])
# optional 3rd argument is the step
print(alphabet[::2])
print(alphabet[1::2])

name = input("Enter your name").upper()

shift = int(input("Enter the number of characters to shift for your cipher"))

result = ""

# find will return the index of the character
for letter in name:
    current_index = alphabet.find(letter)
    new_index = ( current_index + shift ) % 26
    new_letter = alphabet[new_index]
    result += new_letter

print(result)

for letter in name:
    current_value = ord(letter)
    new_value = ( current_value - 65 + shift) % 26 + 65
    new_letter = chr(new_value)
    print(new_letter)

count_of_vowels = 0

for letter in name:
    if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        count_of_vowels += 1

a_count = name.count("A")
e_count = name.count("E")
#i_count

vowels = "AEIOU"

for vowel in vowels:
    count_of_vowels += name.count(vowel)

# umgpt - prompt: write python code to count the number of vowels in a string
# prompt 2: write it in a single line
num_vowels = sum(1 for c in name if c.lower() in "aeiou")
print(num_vowels)

print(name.replace("E","Z"))

phone_number = "800-CALL-SAM"

for letter in "ABC":
    phone_number = phone_number.replace(letter, "2")

for letter in "DEF":
    phone_number = phone_number.replace(letter, "3")

print(phone_number)

print(phone_number.split('-'))

sentence = input("Enter a sentence")

word_count = len(sentence.split(" "))

print(word_count)