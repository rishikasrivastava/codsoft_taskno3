import random
import string
print("Hello,Welcome to Password Genrator!")

def gen_password(length):
    
    character=string.digits + string.ascii_lowercase + string.ascii_uppercase + string.printable
    password=''.join(random.choice(character) for _ in range(length))
    return password

def main():
    length=int(input("Enter the desired length of the password:"))

    password = gen_password(length)
    print("Generated Password :-",password)

if __name__=="__main__":
    main()    

