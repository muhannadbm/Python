"""
A simple die roller

Author: Muhannad Bani almarje
Date: November 30, 2020
"""
import random
first= input("Type the first number: ")
last= input("Type the last number: ")
roll = random.randint(int(first),int(last))
print('Choosing a number between '+ str(first)+' and '+str(last)+ '.')
print('The number is '+ str(roll)+'.')