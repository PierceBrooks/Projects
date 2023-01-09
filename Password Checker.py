
# This file will ask the user to input password. The program will then asses the submission from the user and check for character requirement and display either the password is valid or what requirement is not met.

# Function to check length of the password to make sure it falls in between the guidelines
def passwordLength(password):
    
    # if it is less than 6 or greater than 15, returns true or false
    
    if(len(password) < 6 or len(password) > 15):

        return False 

    return True

# function to check if password contains spaces    
def containsSpace(password):
    
    # returns true or false if spaces are included in entry
    
    if(' ' in password):

        return True
    
    return False

# function to check if password contains both digits and alphabets    
def containsDigit(password):
    
    # first checks if length of password is valid
    if(passwordLength(password) == False):

        return "Length of password should be greater than 6 and less than 15 please try again"
    
    # check if it contains spaces
    elif(containsSpace(password)):

        return "password should not contain any spaces please try again"
    
    # if it does not contain spaces, then check if the string is all alphabets
    elif(password.isalpha()):

        return "Password should have at least one digit"
     
    # check if the string is all digits    
    elif(password.isdigit()):

        return "Password should contain at least one letter"
    
    # if all conditions are False, return Valid Password
    return "This is a valid password"

def main():

    # taking Password input from the user    
    password = input("Please enter your password: ")

    #Password will be called through all functions
    print(passwordLength(password))

    print(containsSpace(password))

    print(containsDigit(password))

main()
