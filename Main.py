import ManipulateFile
import csv

#Get the source file path
source_file_path = ManipulateFile.Select_file()

#Open stream to the source file path
source_file = ManipulateFile.Open_existing_file(source_file_path)

if source_file != None:
    with source_file as source:
        csv_reader = csv.reader(source, delimiter=';')
        line_count = 0
        for row in csv_reader:
            print(row)
else:
    print("Impossible d'ouvrir le fichier sélectionné, veuillez ré-essayer")