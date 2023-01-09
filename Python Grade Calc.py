import sys

def main():

    score_list=get_scores()

    display_menu()

    choice=int(input("Enter your Choice:"))
    
    
    if choice==1:

        score_metrices(score_list)

    elif choice==2:

        mine_scores(score_list)

    elif choice==3:

        update_score(score_list)

    elif choice==4:

        disply_score(score_list)

    elif choice==5:

        sys.exit("You Quit The Program")

    else:

        print("NO Choice Entered from the Menu")

        

        

#fucntion 2

def get_scores():

    scores=[]

    

    number_of_test=int(input("How many Scores will you be entering:"))

    test=1

    while number_of_test>0:

        

        score=int(input("Enter test score "+str(test)+" (0-100:"))

        scores.append(score)

        

        number_of_test-=1

        test+=1

    return scores

#disply 3

def display_menu():

    print("1. Process Scores (min/max/avage)")

    print("2. Mine Scores (low/high scores)")

    print("3. Updates Score")

    print("4. Display Scores")

    print("5. Quit")



# Fucntion 4    

def score_metrices(Score_list):

    score=Score_list

    low=min(score)

    high=max(score)

    length=len(score)

    average = sum(score)/length

    print("Number of Score:",len(Score_list))

    print("High Score:",high)

    print("Low Score:",low)

    print("Average Score:",average)

    

    

#function 5    

def mine_scores(score_list):

    length=len(score_list)

    average = sum(score_list)/length

    high_test_score=[x for x in score_list if x>=average]

    low_test_score=[x for x in score_list if x<average]

    #sorting the list

    high_test_score.sort()

    low_test_score.sort()

    print("Top Scores: ")

    for i in high_test_score:

        print(format(i,".2f"))

    print("Low Scores: ")

    for i in low_test_score:

        print(format(i,".2f"))

        

        

# Function 6     

def update_score(score_list):

    print("Update test score")

    for i in range(len(score_list)):

        print(i+1,".",score_list[i])

    update=int(input("Select score number to update:"))

    try:

        new=int(input("Enter new score:"))

        score_list[update-1]=new

        for i in range(len(score_list)):

            print(i+1,".",score_list[i])

    except ValueError:

        print("Oops!  That was no valid number.")

    except NameError :

        print("Oops!  That was no valid Name. ")

    except IndexError:

        print("Oops!  IT is out of index. ")

        

# Fuction 07  

def disply_score(scores_list):

    print("Scores in reverse order:")

    reversing=scores_list[::-1]

    

    for i in range(len(scores_list)):

        print(reversing[i])

    

   

    

            

    

    

    

#score_list=get_scores()

#score_metrices(score_list) 

#mine_scores(score_list)

#update_score(score_list)

#disply_score(score_list)

main()
