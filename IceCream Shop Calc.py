# Programmer name: Pierce Brooks
# Icecream order calc
# This program takes the number of icecream scoops you order and calculates the price

# Metrics for the order, scoops and price point 

scoops = int(input("How many scoops would you like? "))

regular_price = 1.50

discounted_price = 1.25



# Advises user that their selection is not sufficient

if scoops <= 0:

    print(f'You asked for {scoops} scoops. You must order one or more scoops')



# Determins the price point per scoop based on scoops selected
    
if scoops <= 0:
            
    print(" ")

elif scoops >= 3:

    print(f'The price per scoop is ${discounted_price:.2f}.')

else:

    print(f'The price per scoop is ${regular_price:.2f}.')



# Calculates the order by multiply scoops by price point        

if scoops <= 0:
    
    print(" ")

elif scoops >= 3:
            
            order = discounted_price * scoops 
else:
            
            order = regular_price * scoops



# Displays the amount od sccop selected         

if scoops <= 0:

    print(" ")

elif scoops >= 2:
    
        print(f'Your ordered {scoops} scoops.')
        
else:
    
        print(f'Your ordered {scoops} scoop.')




# Displays the total cost of the order   

if scoops <= 0:

    print(" ")

else:

    print(f'Your total cost is ${order:.2f}.')




