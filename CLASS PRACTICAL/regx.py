import re

text = "My name is Samuel and my phone number is 9876543210."

# Search for a name
name = re.search(r"Samuel", text)

if name:
    print("Name found:", name.group())

# Search for a 10-digit phone number
phone = re.search(r"\d{10}", text)

if phone:
    print("Phone number found:", phone.group())

# Find all digits
numbers = re.findall(r"\d+", text)

print("Numbers found:", numbers)
