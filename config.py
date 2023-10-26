project = "brainstorm"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Design

background_fix = 1
background_picture = "Wiretap.jpg"

title_fix = 1
title_picture = "Wiretap.jpg"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# AI prompts


zielgruppe = "firmen die produkte haben"
branche = "b2b"

userjob = "grassroot automation"
problem1 = "viel data work"
problem2 = "stress in der agentur"
problem3 = "technische welt"
job_outcome = "new clients"

feature1 = "automation"
feature2 = "apps"
feature3 = "code"
brand_edge = "kreativität"


ki_request_001 = f"du hast ein produkt entwickelt und willst es einem potentiellen kunden beschreiben. der kunde will {userjob} aber hat drei probleme: {problem1}, {problem2}, {problem3}. als lösung bietet das produkt: {feature1}, {feature2}, {feature3} an um {job_outcome}. Beschreibe mir 1. was das produkt dem kunden abnimmt, 2. wie das produkt dies macht (gib auch ein beispiel) und 3. welche technischen komponenten das produkt haben muss. Schreibe den text einfach wie für einen fünfjährigen in kurzen worten aber mindestens 40 worte pro punkt. teile es in 3 punkte (1., 2., 3.)"
ki_request_002 = f"Du führst eine marke, die hilft bei {problem1}, {problem2}, {problem3} und {job_outcome}. Liste mir 10 einzigartige und kreative Kampagnenansätze"


# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# File Paths

title = "1 Second Deck – Powerpoint App"

userfolder_path = "" 

# Pfad zum Eingangsordner (masters) und zur Eingabe-Datei (Master.pptx)
input_folder = f"{userfolder_path}masters"
input_file = f"{project}.pptx"

# Pfad zum Ausgabeordner (output) und zum Ausgabe-Dateinamen
output_folder = f"{userfolder_path}output"
output_file = f"{project}_edited.pptx"

img_folder = f"{userfolder_path}img/"

