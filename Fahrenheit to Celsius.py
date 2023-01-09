#Pierce Brooks

#Temperature conversion program

#This program allows the user to select which degree conversion they want then input the data


#This function works as the control panel for the whole program
def main():
    

    display_menu()
    

    choice = int(input("Enter your choice: "))
    

    if choice == 1:

        
        to_fahr()

        
    elif choice == 2:

        
        to_cels()

        
    elif choice == 3:

        
        to_quit()

        
    else:
        
    
        main()

        
# This functions provides the menu options the users has to get desired temp conversion
def display_menu():

    
    print('Temperature Conversions')

    
    print('')

    
    print('1) Celsius to Fahrenhiet')

    
    print('2) Fahrenheit to Celsius')

    
    print('3) Quit')

    
# This is the equation and input for the Celsius to Fahrenhiet    
def to_fahr():
    
 
    print("Convert Celsius to Fahrenhiet")

    
    ctemp = int(input('Enter the Celsius temperature to convert: '))

    
    f_ctemp = "{:.2f}".format(ctemp)
    

# Formula to convert Celsius to Fahrenhiet    
    fahrenheit = (9/5) * ctemp + 32

    
    print(f_ctemp + ' degrees Celsius is  {:.2f} '.format(fahrenheit) + 'degrees Fahrenheit')

    
    main()

    
# This is the equation and input for the Fahrenhiet to Celsius
def to_cels():
    

    print("Convert Fahrenheit to Celsius")

    
    ftemp = int(input('Enter the Fahrenheit temperature to convert: '))

    
    c_ftemp = "{:.2f}".format(ftemp)
    

# Formula to convert Fahrenhiet to Celsius    
    celsius = (ftemp - 32) * 5 / 9

    
    print(c_ftemp + ' degrees Fahrenheit is {:.2f} '.format(celsius) + 'degrees Celsius')

    
    main()


# This function ends the program
def to_quit():

    
    print("Exiting the Program...")

    

    
main()



