#generating random password
#importing libraries
#defining function password_func
def password_func():
    import random
    import string
    characters= string.ascii_letters + string.punctuation + string.digits
#defining a variable called characters to determine the types of characters the password would be made of
    password = ''
#defining the variable to house the password
    password_length = random.randint(5, 20)
    for num in range (password_length):
#pick a random number, minimum should be 5, maximum should be 20

        char = random.choice(characters)
        password = password + char
    print(password)
password_func()