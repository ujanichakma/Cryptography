
'''Write a program that encrypts a plaintext containing letters 
and spaces using Caesar Cipher followed by Substitution Cipher. 
Then perform the reverse operation to get back the original plaintext.'''
def ceaser(text, shift):
    result = ""

    for c in text:
        if c.isalpha():
            if c.isupper():
                base = ord('A')
            else:
                base = ord('a')

            result += chr((ord(c) - base + shift) % 26 + base)

        else:
            result += c

    return result


# Substitution Encryption
def sub_encrypt(text, key):
    result = ""

    for c in text:
        if c.isalpha():
            if c.isupper():
                index = ord(c) - ord('A')
                result += key[index].upper()
            else:
                index = ord(c) - ord('a')
                result += key[index].lower()

        else:
            result += c

    return result


# Substitution Decryption
def sub_decrypt(text, key):
    result = ""

    for c in text:
        if c.isalpha():
            if c.isupper():
                index = key.index(c.upper())
                result += chr(index + ord('A'))
            else:
                index = key.index(c.upper())
                result += chr(index + ord('a'))

        else:
            result += c

    return result


# Main Program
plain_text = "Computer Science"
shift = 3

key = "QWERTYUIOPASDFGHJKLZXCVBNM"

print("Original text : \n", plain_text)


# Ceaser Encryption
ceaser_text = ceaser(plain_text, shift)
print("After ceaser : \n", ceaser_text)


# Substitution Encryption
cipher_text = sub_encrypt(ceaser_text, key)
print("After substitution encryption : \n", cipher_text)


# Substitution Decryption
decrypted_text = sub_decrypt(cipher_text, key)
print("Substitution Decryption text : \n", decrypted_text)


# Ceaser Decryption
ceaser_decrypt = ceaser(decrypted_text, -shift)
print("Decrypted Final(original) Text : \n", ceaser_decrypt)
