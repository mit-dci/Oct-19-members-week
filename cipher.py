from pycipher import Caesar

def cipher(message, offset):
    encrypted_message = Caesar(key=offset).encipher(message)
    print(f"{message} encrypted with the Caesar cipher with an offset of {offset}: ")
    print(encrypted_message)


my_message = input("Enter message to encrypt: ")

my_offset = int(input("Enter the offset: "))

cipher(my_message, my_offset)