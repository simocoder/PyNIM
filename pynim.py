"""
This program plays the ancient Chinese game of NIM. 
Actually, this is a simplified version of the original game. 
In this game, the person who runs your program will be one of the two human players.
This program will be a simple Artificial Intelligence (AI) that will serve as the other player, 
as well as provide the narrative for the game and keep score, invite a friend to be the third player.

'The Python' i.e. the computer/AI player in this version is "cheeky", to make it more interesting, and to 
more fully emulate the "personality" that an actual snake/reptile might perhaps have.

If there was more time to do work on this, there would have been an option for "Do you want The Python
to be in friendly or reptilian mode?", and if in reptilian mode the AI would tell lies about 
how many stones it's removed, and sometimes cheat on the rules (e.g. by removing 4 stones), 
and make even more condescending  remarks, just to make the game more interesting. 
However this feature was not implemented, due to the extra time required and many other assessments are also due.

Rules of the Game:

    *    Number of participating Players: 2 students and 1 computer
    *    The player who goes first shall define the number of stones in the pile. The number must be between 30 to 50.
    *    Each player then removes some number (between 1 to 3) of stones from the pile in turn until one player removes the final stone.
    *    The player who goes first:
            i. Provides the number of stones to be placed in the pile,
            ii. Removes the first set of 1 to 3 stones
    *    The other player removes a set of 1 to 3 stones
    *    The players then take turns(iteration) until the final stone is removed.
    *    The player who removes the final stone is the winner (student player 1/ student player 2 / the computer).

Most of the comments in the code occur above the line(s) they are relevant to, however occasionally 
they are written underneath, in cases where writing them above would have broken up the visual appearance 
of the code itself and made it look more complicated and harder to follow/read by people.

A few lines of debugging code (in the form of print() statements) have been commented out, but left in this program.
In a 'real' commercial program this may be removed, or not, depending on the style/conventions used by the
coding company involved. Leaving the degugging code in allows for future additions to the game,
and also for any debugging that may be needed to the existing version, and which
may be helped by being able to easily activate/turn on some of the debugging info. 

Generally, variable and function names have been chosen to help make the code itself as "self-commenting" as possible.
"""

# importing the random module
import random

# Function to input the number of stones a player removes in any one turn
#
# I made this a separate function since the code gets called twice,
# and it seemed more elegant than writing it twice in the parent function
def input_players_stones(name, max_removable):
    """
    This function processes the input for a player's choice of how many stones to remove
    within each step of their turn.
    """
    num_removed = input("How many stones (from 1 to " + str(max_removable) + ") will you remove, " + name + "? (or press Enter for a mystery value): ") 
    if num_removed == '':
        num_removed = str(random.randint(1, max_removable))
        print(name + ", you have removed " + num_removed + " stones.")
        
    return(num_removed)
   

# Function definition for each human player's turn
# I made this into a function since the whole thing gets called twice
# (once for each human player). 
def players_turn(players_name):
    """
    This function processes the input for a player's turn
    """
    print("There are " + str(current_num_stones) + " stones remaining...")
    
    if current_num_stones < 3:
        max_removable_stones = current_num_stones
    else:
        max_removable_stones = 3
    
    
    num_removed = input_players_stones(players_name, max_removable_stones)
    
    while not num_removed.isnumeric() or int(num_removed) < 1 or int(num_removed) > max_removable_stones:
        print("You MUST enter a number from 1 to " + str(max_removable_stones) + "! Can you even count, " + players_name + "?")
        num_removed = input_players_stones(players_name, max_removable_stones)
        # print ('Debugging: Your corrected attempt is removing ' + num_removed + ' stones.')

        
    # print ('Debugging: You are removing ' + num_removed + ' stones.')
        
    num_removed = int(num_removed)
    
    return num_removed

# Init basic game counters and other variables
game_running = True
games_played = 1
player_1_score = 0
player_2_score = 0
pythons_score = 0

# Get basic info from players

# Display opening message and rules.
print('Welcome to PyNIM, the Ancient game of NIM played against a real live Python!')
print('... or, perhaps against a virtual Python...')
print('... or, maybe it\'s played against a computer language called Python.')
print('\nA formidable opponent... Can you (or your friend) beat the powerful AI of the Python?')
print('\nPyNIM has 3 players: Two humans, plus "The Python" which is this computer.')
print('The first player initially decides how many stones to start the game with, from 30 to 50.')
print('For each round of the game, each player gets to remove from 1 to 3 stones from the pile.')
print('The player who removes the last stone (i.e. reduces the pile to 0 stones) is the winner.\n')

# Input players' details. Completely blank inputs are rejected, and the question is repeated until answered.
player_1_name = ''
while player_1_name == '':
    player_1_name = str.capitalize(input("What is your name, Player One? "))[:30] # Limit to first 30 characters entered
    
player_1_id = ''
while player_1_id == '':    
    player_1_id   = input("What is your MIT Student ID, " + player_1_name + "? ")[:9] # Limit to first 9 characters entered
    
player_2_name = ''
while player_2_name == '':    
    player_2_name = str.capitalize(input("What is your name, Player Two? "))[:30]

player_2_id = ''
while player_2_id == '':
    player_2_id   = input("What is your MIT Student ID, " + player_2_name + "? ")[:9]

# Note that it would easily be possible to further validate the IDs above, e.g. by requiring them to begin with 'MIT',
# and to then consist of exactly 6 digits. However this was not officially in the specs and therefore
# was not implemented here to save development time. Especially since it was easier to test-play the game
# a large number of times without having to type in a valid MIT student ID string for each test run.

print("Welcome, " + player_1_name + " and " + player_2_name + " to the game of Taking Stones.")

# Loop over each single entire game until player chooses to quit
while game_running: 
      
    initial_num_stones = 0
    while initial_num_stones < 30 or initial_num_stones > 50:
        initial_num_stones = input("How many stones (from 30 to 50) would you like to start the game with, " + player_1_name + "? ")[:3] # Limit to 3 chars
        # Note above that if the input above was limited to 2 characters (as may seem more appropriate for 30-50 stones), then a value like 345 would be 
        # interpreted as 34, rather than generating an error message and asking to input the number again as is the intended behaviour.
        try:
            initial_num_stones = int(initial_num_stones)
        except ValueError:
            print("This is not even a number! Numbers consist of the digits from 0 to 9, in case you have forgotten!")
            initial_num_stones = 0
            # The computer is a "Python" so it has a cheeky/rude personality befitting a reptile
        
    print("You have selected " + str(initial_num_stones) + " stones, " + player_1_name + ". A fine choice!\n")
    
    current_num_stones = initial_num_stones
    
    while current_num_stones > 0:
        # print("There are " + str(current_num_stones) + " stones remaining...")
        
        current_num_stones -= players_turn(player_1_name)
        if current_num_stones == 0:
            winners_name = player_1_name
            winners_id = player_1_id
            player_1_score += 1
            break
        
        current_num_stones -= players_turn(player_2_name)
        if current_num_stones == 0:
            winners_name = player_2_name
            winners_id = player_2_id
            player_2_score += 1
            break
            
        # The 'Python's turn to play
        # The optimal strategy is as follows: Divide the remaining number of stones by three. 
        # If the remainder is zero, then two stones are removed, or else one stone is removed
        # *** Note that this strategy was modified for the last move of the game, where the
        #     computer will remove as many stones as possible to win on that move, if it can.
        # Since the computer's turn is processed quite differently to the human players' turns,
        # there seemed no need to make it a function, since the code only needs to be written once.
        
        if current_num_stones == 3: # This is a winning move for the final move only
            computer_removes = 3
            
        elif current_num_stones == 2: # This is a winning move for the final move only
            computer_removes = 2
            
        elif current_num_stones % 3 == 0: # This is a non-winning move on the non-final moves
            computer_removes = 2
            
        else:
            computer_removes = 1 # This may be either on the final move, or not, it's the same action for either.
            
        print("The Python has removed " + str(computer_removes) + " stones...\n")
            
        current_num_stones -= computer_removes
        
        if current_num_stones == 0:
            winners_name = "The Python"
            pythons_score += 1
            break
        
        
    # The code below calculates offsets for lining up the final asterisk in the
    # "box" display of asterisks, and displays them.
    # Note to any future development -- this section may need to be modded if there is a 
    # significant change to the character length limits on the Name and the Student ID fields
    
    print('\n' + '*' * (44 + len(winners_name)))
    #print("****************************************************")        
    print("*     And...THE WINNER IS......... " + winners_name + "!!!" + "     *")
    
    if winners_name != "The Python":
        print("*     Your MIT Student ID is: " + winners_id + ' ' * (44 + len(winners_name) - len(winners_id) - 31) +'*')
        #print("*     Congratulations, " + winners_name + "! Nice work!" + ' ' * (16 - len(winners_name)) +'*')
        print("*     Congratulations, " + winners_name + "! Nice work!        *")
        
    print('*' * (44 + len(winners_name)) + '\n')
    #print("****************************************************\n")  
    
    print("The score so far:")
    print(player_1_name + ": " + str(player_1_score))      
    print(player_2_name + ": " + str(player_2_score))      
    print("The Python: " + str(pythons_score))   
    print()   
    
    if pythons_score > player_1_score and pythons_score > player_2_score and winners_name == "The Python":
        print("Evidently, reptilian intelligence exceeds that of humans.")
        print("Perhaps you can be a better example of success for your species in the next game...?\n")
        
    elif winners_name == player_1_name or winners_name == player_2_name:
        print("The Python is hissing as it concedes to your superior playing skill. Ssssssssss...\n")

    play_again = ''
    while play_again == '':
        play_again = input("Would you like to play again? ")
    
    if play_again.lower() == 'y' or play_again.lower() == 'yes':
        games_played += 1
        print("\nGreat! Get ready for round " + str(games_played) + "...\n")
    else:
        game_running = False
        print("\nGoodbye, and thank you for playing PyNIM!!!")
        

    