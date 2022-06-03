# Constants are stored in this file

HANGMAN_WORD_ART = '''
 \t##  ##     ##     ##  ##    ####    ##   ##    ##     ##  ##  
 \t##  ##    ####    ### ##   ##  ##   ### ###   ####    ### ##  
 \t##  ##   ##  ##   ######   ##       #######  ##  ##   ######  
 \t######   ######   ######   ## ###   ## # ##  ######   ######  
 \t##  ##   ##  ##   ## ###   ##  ##   ##   ##  ##  ##   ## ###  
 \t##  ##   ##  ##   ##  ##   ##  ##   ##   ##  ##  ##   ##  ##  
 \t##  ##   ##  ##   ##  ##    ####    ##   ##  ##  ##   ##  ##  
                                                               
'''
HELP = [
    '''
a game in which the object is for one player to guess the letters of an unknown
movie before the computer creates a stick figure of a hanged man by drawing one
line for each incorrect guess
''',
'''
you can guess an alphabet from movie by pressing any of the key from your keyboard.
if the character you pressed is in the movie, it will be marked, else one of your 
life will be lost.
the process continues until you run out of lives, or if you win.

you will be taken to the next round if you can correctly guess the movie before 
your life runs out.
''',
'''
Each successful round gives you a score. the score modifier is multiplied as you
pass onto higher levels.
your final score after you run out of lives is updated in the leaderboards. 
'''
]

WIN_MESSAGE = '\n\n\tYOU WON, Press enter for next round'
LOSE_MESSAGE = '\n\n\tYOU LOSE!!! the movie was'
