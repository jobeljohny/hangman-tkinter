import os
from constants import *
# DICTIONARY to store UI for Hangman stages
stagesUI = {}
# tuple containing characters that are to be removed while playing the game
invalidTuplues = (':', '.', "'", '-', '?', '/', '!', ',', '(', ')')

def clear():
    os.system("cls" if os.name=='nt' else 'clear')
def formatter(movie): # removing unwanted characters from the movie for the ease of user
    movie = movie.lower()
    for ichar in invalidTuplues:
        movie = movie.replace(ichar, '')    
    return movie


def populateHangmanUI():  
    # populate the Stages UI to display each stage of the hangman , a text file is read once at the begining of program execution
    # and the text is formatted and stored in the data structure (DICTIONARY) as hey value pairs representing the stages of the hangman
    global stagesUI
    content = ''
    with open("hangmanUI.txt", 'r') as f:
        content = f.read()
    stages = content.split('X')
    stagesUI = {}
    for i, stage in enumerate(stages):
        stagesUI[i] = stage

def fetchLeaderBoard(): # function to fetch and return leaderboard entries
    with open("leaderboard.txt", 'r') as f:
        entries=[]
        for line in f:
            name, score = line.split(':')
            entries.append([name.title(),float(score)])
    return entries
            


def updateLeaderboard(username,score): # function to add new entry to the leaderboard and update the ranking
    content = fetchLeaderBoard()
    content.append([username,score])
    content.sort(key= lambda l:l[1],reverse =True) #sorting the leaderboard based on score
    with open("leaderboard.txt",'w') as f:
        for entry in content:
            f.write(entry[0]+':'+str(entry[1])+'\n')

def displayLeaderboard(): # function to display the leaderboard in a pretty formatted manner
    clear()
    print("\n\t      LEADERBOARD\n\n")
    print('\t{name:<10} |\t{score:>5}'.format(name='PLAYER',score='SCORE'))
    print('\t'+"-"*23)
    content = fetchLeaderBoard()
    for i,entry in enumerate(content):
        name,score=entry
        print('\t{name:<10} |\t{score:>5}'.format(name=name,score=score))
    input('\n\n\tpress enter to go back')


    

def panel(solver, life, wrongs,round,score): # displays panel UI for the game area with formatted texts
    clear()
    print('\n')
    print('{}ROUND {}\t\tSCORE : {}\n\n'.format('\t'*4,round,score))
    print('\t', ''.join(solver).upper(), '\t\t LIFE REMAINING :',
          life, '\t\tErrors : ', *wrongs)
    print()
    print(stagesUI.get(life))
    print('\n\n')

def help():
    clear()
    print(HELP)
    input()

def menu(): # The main selection menu for the game
    print(HANGMAN_WORD_ART)
    options='''
    \t1. START GAME
    \t2. VIEW LEADERBOARD
    \t3. HELP
    \t4. EXIT

    '''
    print(options)
    return int(input("\tChoice : "))





populateHangmanUI() # populates the hangman stage UI DICTIONARY for retrieving the states of the hangman stick UI