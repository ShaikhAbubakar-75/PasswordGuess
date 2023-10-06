import os
from random import *

My_Password = input("Enter Password Using Alphabet & Number : ")

password = ['1','2','3','4','5','6','7','8','9','0','a', 
            'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w','x','y','z']

guess = ""
while (guess != My_Password):
    guess = ""
    for letter in range(len(My_Password)):
        guess_Password = password[randint(0, 4)]
        guess = str(guess_Password) + str(guess) 
        print(guess)
        os.system("cls")

print("Your Password Is : ",guess)