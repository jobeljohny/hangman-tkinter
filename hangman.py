import random
import os
import csv
import utility as ut
from constants import *

def getSolver(movie): # return the abstracted movie hiding the actual characters and randomly choose a character for the user from the movie
    org = movie[:]
    n = len(movie)
    for i in range(n):
        movie[i] = '/' if movie[i] == ' ' else '-'
    x = ' '
    while(x == ' '):
        x = random.choice(org)
    for i in range(n):
        if(x == org[i]):
            movie[i] = x

    return movie


def CheckWin(movie): # function to check weather the user has won at an instance
    for i in movie:
        if(i == '-'):
            return False
    return True


def checkChar(movie, o): #function to check weather a user inputed character exist in the movie
    for i in movie:
        if(i == o):
            return True
    return False


def update(solver, movie, o): #function to update the abstracted layer with the user inputed value
    for i in range(len(movie)):
        if(o == movie[i]):
            solver[i] = o
    return solver


def getMovie(): #function to randomly pick a movie from a csv collection of movies and return it
    r = random.randint(0, 999)
    selected = None
    with open('movies.csv') as file:
        data = list(csv.reader(file))
        selected = data[r][0]
    return selected


def game(): #the main game loop
    username = input("\n\tEnter your name : ")
    ROUND = 1
    SCORE = 0.0
    DEFEATED = False
    while(not DEFEATED):
        movie = getMovie()
        movie = list(ut.formatter(movie))

        ut.clear()
        solver = getSolver(movie[:])
        wrongs = []
        life = 6
        win = False
        while(win is False):

            ut.panel(solver, life, wrongs, ROUND, SCORE)
            o = input('\tyour Choice : ')
            if(checkChar(movie, o)):
                solver = update(solver, movie, o)
            else:
                if(o.upper() in wrongs):
                    continue
                wrongs.append(o.upper())
                life = life-1
            if(life == 0):
                break
            win = CheckWin(solver)
        if(win):
            input(WIN_MESSAGE)
            SCORE += 10 + ROUND * 3.5
            ROUND += 1
        else:
            ut.panel(solver, life, wrongs, ROUND, SCORE)
            print(LOSE_MESSAGE, ''.join(movie))
            DEFEATED = True
    input("\n\n\tpress enter to continue...")
    ut.updateLeaderboard(username, SCORE)


if __name__ == "__main__":

    choice=-1
    while(choice!=4):
        ut.clear()
        choice = ut.menu()
        if(choice == 1):
            game()
        elif(choice == 2):
            ut.displayLeaderboard()
        elif(choice == 3):
            ut.help()
        



