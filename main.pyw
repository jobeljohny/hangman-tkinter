import tkinter as tk
from tkinter import *
import hangman as HM
import constants as C
import utility as ut


class SampleApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.root.geometry("800x500") # setting window geometry
        self.root.config(background="#fffee0")
        self.setVariables()
        self._frame = None
        Label(self.root, text="H A N G M A N", fg="Green", bg="#fffec8", font=('Arial', 15, 'bold')).pack(
            side='top', fill='x', pady=5)
        self.switch_frame("menu") # Loading the menu frame initially for the user

    # This function sets the initial values for all the variables thar are dynamically changed during the game  
    def setVariables(self): 
        # help
        self.helpTitle = StringVar()
        self.helpTitle.set("About")
        # username
        self.username = StringVar()
        self.username.set('')
        # game
        self.roundString = StringVar()
        self.roundString.set('')

        self.scoreString = StringVar()
        self.scoreString.set('')

        self.template = StringVar()
        self.template.set('N--H-/--/T--/MUSE---')

        self.lifes = StringVar()
        self.lifes.set('')

        self.errorList = StringVar()
        self.errorList.set('')

    # this function updates the UI variables depending on the binded variables
    def setter(self, entity, value):
        if(entity == 'template'):
            template = ''.join(value)
            template = template.upper()
            self.template.set(template)
        elif(entity == 'round'):
            self.roundString.set('ROUND : '+str(value))
            print('round updated!')
        elif(entity == 'score'):
            self.scoreString.set('SCORE : '+str(value))
            print('score updated!')
        elif(entity == 'life'):
            self.lifes.set('LIFE REMAINING : ' + str(value))
            print('life updated!')
        elif(entity == 'error'):
            self.errorList.set('Errors : ' + ' '.join(value))
            print('error updated!')
        

    def setHangImage(self,s): # updates the hangman image UI based on the life value
        try:
            img = PhotoImage(file='states/hangman{}.png'.format(6-s))
            self.hangmanLabel.configure(image=img)
            self.hangmanLabel.image=img
        except Exception as e:
            print("no resource found")

        
            
        #this function set the game variables on load
    def initializeSetters(self):
        self.roundString.set('ROUND : 1')
        self.scoreString.set('SCORE : 0.0')
        self.lifes.set('LIFE REMAINING : 6')
        self.errorList.set('Errors : ')

    def switch_frame(self, frameName):
        # Destroys current frame and replaces it with a new one. different frame is loaded as per user menu option
        if self._frame is not None:
            self._frame.destroy()
        new_frame = None
        if(frameName == 'menu'):
            new_frame = self.StartPage()
        elif(frameName == 'username'):
            new_frame = self.UserNamePage()
        elif(frameName == 'game'):
            new_frame = self.GamePage()
        elif(frameName == 'leaderboard'):
            new_frame = self.LeaderboardsPage()
        elif(frameName == 'help'):
            new_frame = self.HelpPage()

        self._frame = new_frame
        self._frame.pack()
    # a controller model funtions to switch to each page frame
    def HomePage(self):
        print("switching to startGame...")
        self.switch_frame('menu')

    def UserName(self):
        print("switching to username...")
        self.switch_frame('username')

    def GameScreen(self):
        print("switching to game...")
        self.switch_frame('game')

    def LeaderBoard(self):
        print("switching to leaderboard...")
        self.switch_frame('leaderboard')

    def Help(self):
        print("switching to help...")
        self.switch_frame('help')

    def Exit(self):
        print("works 4")

    def validAndStartGame(self):
        self.GameScreen()

    #start page displaying and routing all the menu
    def StartPage(self):

        frame = Frame(self.root, background="#fffee0")
        Label(frame, text="Welcome to Hangman - Movies!\nChoose an option", background="#fffee0", font=("Bahnschrift", 20)).pack(
            side="top", fill="x", pady=(20, 50))
        #drop= OptionMenu(frame, self.menu,"C++", "Java","Python","JavaScript","Rust","GoLang")
        # drop.pack()
        Button(frame, text="START GAME", width=25, height=1, font=('Comic Sans MS', 12, 'bold'), bg='#CBC3E3', fg='#C70039', borderwidth=0,
               command=self.UserName).pack(pady=8)
        Button(frame, text="LEADERBOARD", width=25, height=1, font=('Comic Sans MS', 12, 'bold '), bg='#CBC3E3', fg='#C70039', borderwidth=0,
               command=self.LeaderBoard).pack(pady=8)
        Button(frame, text="HELP", width=25, height=1, font=('Comic Sans MS', 12, 'bold '), bg='#CBC3E3', fg='#C70039', borderwidth=0,
               command=self.Help).pack(pady=8)
        Button(frame, text="EXIT", width=25, height=1, font=('Comic Sans MS', 12, 'bold '), bg='#CBC3E3', fg='#C70039', borderwidth=0,
               command=self.Exit).pack(pady=8)
        return frame


    def UserNamePage(self):

        frame = Frame(self.root, background="#fffee0")
        Label(frame, text="ENTER YOUR NICKNAME", background="#fffee0", font=("Bahnschrift", 20)).pack(
            side="top", fill="x", pady=(20, 80))
        namePanel = Frame(frame, background="#fffee0")
        namePanel.pack(pady=40)

        Entry(namePanel, textvariable=self.username, width=15,
              font=("Arial", 20, "bold")).grid(row=0, column=0)
        Button(namePanel, text="OK", width=5, height=2, bg='#CBC3E3', fg='#C70039', borderwidth=0,
               command=self.validAndStartGame).grid(row=0, column=1, padx=5)
        Button(frame, text="Go back to menu", width=25, height=1, font=('Comic Sans MS', 14, 'bold'), bg='#CBC3E3', fg='#C70039', borderwidth=0,
               command=self.HomePage).pack(pady=(80, 0))
        return frame

    #function to update the game state based on the key event provided by the user
    def keyPressed(self, key):
        if(self.DEFEATED):
            return
        print(key)
        if(HM.checkChar(self.movie, key)):
            self.solver = HM.update(self.solver, self.movie, key)
            self.setter('template', self.solver)
        else:
            if(key.upper() in self.wrongs):
                return
            self.wrongs.append(key.upper())
            self.life = self.life-1
            self.setter('error', self.wrongs)
            self.setter('life', self.life)
            self.setHangImage(self.life)
        if(self.life == 0):
            self.resultLabel = Label(self._frame, text="You Lost! the movie was "+''.join(self.movie), background="#fffee0", foreground='#002d69',
                                  font=("Bahnschrift", 15))
            self.resultLabel.grid(row=5, column=0, columnspan=3, pady=(30, 4))
            self.resultButton = Button(self._frame, text="ok", width=3, height=1, font=(
                'Arial', 10, 'bold'), bg='green', fg='yellow', borderwidth=0, command=self.updateLeaderBoard)
            self.resultButton.grid(row=6, column=0, columnspan=3)
            self.DEFEATED = True
        win = HM.CheckWin(self.solver)
        if(win):
            # input(WIN_MESSAGE)

            self.resultLabel = Label(self._frame, text="Congrats! the movie is "+''.join(self.movie), background="#fffee0", foreground='#002d69',
                                  font=("Bahnschrift", 15))
            self.resultLabel.grid(row=5, column=0, columnspan=3, pady=(30, 4))
            self.resultButton = Button(self._frame, text="ok", width=3, height=1, font=(
                'Arial', 10, 'bold'), bg='green', fg='yellow', borderwidth=0, command=self.updateScoreAndUI)
            self.resultButton.grid(row=6, column=0, columnspan=3)
            #print(LOSE_MESSAGE, ''.join(movie))
            
    #funtion to update the UI and scpre once user clears a round
    def updateScoreAndUI(self):
        self.score += 10 + self.round * 3.5
        self.round += 1
        self.setter('score', self.score)
        self.setter('round', self.round)
        self.resultLabel.grid_forget()
        self.resultButton.grid_forget()
        self.resetMovieRound()
    def updateLeaderBoard(self):
         ut.updateLeaderboard(self.username.get(), self.score)
         self.HomePage()

    #function to reset variables and UI elements upon completing a round
    def resetMovieRound(self):
        self.movie = HM.getMovie()
        self.movie = list(ut.formatter(self.movie))
        self.solver = HM.getSolver(self.movie[:])
        self.wrongs = []
        self.life = 6
        self.win = False
        self.setter('template', self.solver)
        self.setter('life', self.life)
        self.setter('error', self.wrongs)
        self.setHangImage(self.life)
        print(self.movie, self.solver)

    #the Main game UI frame
    def GamePage(self):
        self.initializeSetters()
        self.DEFEATED = False
        self.round = 1
        self.score = 0.0
        
        frame = Frame(self.root, background="#fffee0")
        Label(frame, textvariable=self.roundString, background="#fffee0", foreground='#0000ff',
              font=("Bahnschrift", 15)).grid(row=0, column=0, padx=50, pady=(10, 0))
        Label(frame, textvariable=self.scoreString, background="#fffee0", foreground='#81B622',
              font=("Bahnschrift", 15)).grid(row=0, column=1, padx=50)
        Label(frame, textvariable=self.lifes, background="#fffee0", foreground='#faaf3e',
              font=("Bahnschrift", 12)).grid(row=1, column=0, padx=50, pady=30)
        Label(frame, textvariable=self.errorList, background="#fffee0", foreground='red',
              font=("Bahnschrift", 12)).grid(row=1, column=1, padx=50)
        Label(frame, textvariable=self.template, background="#fffee0", foreground='#141413',
              font=("Bahnschrift", 20)).grid(row=2, columnspan=3, pady=(30, 10))
        img = PhotoImage(file='states/hangman0.png')
        img = img.subsample(1, 1)
        self.hangmanLabel = Label(frame, image=img, background="#fffee0")
        self.hangmanLabel.Image = img
        self.hangmanLabel.grid(rowspan=2, column=2, row=0)
        ##
        buttonStack1 = Frame(frame, background="#fffee0")
        buttonStack2 = Frame(frame, background="#fffee0")
        for i in range(26):
            if(i < 15):
                Button(buttonStack1, text=chr(65+i), width=3, height=1, bg='#CBC3E3', fg='#C70039', borderwidth=0,  font=('Comic Sans MS', 12),
                       command=lambda x=chr(97+i): self.keyPressed(x)).grid(row=0, column=i, padx=2)
            else:
                Button(buttonStack2, text=chr(65+i), width=3, height=1, bg='#CBC3E3', fg='#C70039', borderwidth=0, font=('Comic Sans MS', 12),
                       command=lambda x=chr(97+i): self.keyPressed(x)).grid(row=1, column=i, padx=2)
        buttonStack1.grid(row=3, columnspan=3, column=0, pady=(30, 6))
        buttonStack2.grid(row=4, columnspan=3, column=0)
        self.resetMovieRound()
        # frame.update()
        return frame

    #the leaderboard framew is fetched here 
    def LeaderboardsPage(self):

        frame = Frame(self.root, background="#fffee0")
        Label(frame, text="LEADERBOARD", background="#fffee0", font=("Bahnschrift", 20)).pack(
            side="top", fill="x", pady=(20, 50))

        dataFrame = Frame(frame)
        dataFrame.pack()

        self.LeaderBoardFrame(dataFrame)
        Button(frame, text="Go back to menu", width=25, height=1, font=('Comic Sans MS', 14, 'bold'), bg='#CBC3E3', fg='#C70039', borderwidth=0,
               command=self.HomePage).pack(pady=8)
        return frame

    #the leaderboard is displayed here
    def LeaderBoardFrame(self, lframe):

        data = ut.fetchLeaderBoard()
        if(len(data) < 0):
            return
        TOP = 10 if len(data) > 10 else len(data)
        for i in range(TOP):
            for j in range(len(data[0])+1):
                if(j == 0):
                    self.e = Entry(lframe, borderwidth=1, width=2, fg='blue',
                                   font=('Arial', 14))
                    self.e.grid(row=i, column=0)
                    self.e.insert(END, i+1)
                    self.e.config(state='disabled')
                    self.e.configure(disabledbackground="#CBC3E3" if i %
                                     2 == 0 else '#fffee0', disabledforeground="#191970")
                    continue
                elif(j == 1):
                    self.e = Entry(lframe, width=13, borderwidth=1, fg='blue',
                                   font=('Arial', 14))
                elif(j == 2):
                    self.e = Entry(lframe, width=8, borderwidth=1, fg='blue',
                                   font=('Arial', 14))
                self.e.grid(row=i, column=j+1)
                self.e.insert(END, data[i][j-1])
                self.e.config(state='disabled')
                self.e.configure(disabledbackground="#CBC3E3" if i %
                                 2 == 0 else '#fffee0', disabledforeground="#191970")

    def updateHelpText(self, box, title):
        indexer = {"About": 0, "How to Play": 1, "Scoring": 2}
        box.configure(state='normal')
        box.delete('1.0', END)
        box.insert('end', C.HELP[indexer[title.get()]])
        box.configure(state='disabled')

    def HelpPage(self):
        frame = Frame(self.root, background="#fffee0")
        Label(frame, text="HELP", background="#fffee0", font=("Bahnschrift", 20)).pack(
            side="top", fill="x", pady=(20, 10))
        Label(frame, textvariable=self.helpTitle, background="#fffee0", font=("Bahnschrift", 15)).pack(
            side="top", fill="x", pady=(20, 20))
        helpFrame = Frame(frame, background="#fffee0")
        helpFrame.pack()
        self.helpTextBox = Text(helpFrame, height=10, width=65, wrap='word', font=(
            'Bahnschrift'), bg='#fffee0', fg='#D71039', borderwidth=0)
        self.helpTextBox.grid(row=0, column=0, pady=(0, 10), padx=5)
        options = ["About", "How to Play", "Scoring"]
        self.updateHelpText(self.helpTextBox, self.helpTitle)
        drop = OptionMenu(helpFrame, self.helpTitle, *options,
                          command=lambda x: self.updateHelpText(self.helpTextBox, self.helpTitle))
        drop.grid(row=0, column=1)

        Button(frame, text="Go back to menu", width=25, height=1, font=('Comic Sans MS', 14, 'bold'), bg='#CBC3E3', fg='#C70039', borderwidth=0,
               command=self.HomePage).pack(pady=8)
        return frame


if __name__ == "__main__":
    root = tk.Tk()
    my_gui = SampleApp(root)
    root.mainloop()
