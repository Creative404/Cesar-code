import re
import time

time.sleep(0.5)
print("this program will encryp/decrypt your text in *cesar* code\n")
time.sleep(2)

def encrypt(encrypt, key):
    almost_encrypted_list = []
    encrypted = ""

    for x in encrypt:
        encrypting = ord(x)
        encrypting += key
        almost_encrypted = chr(encrypting)
        almost_encrypted_list.append(almost_encrypted)
    for xx in almost_encrypted_list:
        encrypted += xx
    return encrypted


    #ord(): #giving u ascii number
    #chr(): #number to symbol
def decrypt(decrypt, key):
    almost_decrypted_list = []
    decrypted = ""

    for x in decrypt:
        decrypting = ord(x)
        decrypting -= key
        almost_decrypted = chr(decrypting)
        almost_decrypted_list.append(almost_decrypted)
    for xx in almost_decrypted_list:
        decrypted += xx
    return decrypted

    #ord(): #giving u ascii number
    #chr(): #number to symbol

print("pick: encrypt: 1    decrypt: 2")

while True:
    try:
        choose = int(input("encrypt/decrypt: "))
        if choose < 3:
            break
        else:
            print("choose 1 or 2")
    except ValueError:
        print("choose 1 or 2")


if choose == 1:
    To_encrypt = input("Type ur text that u wanna encrypt: \n")

    while True:
        try:
            encrypt_key = int(input("Type your key encrypt (1-9): "))
            if encrypt_key <= 9 and encrypt_key >= 1:
                break

            else:
                print("only 1-9 range\n")

        except ValueError:
            print("type correct value")
            time.sleep(0.5)


    encrypted = encrypt(To_encrypt,encrypt_key)

    print("Wait a sec :3\n")
    time.sleep(2)
    print("here is yours encrypted text:")
    print(encrypted)

elif choose == 2:
    To_decrypt = input("Type ur text that you wanna decrypt: \n")

    while True:
        try:
            decrypt_key = int(input("Type your key encrypt (1-9): "))
            if decrypt_key <= 9 and decrypt_key >= 1:
                break

            else:
                print("only 1-9 range\n")

        except ValueError:
            print("type correct value")
            time.sleep(0.5)


    decrypted = decrypt(To_decrypt,decrypt_key)

    print("Wait a sec :3\n")
    time.sleep(2)
    print("here is yours encrypted text:")
    print(decrypted)






