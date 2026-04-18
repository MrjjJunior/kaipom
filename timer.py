import time
from datetime import datetime
import sys

def overall_study_duration_count_down(study_hour: int) -> str:

    """This is the overall BIG Clock keeping track of how long I'm studying for overall."""
    
    hours_completed = study_hour 

    study_hour = (60*60)*(study_hour) # I'm converting my hour(s) submitted into seconds.


    while study_hour:
        try:

            mins, secs = divmod(study_hour, 60) # divmod returns quotient and remainder of the division of the first argument with the second. Returns a tuple.
            hours, mins = divmod(mins, 60)
            study_timer = f'{hours:02d}:{mins:02d}:{secs:02d}'
            
            print("Time Left:",study_timer, end='\r', flush = True)  # Overwrite the line each second by putting cursor back to the beginning of the line.
            
            time.sleep(1) # Creates 1 second delay

            study_hour -= 1

        except EOFError:
            
            sys.exit(1)

    return hours_completed


def countdown_timer(t_seconds: int) -> str:

    """Count down Pomodoro section of my code"""

    t_minutes = (t_seconds * 60) # Convert the minutes I'll receive into seconds
    
    while t_minutes:
        mins, secs = divmod(t_minutes, 60) # divmod returns quotient and remainder of the division of the first argument with the second. Returns a tuple.
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        
        print(timer, end='\r')  # Overwrite the line each second by putting cursor back to the beginning of the line.
        
        time.sleep(1)

        t_minutes -= 1

    print("End of session.")
    
    notes = input("What have you learnt so far? ") # I want to store these notes in a json/ csv file. 

    return notes

# countdown_timer(int(minutes))