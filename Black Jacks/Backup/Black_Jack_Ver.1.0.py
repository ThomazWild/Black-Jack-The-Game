# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 17:27:08 2019

@author: thewolenfire

Project name: The Black Jacks game
"""

import random
import time
from sys import exit


#Defining SHits

#-------------------------------------------------------------------------------
#this is player
def draw(p,total,number):
    numberName = { 1 : "first", 2 : "second", 3 : "third",
              4 : "fourth", 5 : "fifth", 6 : "sixth"}

    d = {"A" : [1,10,11], "2" : 2, "3" : 3,
        "4" : 4, "5" : 5, "6" : 6,
        "7" : 7, "8" : 8, "9" : 9,
        "10" : 10, "J" : 10, "Q" : 10, "K" : 10}

    deck_list = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"] 
    
    for i in range(number):
         a = random.choice(deck_list)
         p += 1
         print("Your "+ str(numberName.get(p)) + " Card is " + str(a))
         time.sleep(2)
         
         #If Chosen card is the HARD A
         if a == "A":
            if total + 11 <= 21:
               a = 11
               cards.append(a)
            elif total + 10 <= 21:
               a = 10
               cards.append(a)
            else :
               a = 1
               cards.append(a)
         else:
            cards.append(d.get(a)) 
         
    return(p,total,cards)



def calculate_scores(total,cards):
    #calculating scores
    print(cards) 
    total = sum(cards)  
    print("Cards total is  " + str(total))
    time.sleep(2)
    print()
    return(total,cards)
    
    
    
def ask_the_player(total,total_AI):
    hitMiss = input("Hit Or Miss? [h/m]")
    if hitMiss == "m":
        print("Your total is: " + str(total))
        time.sleep(2)
        print("Jack Sparrow's total is: " + str(total_AI))
        time.sleep(2)
        final(total, total_AI)
    else:
        return
    
def check_1(p,total):
    if total == 21 and p == 2:
        time.sleep(2)
        print("OMFG you got a Black Jack!!!!")
        time.sleep(2)
        print("You win this time...")
        time.sleep(3)
        exit()
    else:
        return
    
#-------------------------------------------------------------------------------
    
def final(total, total_AI):
    
    time.sleep(3)
    print("Calculating scores.") 
    time.sleep(1) 
    print(".") 
    time.sleep(1)
    print(".")
    time.sleep(2)
    
    if total > 21 and total_AI > 21:
        print("You both are loser, LOL")
        exit()
    elif total > 21 and total_AI <= 21:
        print("You did an Oopsie...")
        time.sleep(1)
        print("Over 21...")
        time.sleep(1)
        print("You Oppsie, you loose")
        time.sleep(1)
        print("Captain Jack sparrow Wins")
        time.sleep(3)
        exit()
    elif total <= 21 and total_AI > 21:
        print("You are one lucky mate")
        time.sleep(1)
        print("You Wins")
        time.sleep(3)
        exit()
    else:
        if total > total_AI:
            print("You Wins")
            time.sleep(3)
            exit()
        elif total < total_AI:
            print("You loose")
            time.sleep(3)
            exit()
        else:
            print("It's a drawwww")
            time.sleep(1)
            exit()

#-------------------------------------------------------------------------------
#This is the AI's part
            
def AI_draw(p_AI,total_AI,number):
    numberName = { 1 : "first", 2 : "second", 3 : "third",
              4 : "fourth", 5 : "fifth", 6 : "sixth"}

    d = {"A" : [1,10,11], "2" : 2, "3" : 3,
        "4" : 4, "5" : 5, "6" : 6,
        "7" : 7, "8" : 8, "9" : 9,
        "10" : 10, "J" : 10, "Q" : 10, "K" : 10}

    deck_list = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"] 
    
    for i in range(number):
         a_AI = random.choice(deck_list)
         p_AI += 1
         print("Jack Sparrow's "+ str(numberName.get(p_AI)) + " card is " + str(a_AI))
         time.sleep(2)
         
         #If Chosen card is the HARD A
         if a_AI == "A":
            if total + 11 <= 21:
               a_AI = 11
               cards_AI.append(a_AI)
            elif total + 10 <= 21:
               a_AI = 10
               cards_AI.append(a_AI)
            else :
               a_AI = 1
               cards_AI.append(a_AI)
         else:
            cards_AI.append(d.get(a_AI)) 
         
    return(p_AI,total_AI,cards_AI)
    
#Choices for AI
def AI_choice(p_AI,cards_AI,total_AI):
    if total_AI < 17:
        p_AI,total_AI,cards_AI = AI_draw(p_AI,total_AI,1)
        total_AI,cards_AI = calculate_scores(total_AI,cards_AI)
        return(p_AI,total_AI,cards_AI)
    else:
        time.sleep(2)
        print("Jack Sparrow stands his deck...")
        return
        
        
        
    
    
    
    
    
    
    
    
#-------------------------------------------------------------------------------
#This Is Where The Game Begins

print("Welcome to Russian Roulette Black Jacks")
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
    time.sleep(1)
    p = 0
    p_AI = 0
    total = 0
    total_AI = 0
    cards = []
    cards_AI = []
    
    print("-----------------------------------")
    
    #player
    p,total,cards = draw(p,total,1)
    total,cards = calculate_scores(total,cards)
    p,total,cards = draw(p,total,1)
    total,cards = calculate_scores(total,cards)
    check_1(p,total)
    
    #AI
    p_AI,total_AI,cards_AI = AI_draw(p_AI,total_AI,1)
    total_AI,cards_AI = calculate_scores(total_AI,cards_AI)
    p_AI,total_AI,cards_AI = AI_draw(p_AI,total_AI,1)
    total_AI,cards_AI = calculate_scores(total_AI,cards_AI)
    
    print("-----------------------------------")
    
    for i in range (10):
        #Player
        ask_the_player(total,total_AI)
        time.sleep(2)
        p,total,cards = draw(p,total,1)
        total,cards = calculate_scores(total,cards)
        check_1(p,total)
        
        #AI
        if total_AI < 17:
            p_AI,total_AI,cards_AI = AI_draw(p_AI,total_AI,1)
            total_AI,cards_AI = calculate_scores(total_AI,cards_AI)
        else:
            time.sleep(2)
            print("Jack Sparrow stands his deck...")
    
        print("-----------------------------------")

    
    
    
    
    
       
                                      


