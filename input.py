user_text = input('Enter some text: ')
#
# print(user_text.upper())
#
# user_number = input("What do you wnat to double? ")
#
# print(int(user_number) * 2)
# print(type(user_number))

upper_or_lower = input("Enter 1 to uppercase and 2 to lowercase: ")
if upper_or_lower == "1":
    print(user_text.upper())
else:
    print(user_text.lower())
