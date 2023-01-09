

#  This function displays and accepts the name of the students and pulls them from the main function        

def getWeightedScores(name):

    # T# The weights for the grades were inspired by UMGC curriculum. These wights are hard set into the program and cannot be edited

    discussion = 0.10

    quiz = 0.40

    assignment = 0.50

    # Displays users name and asks for discussion score

    discussionScore = float(input(f'{name}, enter discussion score: '))

    # Displays users name and asks for quiz score

    quizScore = float(input(f'{name}, enter quiz score: '))

    # Displays users name and asks for assignment score

    assignmentScore = float(input(f'{name}, enter assignment score: '))

    # Computes and returns the average of scores input by user

    average = discussionScore * discussion + quizScore * quiz + assignmentScore * assignment

    return average


def main():

    # List of all the students that need to have grades input and calculate

    names = ['Jonny Lewis', 'Sally Tomson', 'Connor Luke', 'Brandon Jole']

    highestScore = 0

    topStudent = ''

    # For loop that cycles through list of student list

    for i in range(len(names)):

        score = getWeightedScores(names[i])

        print(f'\n{names[i]} weighted score: {score:.2f}\n')

        # If statement that displays the student with the highest score after each input cycle by the user

        if i == 0 or highestScore < score:

            highestScore = score

            topStudent = names[i]

        print(f'{topStudent} has the highest score : {highestScore:.2f}\n')


main()
