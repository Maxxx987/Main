
import re

phone_numbers = ["(123) 456-7890", "987-654-3210", "555.123.4567", "1234567890"]

patern = r'\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{3}.\d{3}.\d{4}|\d{10}'

for number in phone_numbers:
    if number == patern:
        print(number)