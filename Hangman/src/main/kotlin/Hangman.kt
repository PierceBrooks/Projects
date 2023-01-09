import kotlin.random.Random

val words = listOf("elbow", "tool", "car", "time", "clothes", "tree", "show", "jeans", "mile", "tone", "calve", "leg", "bike", "phone", "milk", "wild", "can", "jar", "lick", "boat")
var word = ""
val guess = arrayListOf<Char>()
var remainingGuesses = 6
var mistakes = 0

fun main(args: Array<String>){
    setupGame()

}

fun setupGame() {
    val wordIndex: Int = Random.nextInt(words.size)
    word = words[wordIndex].toUpperCase()
    println(word)

    for(i: Int in word.indices)
        guess.add('_')

    printGamesStatus()

    println("Please enter a letter:")

    var gameOver = false

    do {

        printGamesStatus()
        println("Please enter a letter:")
        val input: String = readLine()?:""

        if(input.isEmpty()) {
            println("That's not a valid input. Please try again")
        } else {
            val letter: Char = input[0].toUpperCase()
            if(word.contains(letter)){
                for (i: Int in word.indices){
                    if (word[i] == letter)
                        guess[i] = letter
                }
                if(!guess.contains('_'))
                    gameOver = true
            }else{
                println("Sorry, that's not part of the world")
                remainingGuesses--
                mistakes++
                if(mistakes == 6)
                    gameOver = true
            }
        }

    } while (!gameOver)

    if (mistakes == 6) {
        printGamesStatus()
        println("Sorry, you lost. The word was \n$word")
    }else{
        println("\nCongratulations, you win!")
        println("The word was \n$word")
    }
}

fun printGamesStatus(){
    when(mistakes){
        0 -> print0Mistakes()
        1 -> print1Mistake()
        2 -> print2Mistake()
        3 -> print3Mistake()
        4 -> print4Mistake()
        5 -> print5Mistake()
        6 -> print6Mistake()
    }
    print("Word: ")
    for(element:Char in guess)
        print("$element ")
    println("\nYou have $remainingGuesses guess(es) left")
}

fun print0Mistakes(){
    println("   |-----|-")
    println("   |     | ")
    println("   |       ")
    println("   |       ")
    println("   |       ")
    println("   |       ")
    println("  /|\\     ")
    println(" / | \\    ")

}

fun print1Mistake(){
    println("   |-----|-")
    println("   |     | ")
    println("   |     O ")
    println("   |       ")
    println("   |       ")
    println("   |       ")
    println("  /|\\     ")
    println(" / | \\    ")
}

fun print2Mistake(){
    println("   |-----|-")
    println("   |     | ")
    println("   |     O ")
    println("   |     | ")
    println("   |     | ")
    println("   |       ")
    println("  /|\\     ")
    println(" / | \\    ")
}

fun print3Mistake(){
    println("   |-----|-")
    println("   |     | ")
    println("   |     O ")
    println("   |    /| ")
    println("   |     | ")
    println("   |       ")
    println("  /|\\     ")
    println(" / | \\    ")
}

fun print4Mistake(){
    println("   |-----|-")
    println("   |     | ")
    println("   |     O ")
    println("   |    /|\\")
    println("   |     | ")
    println("   |       ")
    println("  /|\\     ")
    println(" / | \\    ")
}

fun print5Mistake(){
    println("   |-----|-")
    println("   |     | ")
    println("   |     O ")
    println("   |    /|\\")
    println("   |     | ")
    println("   |    /  ")
    println("  /|\\     ")
    println(" / | \\    ")
}

fun print6Mistake(){
    println("   |-----|-")
    println("   |     | ")
    println("   |     O ")
    println("   |    /|\\")
    println("   |     | ")
    println("   |    / \\")
    println("  /|\\     ")
    println(" / | \\    ")
}