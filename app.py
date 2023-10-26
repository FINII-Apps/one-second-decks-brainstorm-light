import config as config

from pres import Deliverable
from ki import functions as ki_f

import os
import random

# pip3 install playsound==1.2.2
# pip3 install openai python-dotenv python-pptx



def chooseRandomPicture():

    # Verzeichnis, in dem die Bilder gespeichert sind
    verzeichnis = f"{config.userfolder_path}img/random"

    # Liste aller Dateien im Verzeichnis
    dateien = os.listdir(verzeichnis)

    # Filtere nur die Bilddateien (z.B. JPG, PNG)
    bildendungen = ['.jpg', '.jpeg', '.png', '.gif']  # Füge weitere Endungen hinzu, wenn nötig
    bilddateien = [datei for datei in dateien if any(datei.endswith(endung) for endung in bildendungen)]

    # Wenn keine Bilder im Verzeichnis gefunden wurden, breche ab
    if not bilddateien:
        print("Keine Bilder im Verzeichnis gefunden.")
    else:
        # Zufällig ein Bild auswählen
        zufalliges_bild = random.choice(bilddateien)
        #print("Zufällig ausgewähltes Bild: ", zufalliges_bild)

    return zufalliges_bild



if __name__ == "__main__":

    try:

        config_list = []

        with open(f"{config.userfolder_path}config.py", "r") as file:
            lines = file.readlines()

        for line in lines:
            if "=" in line and "ki_request" in line:
                var_name = line.split("=")[0].strip()
                config_list.append(var_name)
                
        anzahl_eintraege = len(config_list)
        print(f"Die Anzahl der Einträge in der Liste beträgt: {anzahl_eintraege}")
        
        for config_variable in config_list:
            exec(f"{config_variable} = ki_f.initOpenAI(config.{config_variable})")

    finally: 
        
        print("KI done")
                
        report = Deliverable.OneSecondDeck(config.output_file, config.output_folder, config.input_file, config.input_folder)

    # SLIDE 1
    try:
    
        #abschnitte = report_explainer.split('\n\n')

        slide = 1 # Verwendeter Master-Slide: Drei Inhalte
        report.insertTextOnSlide(f"Brainstorm", slide, "Titel 1")
        
        #report.insertTextOnSlide(f"Was die App dir abnimmt:\n{content[0]}", slide, "Inhaltsplatzhalter 4")
        #report.writeNotes(f"Markt:\n{ki_request_007}", slide)
        #report.insertImageOnSlide(f'{config.userfolder_path}img/random/{chooseRandomPicture()}', slide, 'Titel 1', 0, 0, 33.87, 19.05, True)

    finally: 
        print(f"#### Slide {slide} done ####")

    # SLIDE 2
    try:
    
        #abschnitte = report_explainer.split('\n\n')

        slide = 2 # Verwendeter Master-Slide: Drei Inhalte

        content = ki_request_002.splitlines()
        content = [element for element in content if element != '']
        content = [element for element in content if element != ':']
        print(content)
        
        introduction = "Starbursting ist eine Methode des klassischen Brainstormings, bei der eine zentrale Idee in die Mitte eines Whiteboards geschrieben wird, um die herum ein sechseckiger Stern gezeichnet wird. Jede Spitze des Sterns repräsentiert eine der W-Fragen: Wer, Was, Wann, Wo, Warum und Wie. Diese Fragen werden verwendet, um die Idee aus verschiedenen Perspektiven zu betrachten und mögliche Anwendungen zu erforschen. Dies hilft, Szenarien zu erkunden und unerwartete Hindernisse aufzudecken. Starbursting eignet sich besonders gut für Brainstorming in großen Gruppen und eine gründliche Überprüfung von Ideen."
        
        report.insertTextOnSlide(f"Tipp", slide, "Titel 3")
        report.insertTextOnSlide(f"{introduction}", slide, "Inhaltsplatzhalter 4")
        #report.writeNotes(f"Markt:\n{ki_request_007}", slide)
        report.insertImageOnSlide(f'{config.userfolder_path}img/random/{chooseRandomPicture()}', slide, 'Titel 1', 17, 7, 11, 6.5, True) if config.background_fix == 1 else None


    finally: 
        print(f"#### Slide {slide} done ####")

    # ALL OTHER SLIDES
    try:
    
        #abschnitte = report_explainer.split('\n\n')

        slide = 3 # Verwendeter Master-Slide: Drei Inhalte
        report.insertTextOnSlide(f"{content[1]}", slide, "Titel 1")
        report.insertTextOnSlide(f"Ansatz {slide}", slide, "Textplatzhalter 2")
        #report.writeNotes(f"Markt:\n{ki_request_007}", slide)
        report.insertImageOnSlide(f'{config.userfolder_path}img/random/{chooseRandomPicture()}', slide, 'Titel 1', 17, 7, 11, 6.5, True) if config.background_fix == 1 else None

        slide = 4 # Verwendeter Master-Slide: Drei Inhalte
        report.insertTextOnSlide(f"{content[2]}", slide, "Titel 1")
        report.insertTextOnSlide(f"Ansatz {slide}", slide, "Textplatzhalter 2")
        #report.writeNotes(f"Markt:\n{ki_request_007}", slide)
        report.insertImageOnSlide(f'{config.userfolder_path}img/random/{chooseRandomPicture()}', slide, 'Titel 1', 17, 7, 11, 6.5, True) if config.background_fix == 1 else None

        slide = 5 # Verwendeter Master-Slide: Drei Inhalte    
        report.insertTextOnSlide(f"{content[3]}", slide, "Titel 1")
        report.insertTextOnSlide(f"Ansatz {slide}", slide, "Textplatzhalter 2")
        #report.writeNotes(f"Markt:\n{ki_request_007}", slide)
        report.insertImageOnSlide(f'{config.userfolder_path}img/random/{chooseRandomPicture()}', slide, 'Titel 1', 17, 7, 11, 6.5, True) if config.background_fix == 1 else None

        slide = 6 # Verwendeter Master-Slide: Drei Inhalte    
        report.insertTextOnSlide(f"{content[4]}", slide, "Titel 1")
        report.insertTextOnSlide(f"Ansatz {slide}", slide, "Textplatzhalter 2")
        #report.writeNotes(f"Markt:\n{ki_request_007}", slide)
        report.insertImageOnSlide(f'{config.userfolder_path}img/random/{chooseRandomPicture()}', slide, 'Titel 1', 17, 7, 11, 6.5, True) if config.background_fix == 1 else None

        slide = 7 # Verwendeter Master-Slide: Drei Inhalte    
        report.insertTextOnSlide(f"{content[5]}", slide, "Titel 1")
        report.insertTextOnSlide(f"Ansatz {slide}", slide, "Textplatzhalter 2")
        #report.writeNotes(f"Markt:\n{ki_request_007}", slide)
        report.insertImageOnSlide(f'{config.userfolder_path}img/random/{chooseRandomPicture()}', slide, 'Titel 1', 17, 7, 11, 6.5, True) if config.background_fix == 1 else None

        slide = 8 # Verwendeter Master-Slide: Drei Inhalte    
        report.insertTextOnSlide(f"{content[6]}", slide, "Titel 1")
        report.insertTextOnSlide(f"Ansatz {slide}", slide, "Textplatzhalter 2")
        #report.writeNotes(f"Markt:\n{ki_request_007}", slide)
        report.insertImageOnSlide(f'{config.userfolder_path}img/random/{chooseRandomPicture()}', slide, 'Titel 1', 17, 7, 11, 6.5, True) if config.background_fix == 1 else None

        slide = 9 # Verwendeter Master-Slide: Drei Inhalte    
        report.insertTextOnSlide(f"{content[7]}", slide, "Titel 1")
        report.insertTextOnSlide(f"Ansatz {slide}", slide, "Textplatzhalter 2")
        #report.writeNotes(f"Markt:\n{ki_request_007}", slide)
        report.insertImageOnSlide(f'{config.userfolder_path}img/random/{chooseRandomPicture()}', slide, 'Titel 1', 17, 7, 11, 6.5, True) if config.background_fix == 1 else None
        
        slide = 10 # Verwendeter Master-Slide: Drei Inhalte    
        report.insertTextOnSlide(f"{content[8]}", slide, "Titel 1")
        report.insertTextOnSlide(f"Ansatz {slide}", slide, "Textplatzhalter 2")
        #report.writeNotes(f"Markt:\n{ki_request_007}", slide)
        report.insertImageOnSlide(f'{config.userfolder_path}img/random/{chooseRandomPicture()}', slide, 'Titel 1', 17, 7, 11, 6.5, True) if config.background_fix == 1 else None


    finally: 
        print(f"#### Slide {slide} done ####")

    report.createPres()
