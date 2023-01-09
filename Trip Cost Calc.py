
# This program calculates and displays the total cost of a trip and splits the cost per person.



def main():

    # Ask the user for the amount of people going on the trip
    
    numPeople = int(input("How many people are going on the trip with you: "))

    # Ask the user for the length of trip in days

    numDays = int(input("How many days is the trip: "))

    # Food and gas that holds the inputs

    food = [None] * numDays

    gas = [None] * numDays

    # Ask the user for food and gas costs per day

    for i in range(numDays):

        food[i] = float(input("Cost of food for the day " + str(i+1) + ": "))

        gas[i] =  float(input("Cost of gas for the day " + str(i+1) + ":  "))

    

    foodCost = 0

    gasCost = 0

    # Loops through the cost per day based on input by the user

    for i in range(numDays):

        foodCost = foodCost + food[i]

        gasCost = gasCost + gas[i]

    # Calculate total cost of the trip

    totalCost = foodCost + gasCost

    #Calculate share of each person

    perPerson = totalCost/numPeople

    #Display the data

    print("\nTotal Food Cost:$ ",foodCost)

    print("Total Gas Cost:$  ",gasCost)

    print("Share per person:$ ",perPerson)
    
main()
