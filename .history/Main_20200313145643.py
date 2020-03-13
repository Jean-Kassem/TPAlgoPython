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
out_error_lines = []
# brand = ""
model = ""
type = ""
count = 0

if source_file != None:
    with source_file as source:
        csv_reader = csv.reader(source, delimiter=';')
        for row in csv_reader:
            source_lines.append(LineSource(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))

        if len(source_lines) < 5:
            print("Le fichier sélectionné contient trop peu de lignes pour être utilisé")
        else:
            for line in source_lines:
                if line.is_empty == False:
                    if line.is_title:
                        if Contain_type(line.designation):
                            type = Upper_first_letter_word(Get_type(line.designation))
                        if Contain_model(line.designation) and (source_lines[count+1].is_empty == False and source_lines[count+1].is_title == False) and source_lines[count-1].is_empty == True:
                            model = Upper_first_letter_word(Get_model(line.designation))
                    else:
                        out = Out(line.reference_client, line.reference_sap, line.designation + " " + str(line.capacity), line.capacity, line.cnt_product_pack, line.barcode, line.buy_price, line.sell_price, type, model, "test")
            if out.is_ok:
                print(out)
                count += 1
            

else:
    print("Impossible d'ouvrir le fichier sélectionné, veuillez ré-essayer")

# def Is_brand(index_line, lines):
#     return False

def Contain_type(value = ""):
    result = False
    checks = ["Eau de ","eau de ","EAU DE ","Eau De "]
    index = -1

    for check in checks:
        index = value.find(check)
        if index >= 0:
            if (len(value) - index) >= 3:
                result = True
                break

    return result

def Get_type(value):
    index = value.find("-")

    if index > -1:
        if index+1 < len(value):
            value = value[index+1:len(value)]
        else:
            value.replace("-", "")

    return value.strip()

def Contain_model(value):
    result = True
    checks = ["Eau de ","eau de ","EAU DE ","Eau De "]
    test_value = value.replace(" ","").replace("-","")
    index = -1

    for check in checks:
        index = test_value.find(check)
        if index >= 0:
            if len(test_value) - (len(test_value) - index) <= 0:
                result = False
                break

    return result

def Get_model(value):
    index = value.find("-")
    checks = ["Eau de ","eau de ","EAU DE ","Eau De "]
    test_value = value.replace("-", "")

    for check in checks:
        index = test_value.find(check)
        if index >= 0:
            test_value = test_value[0,index]

    return test_value.strip()

def Upper_first_letter_word(value):
    need_upper = True
    result = ""

    for char in value:
        if char.isalpha():
            if need_upper:
                result.__add__(char.upper())
                need_upper = False
            else:
                result.__add__(char.lower())
        elif char == " ":
            need_upper = True
            result.__add__(char)
        else:
            result.__add__(char)

    return result