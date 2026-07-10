# create string
from tkinter.scrolledtext import example

s1 = 'string 1'
s2 = "string 2"
s3 = '''strin3

string4
""
'''
print(s1)
print(s2)
print(s3)
text1 = "I want to say \"Hi\""
print(text1)
text2 = "First string\nSecond string\nThird string"
print(text2)
print(len(text2))
first_name = "Sveta"
last_name = "Svetlaya"
full_name = first_name + " " + last_name
print(full_name)
long_string = "Uh "*5
print(long_string)
city = 'Haifa'
temperature = 28.5
text = f"Today in {city} the temperature is {temperature}"
print(text)
print(f"Tomorrow will be : {temperature + 3}")
print(f"Name is uppercase: {first_name.upper()}")

word = "Privet"
print(word[0])
print(word[3])
print(word[-1])
print(word[0:4])
print(word[2:len(word)])
print(word[2:])
print(word[:2])
print(word[::-1])

example_text = '  I like walking  '
print(example_text.upper())
print(example_text.lower())
print("example_text".capitalize())
print(example_text.title())

print(example_text.strip())
print(example_text.lstrip())
print(example_text.rstrip())
print(example_text.strip().replace('walking', 'hiking'))

text6 = "I like walking"
parts = text6.split(" ")
print(parts)
print(" ,".join(parts))

print(text6.find('walking'))

print("walking".count("a"))
print("1234".isdigit())
print("wert".isalpha())

raw = " Today is a good day  "
print(raw.strip().replace(" ", "*"))

# 09.07.2026  "Год: 2026, Месяц: 07, День: 09"
date_str = "09.07.2026"
day, month, year = date_str.split(".")
print(f"Год: {year}, Месяц: {month}, День: {day}")

