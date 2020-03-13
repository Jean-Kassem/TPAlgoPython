import ManipulateFile
from LineSource import LineSource
from Out import Out
import csv

#Get the source file path
source_file_path = ManipulateFile.Select_file()

#Open stream to the source file path
source_file = ManipulateFile.Open_existing_file(source_file_path)
source_lines = []
out_lines = []

if source_file != None:
    with source_file as source:
        csv_reader = csv.reader(source, delimiter=';')
        line_count = 0
        for row in csv_reader:
            source_lines.append(LineSource(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
        
        for source_line in source_lines:
            sl = source_line
            out = Out(sl.reference_client, sl.reference_sap, sl.designation + " " + sl.capacity, sl.capacity, sl.cnt_product_pack, sl.barcode, sl.buy_price, sl.sell_price, "test", "test", "test")
            if out.is_ok:
                print(out)

else:
    print("Impossible d'ouvrir le fichier sélectionné, veuillez ré-essayer")