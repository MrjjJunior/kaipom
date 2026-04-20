"""Kule-Module ngizofaka ama-commands azosetshenziswa i-Program"""

import json
import argparse

def parsing_ama_argument():
    
    parser = argparse.ArgumentParser(description = 'Study tool that helps me study using the Pomodoro Technique') # This instantiates the ArgumentParser class
    subparsers = parser.add_subparsers(dest = 'command') # dest is where the value of the argument is found using dot notation

    # STUDY TIME (25/50)

    parser_study = subparsers.add_parser('study', help = 'Pomodoro study duration. 25 or 50.')

    parser_study.add_argument('minutes', type = int, choices = [25,50,1], help= 'Choose a study time between 25 (Minutes) or 50 (Minutes)')
    parser_study.add_argument('--hour', default = 1, type = int, choices = [1,2,3,4,5,6], help = 'How long the entire study sessions duration will be for.')

    # NOTES

    parser_notes = subparsers.add_parser('notes', help = 'Take a look at your past study notes.')

    parser_notes.add_argument('--notes', type = str, help = 'See your notes from a specific date or look at them holistically to see what you\'ve learnt.')

    args = parser.parse_args()  # creates them all for us and stores it into the args variable

    # QUIZ using RAG

    parser_notes = subparsers.add_parser('quiz', help = 'Generate a quiz based on what you\'ve learnt so far.')

    parser_notes.add_argument('--random', type = str, help = 'See your notes from a specific date or look at them holistically to see what you\'ve learnt.')

    args = parser.parse_args() 

    return args


# """Should I use OOP for this? I think so."""

# """I need to figure out a way to trigger a seperate Hour long study session in Hours, similar to the mini timer."""

# """Code to store my notes in a csv or json file. And code to load it up into my terminal."""




