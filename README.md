# PyNIM
The ancient game of NIM (simplified) in Python. I wrote this as a student exercise.

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

