import string
import random
import secrets

alpha = list(string.ascii_letters)
numbers = list(string.digits)
special_characters = list(string.punctuation)
pwd_complexity = ""
no_of_chracters = 0

no_of_chracters = int(input("Length of password? \n"))
while no_of_chracters <8:
    print("Minimum of 8 characters is needed for a strong password")
    no_of_chracters = int(input("Length of password? \n"))
    if no_of_chracters >= 8:
        break

pwd_complexity = str(input("Complexity of password? (a = High security (recommended for financial accounts), b = Standard security (suitable for general websites)) \n"))
while pwd_complexity not in ("a", "b"):
    print("You need to enter a complexity for the password.")
    pwd_complexity = str(input("Complexity of password? (a = High security (recommended for financial accounts, b = Standard security (suitable for general websites)) \n"))
    if pwd_complexity in ("a", "b"):
        break

if pwd_complexity == "a":
    your_new_pwd = []
    for _ in range(no_of_chracters):
        your_new_pwd.append(secrets.choice(alpha))
    for _ in range(no_of_chracters):
        your_new_pwd.append(secrets.choice(numbers))
    for _ in range(no_of_chracters):
        your_new_pwd.append(secrets.choice(special_characters))
    pwd = "".join(secrets.choice(your_new_pwd) for i in range(no_of_chracters))
    print("--------------------------********************------------------")    
    print(f"Your secure password is: {pwd}")
    print("--------------------------********************------------------")  
    print("This password was generated using cryptographic-quality randomness for sensitive applications. Consider using it for Banking, email, primary accounts")
elif pwd_complexity == "b":
    your_new_pwd = []
    for _ in range(no_of_chracters):
        your_new_pwd.append(random.choice(alpha))
    for _ in range(no_of_chracters):
        your_new_pwd.append(random.choice(numbers))
    for _ in range(no_of_chracters):
        your_new_pwd.append(random.choice(special_characters))
    pwd = "".join(random.choice(your_new_pwd) for i in range(no_of_chracters))
    print("--------------------------********************------------------")
    print(f"Your insecure password is: {pwd}")
    print("--------------------------********************------------------")  
    print("This password was generated using a standard random generator, which is less secure. These passwords are suitable for non-critical accounts where absolute security isn't essential. While still difficult to guess, they don't use cryptographic-level randomness and shouldn't be used for financial or highly sensitive accounts.")

print("Thank you for using the password generator")

