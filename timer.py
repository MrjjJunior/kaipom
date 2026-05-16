import time
from tqdm import trange # tqdm stands for progress in arabic
from rich.progress import Progress, track
from rich import print
from rich.markdown import Markdown
from rich.console import Console
from rich.progress import BarColumn,TimeRemainingColumn
console = Console() # rich library to make your text output be colourful

class Timer:

    def __init__(self, total_duration_of_study_session, pomodoro_duration):
        self.total_duration_of_study_session = total_duration_of_study_session
        self.pomodoro_duration = pomodoro_duration

    
    def study_countdown(self):
            
        start = time.monotonic() 

        print("Time left: ") 

        try: 
            total_study_session_hours = (self.total_duration_of_study_session*60*60) #Total study duration in seconds

            pomodoro_minutes_in_seconds = (self.pomodoro_duration * 60) 
        except ValueError:
            print("Only integers are allowed!")
        

        # The progress bar
        with Progress(BarColumn(), TimeRemainingColumn()) as progress: # "With" closes the progress bar automatically once done

            study_session = progress.add_task( total = pomodoro_minutes_in_seconds,description= "Pomodoro in session",)
            
            while True:
                elapsed_time = time.monotonic() - start # Calculates how many seconds it has been
                if (elapsed_time >= pomodoro_minutes_in_seconds):
                    progress.update(study_session, completed = pomodoro_minutes_in_seconds) 
                    break
                
                progress.update(study_session, completed = elapsed_time)
                time.sleep(0.1)      
                

        console.print("End of session. ") 
        print("")
        
        notes = input("What have you learnt/done so far? ")  # I want to store these notes in a json/ csv file. 
        print("")
        return notes 
        

    def break_countdown(self):

        if (self.pomodoro_duration == 25):
            study_break = 5*60 # converting min to seconds
        else:
            study_break = 10*60 # converting min to seconds

        start_break = time.monotonic()

        print("Break:") 

        try:
            with Progress(BarColumn(),TimeRemainingColumn()) as progress_break: # With will close the progress bar once I'm done with it automatically

                break_session = progress_break.add_task(description= "Break in progress", total=study_break)
                
                while True:
                    elapsed_time = time.monotonic() - start_break # How many seconds has it been?
                    if (elapsed_time >= study_break):
                        progress_break.update( break_session, completed = study_break) 
                        break
                    
                    progress_break.update(break_session, completed=elapsed_time)
                    time.sleep(0.1)   

            console.print(f"Goodbye!")   
            
        except EOFError:
            console.print("You've terminated your break. Goodbye!")
        