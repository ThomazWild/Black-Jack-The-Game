# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:27:08 2019

@author: thewolenfire

Project name: The Black Jacks game
"""
#Ver 1.0
# - base version
#Ver 1.1 
# - Improved AI 
#Ver 1.2
# - Improved performance by incorporating class and self Part 1
#Ver 1.3
# - Improved performance by incorporating class and self Part 2
#Ver 1.4
# - Shortening class code for player add-ons
#Ver 1.5
# - Implementing Multi-player system (Big update)

 
##Imports
import random
import time
from sys import exit
##Imports
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#this is player
class cardGame():
    
    p_AI = 0 
    total_AI = 0
    cards_AI = []
    AI = None
    
    def reset(self):
        self.__init__()
        
    def start(self):
        print("Welcome to Russian Roulette Black Jacks")
        time.sleep(2)
        print("Your're playing Agains Captain. Jack Sparrow")
        time.sleep(2)
        i = input("Proceed to play? [y/n]")
        time.sleep(1)
        if i == "n":
            print("Oh...")
            time.sleep(1)
            print("Ok...")
            time.sleep(2)
            exit
        else:
            print("let's begins...")
                
        
    numberName = { 1 : "first", 2 : "second", 3 : "third",
                  4 : "fourth", 5 : "fifth", 6 : "sixth"}
    
    d = {"A" : [1,10,11], "2" : 2, "3" : 3,
            "4" : 4, "5" : 5, "6" : 6,
            "7" : 7, "8" : 8, "9" : 9,
            "10" : 10, "J" : 10, "Q" : 10, "K" : 10}
    
    deck_list = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"] 
    
    #calculating scores
    def calculate_scores(self,N):
        #calculating scores
        print(self.cards[N]) 
        self.total[N] = sum(self.cards[N])
        print("Cards total is  " + str(self.total[N]))
        time.sleep(2)
        print()
        return(self.total[N])
    
    #First checking if the player got a Black Jack or not
    def check_1(self,N):
        if self.total[N] == 21 and self.p[N] == 2:
            time.sleep(2)
            print("OMFG " + str(self.player_name[N]) + " got a Black Jack!!!!")
            time.sleep(2)
            print("You win this time...")
            time.sleep(3)
            exit()
        else:
            return
    
    #First checking if the AI got a Black Jack or not
    def check_2(self):
        if self.total_AI == 21 and self.p_AI == 2:
            time.sleep(2)
            print("OMFG Captain Jack got a Black Jack!!!!")
            time.sleep(2)
            print("He is a lucky mate!")
            time.sleep(3)
            exit()
        else:
            return
        
    #-------------------------------------------------------------------------------
        
    def final(self):
        
        time.sleep(3)
        print("Calculating scores.") 
        time.sleep(1) 
        print(".") 
        time.sleep(1)
        print(".")
        time.sleep(2)
        
        for n, i in enumerate(self.total):
            if i > 21:
                self.total[n] = 0
        print(self.total)

        if self.total == [0 for i in range(0,len(self.p))] and self.total_AI > 21:
            print("You All are loser, LOL")
            exit()
            
        elif self.total == [0 for i in range(0,len(self.p))] and self.total_AI < 21:
            print("You ALL an Oopsie...")
            time.sleep(1)
            print(" Everyone are over 21...")
            time.sleep(1)
            print("You Oppsie, you loose")
            time.sleep(1)
            print("Captain Jack sparrow Wins")
            time.sleep(3)
            exit()
        elif self.total != [0 for i in range(0,len(self.p))] and self.total_AI < 21:
            if max(self.total) < self.total_AI:
                print("Captain. Jack Sparrow wins....")
                time.sleep(4)
                exit()
            elif max(self.total) > self.total_AI:
                list_winner = [i for i, x in enumerate(self.total) if x == max(self.total)]
                print("The winner: ")
                for i in range(0,len(list_winner)):
                    list_winner[i]
                    print(self.player_name[list_winner[i]])
                exit()
            else:
                list_winner = [i for i, x in enumerate(self.total) if x == max(self.total)]
                print("The winner: ")
                for i in range(0,len(list_winner)):
                    list_winner[i]
                    print(self.player_name[list_winner[i]])
                print("And Captain Jack Sparrows.")
                exit()
        elif self.total != [0 for i in range(0,len(self.p))] and self.total_AI > 21:
            list_winner = [i for i, x in enumerate(self.total) if x == max(self.total)]
            print("The winner IS: ")
            for i in range(0,len(list_winner)):
                list_winner[i]
                print(self.player_name[list_winner[i]])
            exit()
        else:
            print("Error")
            exit()
    #-------------------------------------------------------------------------------
    #This is the AI's part
                
    def AI_draw(self,number):
        numberName = { 1 : "first", 2 : "second", 3 : "third",
                  4 : "fourth", 5 : "fifth", 6 : "sixth"}
    
        d = {"A" : [1,10,11], "2" : 2, "3" : 3,
            "4" : 4, "5" : 5, "6" : 6,
            "7" : 7, "8" : 8, "9" : 9,
            "10" : 10, "J" : 10, "Q" : 10, "K" : 10}
    
        deck_list = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"] 
        
        for i in range(number):
             a_AI = random.choice(deck_list)
             self.p_AI += 1
             print("Jack Sparrow's "+ str(numberName.get(self.p_AI)) + " card is " + str(a_AI))
             time.sleep(2)
             
             #If Chosen card is the HARD A
             if a_AI == "A":
                if self.total_AI + 11 <= 21:
                   a_AI = 11
                   self.cards_AI.append(a_AI)
                elif self.total + 10 <= 21:
                   a_AI = 10
                   self.cards_AI.append(a_AI)
                else :
                   a_AI = 1
                   self.cards_AI.append(a_AI)
             else:
                self.cards_AI.append(d.get(a_AI)) 
             
        return(self.p_AI,self.total_AI,self.cards_AI)
        
    #calculating scores
    def calculate_scores_AI(self):
        #calculating scores
        print(self.cards_AI) 
        self.total_AI = sum(self.cards_AI)
        print("Cards total is  " + str(self.total_AI))
        time.sleep(2)
        print()
        return(self.total_AI)
        
    def Number_Of_Player(self,N):
        self.p = []
        self.total = []
        self.cards = []
        self.player = []
        self.player_name = []
        self.player_status = []
        for i in range(0,N):
            self.p.append(0)
            self.total.append(0)
            self.cards.append([])
            self.player.append(0)
            self.player_status.append(0)
            Name = input("Enter player  " + str(i) +"'s Name : ")
            self.player_name.append(Name)
        return(self.p,self.total,self.cards,self.player)
            
    def draw(self,No,number):       
        for i in range(number):
             a = random.choice(self.deck_list)
             self.p[No] += 1
             print(str(self.player_name[No] + "'s " + str(self.numberName.get(self.p[No])) + " Card is " + str(a)))
             time.sleep(2)
             
             #If Chosen card is the HARD A
             if a == "A":
                if self.total[No] + 11 <= 21:
                   a = 11
                   self.cards[No].append(a)
                elif self.total[No] + 10 <= 21:
                   a = 10
                   self.cards[No].append(a)
                else :
                   a = 1
                   self.cards[No].append(a)
             else:
                self.cards[No].append(self.d.get(a)) 
        return(self.cards[No],self.p[No])
        
    def Ask_player(self,N):
        if int(self.player_status[N]) == 1 :
            print((str(self.player_name[N]) + " already stood his deck"))
        else:
            status = input((str(self.player_name[N]) + ", do you want to Hit or Miss? [h/m]"))
            print(" ")
            if status == "m":
                self.player_status[N] = 1
                return(self.player_status) 
            else:
                return
    
    def Check_player_status(self):
        if  self.player_status == [1 for i in range(0,len(self.p))] and self.AI == True :
                Game.final()
        
            
        
#-------------------------------------------------------------------------------

#Defining sh!ts
Game = cardGame()

#This Is Where The Game Begins
Game.reset()
Game.start()

#Player Define
while True:
    try:
        Players = int(input("Enter number of humanoid players: "))
        break
    except:
        print("Error")
        print("Please Enter Number")
        
Game.Number_Of_Player(Players)

print("-----------------------------------")

#player
 

    
#AI
Game.AI_draw(1)
Game.calculate_scores_AI()
Game.AI_draw(1)
Game.calculate_scores_AI()
Game.check_2()

print("-----------------------------------")

for i in range(0,len(Game.p)):
    if Game.player_status[i] == 0:
        Game.draw(i,1)
        Game.calculate_scores(i)
        Game.check_1(i)


for i in range (10):
    
    #Player
    for i in range(0,len(Game.p)):
        if Game.player_status[i] == 0:
            Game.draw(i,1)
            Game.calculate_scores(i)
            Game.check_1(i)
        
    for i in range(0,len(Game.p)):
        Game.Ask_player(i)
        Game.Check_player_status()
    #AI
    if Game.total_AI < 17:
        Game.AI_draw(1)
        Game.calculate_scores_AI()
    else:
        time.sleep(2)
        print("Jack Sparrow stands his deck...")
        Game.AI = True

    print("-----------------------------------")
        

    
    
    
    
    
       
                                      


