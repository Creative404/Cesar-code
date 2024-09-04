import time

time.sleep(0.5)
print("this program will encryp/decrypt your text in cesar code\n")
time.sleep(2)

def encrypt():
    print()
def decrypt():
    print()

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

#ord(char): #giving u ascii number