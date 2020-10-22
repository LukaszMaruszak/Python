# zad 2.10 Autor: Lukasz Maruszak

line = """Ala ma     kota i     psa. 
Lubi jeść       kotlety, a 
na spacer chodzi do parku."""
words = []
words = line.split()
n_words = len(words)

print("zad 2.10 line is: " + line)
print("zad 2.10 Number of words in the line is: " + str(n_words))

# zad 2.11

result_word = ""
i = 0
for char in "word":
    result_word += char + "_"
result_word = result_word[:-1]
print("\nzad 2.11: " + result_word)


# zad 2.12
first_character_word = ""
last_character_word = ""
for word in words:
    first_character_word = first_character_word + word[0]

for word in words:
    last_character_word = last_character_word + word[len(word)-1]

print("\nzad 2.12 First character word: " + first_character_word)
print("zad 2.12 Last character word: " + last_character_word)

# zad 2.13
suma = 0
for word in words:
    w_length = len(word)
    suma += w_length

print("\nzad 2.13 Sum of word lengths in: " + line + "  is: " + str(suma))

# zad 2.14
max_length = 0
max_word = ""
for word in words:
    if len(word) > max_length:
        max_length = len(word)
        max_word = word

print("\nzad 2.14 Max length word in line: " + line + " is: " + max_word + " length: " + str(max_length))


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = ""
for item in L:
    number = number + str(item)

print("\nzad 2.15 Numbers in List: ", L)
print("zad 2.15 Number: " + number )

# zad 2.16
line_to_replace = "This is line with GvR"
word_to_find = "GvR"
new_word = "Guido van Rossum"

print("\nzad 2.16 Line to find GvR: " + line_to_replace)

line_to_replace = line_to_replace.replace(word_to_find, new_word)

print("zad 2.16 Line with replaced words: " + line_to_replace)

# zad 2.17

alphabetical_sort = sorted(words, key=str.lower)
length_sort = sorted(words, key=len)
print("\nzad 2.17 Alphabetical sort: " + str(alphabetical_sort))
print("zad 2.17 Length sort: " + str(length_sort))
length_sort = sorted(words, key=len, reverse=True)
print("zad 2.17 Length sort: " + str(length_sort))

# zad 2.18

number = 1505020800407000006456400001
number_of_zero = 0
for char in str(number):
    if char == "0":
        number_of_zero += 1

print("\nzad 2.18 Number of zeros in the number: " + str(number) + " is " + str(number_of_zero))

# zad 2.19

L2 = [123, 12, 3, 25, 999, 56, 3, 0]
print("\nzad 2.19 List: ", L2)

for i in range(len(L2)):
    L2[i] = str(L2[i]).zfill(3)

print("\t\t List: ", L2)


