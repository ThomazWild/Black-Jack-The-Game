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

 
##Imports
import random
import time
from sys import exit
##Imports

#-------------------------------------------------------------------------------
#this is player
class cardGame():
    def reset(self):
        self.__init__()
        
    numberName = { 1 : "first", 2 : "second", 3 : "third",
                  4 : "fourth", 5 : "fifth", 6 : "sixth"}
    
    d = {"A" : [1,10,11], "2" : 2, "3" : 3,
            "4" : 4, "5" : 5, "6" : 6,
            "7" : 7, "8" : 8, "9" : 9,
            "10" : 10, "J" : 10, "Q" : 10, "K" : 10}
    
    deck_list = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"] 
    
    def draw(self,number):       
        for i in range(number):
             a = random.choice(self.deck_list)
             self.p += 1
             print("Your "+ str(self.numberName.get(self.p)) + " Card is " + str(a))
             time.sleep(2)
             
             #If Chosen card is the HARD A
             if a == "A":
                if self.total + 11 <= 21:
                   a = 11
                   self.cards.append(a)
                elif self.total + 10 <= 21:
                   a = 10
                   self.cards.append(a)
                else :
                   a = 1
                   self.cards.append(a)
             else:
                self.cards.append(self.d.get(a)) 
        return(self.cards,self.p)
    
    
    #calculating scores
    def calculate_scores(self):
        #calculating scores
        print(self.cards) 
        self.total = sum(self.cards)
        print("Cards total is  " + str(self.total))
        time.sleep(2)
        print()
        return(self.total)
    
    #First checking if the player got a Black Jack or not
    def check_1(self):
        if self.total == 21 and self.p == 2:
            time.sleep(2)
            print("OMFG you got a Black Jack!!!!")
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
        
        if self.total > 21 and self.total_AI > 21:
            print("You both are loser, LOL")
            exit()
        elif self.total > 21 and self.total_AI <= 21:
            print("You did an Oopsie...")
            time.sleep(1)
            print("Over 21...")
            time.sleep(1)
            print("You Oppsie, you loose")
            time.sleep(1)
            print("Captain Jack sparrow Wins")
            time.sleep(3)
            exit()
        elif self.total <= 21 and self.total_AI > 21:
            print("You are one lucky mate")
            time.sleep(1)
            print("You Wins")
            time.sleep(3)
            exit()
        else:
            if self.total > self.total_AI:
                print("You Wins")
                time.sleep(3)
                exit()
            elif self.total < self.total_AI:
                print("You loose")
                time.sleep(3)
                exit()
            else:
                print("It's a drawwww")
                time.sleep(4)
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
            
        
#-------------------------------------------------------------------------------
#This Is Where The Game Begins

print("Welcome to Russian Roulette Black Jacks")
time.sleep(2)
i = input("Proceed to play? [y/n]")
time.sleep(1)

Game = cardGame()
Game.reset
if i == "n":
    print("Oh...")
    time.sleep(1)
    print("Ok...")
    time.sleep(2)
    exit
else:
    print("let's begins...")
    #Player_1
    Player_1 = "Player 1"
    Game.p = 0
    Game.total = 0
    Game.cards = []
    Game.player = None
    
    #AI so it doesn't have name
    Game.p_AI = 0 
    Game.total_AI = 0
    Game.cards_AI = []
    Game.AI = None
    
    print("-----------------------------------")
    
    #player
    Game.draw(1)
    Game.calculate_scores()
    Game.draw(1)
    Game.calculate_scores()
    Game.check_1()
    
    #AI
    Game.AI_draw(1)
    Game.calculate_scores_AI()
    Game.AI_draw(1)
    Game.calculate_scores_AI()
    Game.check_2()
    
    print("-----------------------------------")
    
    for i in range (10):
        
        #Player
        if Game.player == True:
            print("You stands your Deck")
        else:
            hitMiss = input("Hit Or Miss? [h/m]")
            if hitMiss == "h":
                time.sleep(2)
                Game.draw(1)
                Game.calculate_scores()
            else:
                time.sleep(2)
                Game.player = True
                print("You choose Miss")
                time.sleep(1)
        
        #AI
        if Game.total_AI < 17:
            Game.AI_draw(1)
            Game.calculate_scores_AI()
        else:
            time.sleep(2)
            print("Jack Sparrow stands his deck...")
            Game.AI = True
            
        if Game.AI and Game.player:
            Game.final()
    
        print("-----------------------------------")
        

    
    
    
    
    
       
                                      


