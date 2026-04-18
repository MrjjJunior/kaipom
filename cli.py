"""Kule Module ngizofaka ama-commands azosetshenziswa i-Program"""

import json
import time
from argparse import ArgumentParser

# parser = ArgumentParser(description='Helps you study using the pomodoro technique') # This instantiates the ArgumentParser class

# e.g Input
# Pomodoro session 25/5 or 50/ 10 
# For How long: 50 Min, 1 Hour, 4 Hours etc.

# parser.add_argument('study', metavar='study', type = str, help ='Enter your study time') # This is a positional argument. Optional arguments are declared with (- or --)
# parser.add_argument('notes', metavar='recap', type = str, help ='See your notes')
# parser.add_argument('notes', metavar='recap', type = str, help ='See your notes')

# I might need to add subcommands.


# parser.add_subparsers()

# args = parser.parse_args() 

# study = args.study


# print(f"You're studying for {study}")
# print("Time on the clock: \n24:59")

while True:
    print("Welcome to KaiPom: Enter your pomodoro study method duration: ")
    user_pom= input("Format (mm/mm): ")
    try:
        minutes, minutes_break = user_pom.split("/")
        minutes  = (int(minutes)*60)
        minutes_break = int(minutes_break)
    except ValueError:
        print("Please use the format mm/mm.")
    try:
        user_duration = int(input("How many hour(s)?: "))
        break
    except ValueError:
        print("Please use numbers only.")



def countdown_timer(t_seconds):
    """Count down section of my code"""
    while t_seconds:
        mins, secs = divmod(t_seconds, 60) # divmod returns quotient and remainder of the division of the first argument with the second in a tuple.
        timer = '{:02}d:{:02d}'.format(mins, secs)
        
        print(timer, end='\r')  # Overwrite the line each second by putting cursor back to the beginning of the line.
        
        time.sleep(1)

        t_seconds -= 1

    print("End of first session: ")

    notes = input("What have you learnt so far? ") # I want to store these notes in a json/ csv file. 

countdown_timer(int(minutes))

"""Should I use OOP for this? I think so."""

"""I need to figure out a way to trigger a seperate Hour long study session in Hours, similar to the mini timer."""

"""Code to store my notes in a csv or json file. And code to load it up into my terminal."""




