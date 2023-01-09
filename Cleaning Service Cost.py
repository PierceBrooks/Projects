
def houseCleaning():

    #Price-points for cleaning levels per House

    standardCost = 60 # Price for standard cost

    premiumCost = 120 # Price for premium cost

    #Price point for house size

    small = 50 #Price of the small home

    medium = 75 #Price of the medium home

    large = 100 #Price of the large home

    #House size level: Small <=3 , Medium = 4, Large >= 5

    def TotalCleanCost(rooms, cleanType):

        # if statement that sorts through house size and cleaning cost and returns the final cost of the project

        if cleanType == 1:

            cleanCost = standardCost

        else:

            cleanCost = premiumCost

        if rooms <= 3:

            totalCost = small + rooms * cleanCost

        elif rooms == 4:

            totalCost = medium + rooms * cleanCost

        elif rooms >= 5:

            totalCost = large + rooms * cleanCost

        return totalCost

    #Ask the user for the number of rooms

    print('House service calculator:')

    rooms = eval(input('How many rooms will be cleaned?: '))

    #Ask the user for type of cleaning

    print(' Levels of cleaning:')

    print('(1) Standard: includes dusting and sweeping')

    print('(2) Premium: includes standard + mop, wax, & deep cleaning')

    cleanType = eval(input('For standard enter 1, for premium enter 2: '))

    #Call the function to get the cost

    answer = TotalCleanCost(rooms, cleanType)

    #Print out the total of cleaning the house

    print('The total cost to clean your house is $', answer)

    return answer


def yardService():

    # Prices of different yard services offered

    costMowing=20 

    costEdging=15 

    costBush=40 

    print('\nYard Service Calculator')

    # These will ask for inputs for the details of the specific yard work

    yardMowing=eval(input('\nHow many square feet do you want cut?'))

    yardEdging=eval(input('\nHow many feet of edging do you need?'))

    yardShrubs=eval(input('\nHow many bushes do you need to have trimmed?'))

    # Calculates and prints the total cost of yard servicing based on inputs above

    totalCost=yardMowing*costMowing+yardEdging*costEdging+yardShrubs*costBush

    print('\nThe total cost of yard cleaning is $',totalCost)

    # Return the cost of the service to Yard service function

    return totalCost 

# This function calculates accounts for a discuont that the user may qualify if they are a senior

def calculateDiscount(cost):

    discount= 0.15 * cost # provide a 15% discount - this percent was taken as the average rate given to seniors pulled from multiple sources

    afterDiscount=cost-discount

    return  afterDiscount



def main():

    totalCost=0

    # Ask the user what service they want

    serviceChoice=int(input('Which service do you want? (1)House Cleaning (2)Yard Service: '))

    # if statement that sorts through user inputs

    if serviceChoice==1:

        totalCost=houseCleaning() # Calls the House cleaning function and stores the final cost

    elif serviceChoice==2:

        totalCost=yardService() # Calls the Yard service function and stores the final cost

    else:

        print('INVALID INPUT')
    
    # To provide discount to senior citizens

    isSenior=input('Are you a senior citizen?(Y/N): ')

    # if statement that sorts through user inputs and determines if they are a senior

    if isSenior=='Y' or isSenior=='y':

        print('You have a 15 percent discount')

        print("Your total cost is:$",calculateDiscount(totalCost))

    else:

        print("Your total cost is:$ ",totalCost)

if __name__ == '__main__':

    main()
