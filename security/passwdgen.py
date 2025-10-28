import string
import random
import pyperclip

def welcome():
    print("\n=== password generator ===".title())

def passGen(length=8):
    password = ""
    asciis = [letter for letter in string.digits+string.ascii_letters+string.punctuation]
    random.shuffle(asciis)
    for i in asciis:
        if length == len(password):break
        else:password += i
    ask = input("Copy the password to clipboard? y/n: ")
    if ask.lower().startswith("y"):
        pyperclip.copy(password)
        print("Copied!")
    else:pass
    print(f"Your password is: {password}")
    return password

def ask():
    while 1:
        try:
            ask = input("\nEnter password length, leave empty for 8: ")
            if ask == "":
                passGen()
                break
            else:
                ask = int(ask)
            if ask < 8:
                smallPasswordWarning = input("""Password length below 8 is not recommended,
                    \rdo you still want to continue? y/n: """)
                if smallPasswordWarning.lower().startswith("n"):
                    continue
                else:
                    passGen(ask)
                    break
            else:
                passGen(ask)
                break
        except Exception as e:
            print(f"{e}\nInvalid argument please try again.")
            continue
    return

welcome()
ask()
