from pathlib import Path
import json
from rich.markdown import Markdown
from rich.console import Console
console =  Console()

# Gives the home directory of the os
home_dir = Path.home()

class Notes:

    def __init__(self):
        pass
    
    def get_all_notes(self):

        """This method displays all of the study notes for each session."""
        
        print("")
        heading = """# Study Log """

        heading = Markdown(heading)
        console.print(heading)

        # Where the notes will be stored
        notes_directory = home_dir /'Desktop/kaipom/notes'

        for file in notes_directory.iterdir():

            with open(f"{str(file)}","r") as f:
                data = json.load(f)

                for k,v in data.items(): 
        
                    if k == "notes":
                        console.print(f"+ {k.title()}:\n", end = " ")
                        print("")
                        sentence = v.split(" ")
                        count = 0

                        for word in sentence:
                
                            if count < 15:
                                console.print(word, end = " ")
                                count += 1 
                            else: 
                                print("") 
                                console.print(word, end = " ")

                                count = 0  
                                count+=1        
                                    
                    elif k == "date":
                        date_pretty = v.split("-")
                        date_pretty = " ".join(date_pretty)

                        console.print(f"+ {k.title()}: {date_pretty}")
                    else:
                        console.print(f"+ {k.title()}: ", v)
                        
            ln = "_"
            print(f"\n{ln*108}")
            print(f"{ln*108}")
            print("")
