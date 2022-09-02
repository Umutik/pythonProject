def caesar_encrypt(text, step):
    encrypted_str = ""

    for char in text:
        if not char.isalpha():
            encrypted_str += char
        elif char.isupper():
            encrypted_str += chr(((ord(char) + step - 65) % 26) + 65)
        else:
            encrypted_str += chr(((ord(char) + step - 97) % 26) + 97)

    return encrypted_str

def caesar_decrypt(text, step):
    decrypted_str = ""

    for char in text:
        if not char.isalpha():
            decrypted_str += char
        elif char.isupper():
            decrypted_str += chr(((ord(char) - step - 65) % 26) + 65)
        else:
            decrypted_str += chr(((ord(char) - step - 97) % 26) + 97)

    return  decrypted_str

def save_to_file(message, file_name):
    with open(file_name, "w") as file:
        file.write(message)

def read_from_file(file_name):
    with open(file_name) as file:
        message = file.read()
    return message



message = input("Please enter the message: ")
step = int(input("Now enter the step: "))

#Encrypt the message and save it to a file
encrypted_message = caesar_encrypt(message, step)
print("The encrypted message is:", encrypted_message)
save_to_file(encrypted_message, "encrypted_message.txt")

#Read encrypted message from file
message_from_file = read_from_file("encrypted_message.txt")
decrypted_message = caesar_decrypt(message_from_file, step)
print("The decrypted message:", decrypted_message)




