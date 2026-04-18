"""Lena iMain file yam' essentially and is where everything will run."""
from cli import parsing_ama_argument
from timer import countdown_timer, overall_study_duration_count_down
from datetime import datetime
import json
import os
import time

def main():
    
    namhlanje = date_formatter() # I'll use this date to later catalogue in my json file
    manje = datetime.now()

    args = parsing_ama_argument()
    start_time = manje.strftime("%R") # %R Shorthand for digital format.


    if args.command == 'study':
        print("")
        print(f"Pomodoro: {args.minutes} minutes") 
        print(f"Total Session: {args.hour} hour(s)")
    
        if args.minutes != "25":
            print(f"Break duration: 10 Minutes")
        else:
             print(f"Break duration: 5 Minutes")
        
        print("")
   
        time.sleep(2) # Adds 3 second delay to prep.

        while True:

            """Main Clock Loop"""
            
            big_clock = overall_study_duration_count_down(args.hour)

            notes = countdown_timer(args.minutes)
            session = {"date": str(namhlanje), "study_duration": f"{args.minutes} minute", "start_time": start_time, "notes": notes}
            uniq_json = f"{namhlanje}"

            with open(f"/Users/amahlecele/Desktop/kaipom/notes/{uniq_json}-{start_time}.json", "w") as file: # Storing the files in the notes folder
                json.dump(session, file)

                break
        
        return f"Session over :)"
    else:
         return f":("


def date_formatter():
    "Formats todays date and time into a prettier, more legible format."

    namhlanje = datetime.today()
    return f"{namhlanje.strftime("%d-%B-%Y")}"
        


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()