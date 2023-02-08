#All 24 items are represented in an array, containing the item's name and description.
dataset = [("apple", "a round fruit with red or green skin and white flesh"),
           ("banana", "a long curved fruit with yellow skin and sweet white flesh"),
           ("carrot", "a root vegetable with an orange color and a sweet taste"),
           ("date", "a sweet dried fruit with a brown color and wrinkled skin"),
           ("eggplant", "a purple vegetable with a glossy skin and a slightly bitter taste"),
           ("fig", "a sweet fruit with a soft texture and a dark purple color"),
           ("grape", "a small round fruit with a green or purple skin and a sweet taste"),
           ("honeydew", "a large round fruit with a green skin and a sweet flesh"),
           ("kiwi", "a small brown fruit with a furry skin and a sweet green flesh"),
           ("lemon", "a yellow citrus fruit with a sour taste and a thick skin"),
           ("mango", "a tropical fruit with a yellow or red skin and a sweet juicy flesh"),
           ("nectarine", "a round fruit with a smooth skin and a sweet juicy flesh"),
           ("orange", "a round citrus fruit with a thin orange skin and a sweet juicy flesh"),
           ("peach", "a round fruit with a fuzzy skin and a sweet juicy flesh"),
           ("pear", "a fruit with a bulbous shape and a sweet juicy flesh"),
           ("pineapple", "a tropical fruit with a tough skin and a sweet juicy flesh"),
           ("raspberry", "a small red fruit with a sweet and slightly tart flavor"),
           ("strawberry", "a small red fruit with a sweet flavor and a yellow center"),
           ("tangerine", "a small citrus fruit with a thin skin and a sweet juicy flesh"),
           ("tomato", "a round fruit with a red skin and a juicy flesh often used as a vegetable"),
           ("watermelon", "a large round fruit with a green skin and a sweet juicy red flesh"),
           ("zucchini", "a green vegetable with a cylindrical shape and a mild flavor")]

import random #import function to randomly generate  items from the array
#6 items are randomly collected from the dataset array and stored in the selected_items list
selected_items = random.sample(dataset, 6)
player_score = 0 #Initialise a variable to track the player's score

#Start a for loop which will iterate over the new selected items list
#item variable will hold the item's names and descriptions
for item, description in selected_items:
#The player inputs their guess and this is saved in the player_guess variable
    player_guess = input("Guess the item ... here is a clue, " + description + ": \n")
    player_attempts = 0 #Initialise a variable to track the player's attempts

    while player_guess != item and player_attempts < 3: #If the player incorrectly guesses the item, he has 2 more attempts
        print("Incorrect, lets try that again.")
        player_guess = input("Guess the item ... here is a clue, " + description + ": \n")
        player_attempts += 1

        if player_attempts == 3: #If the player has had 3 attempts, the game ends
            print("End of game. The correct answer was " + item + "." )
            break

        if player_guess == item: #If the player correctly guesses the item, he gains a score
            player_score += 1
            print("Well done. You guessed correctly!")
            print("Your score is: ", player_score)


print("Your final score was: ", player_score) #Displays the player's final score




