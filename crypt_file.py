from cryptography.fernet import Fernet
import pyperclip


class Fencrypt:
    def __init__(self):
        self.key = None
        # self.fkey = None
        self.message = ""
        self.encryptedMessage = ""
        self.decryptedMessage = ""
        # self.extention = ".enc"

    def generate_key(self):
        self.key = Fernet.generate_key()
        return self.key

    def encrypt(self, file_path, userkey):
        userkey = Fernet(userkey)
        with open(file_path, "rb") as f:
            message = f.read()
            encryptedMessage = userkey.encrypt(message)
        with open(file_path, "wb") as f:
            f.write(encryptedMessage)

    def decrypt(self, file_path, userkey):
        userkey = Fernet(userkey)
        with open(file_path, "rb") as f:
            message = f.read()
            decryptedMessage = userkey.decrypt(message)
        # file_path.replace(self.extention, "")
        with open(file_path, "wb") as f:
            f.write(decryptedMessage)


enc = Fencrypt()
x = enc.generate_key()
print(x)
enc.decrypt("example.txt", b'ralNxjzEliJ31uhGInLFgApol0TAFMoBXr5fdM2XFPU=')
