#asssessment

password = input() # get a password
print(len(password)) #will print the length of the string

# check if string contains a character
def check_for_exclaimation(password):
    for character in password:
        if character == '!':
            return True
        
#isalpa() - checks if a string is alphanumeric
#isupper() - checks if 
