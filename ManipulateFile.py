import io
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#Create a new file, return True if it succeed, else return False
def Create_new_file(path):
    result = False
    try:
        f = io.FileIO(path)
        f.close()
    except IOError:
        if (open(path, "x") != None):
            result = True
    finally:
        return result


#Open a file and return the opened reading stream, if file can't be opened return null
def Open_existing_file(path):
    try:
        f = open(path, "r")
    except IOError:
        f = None
    finally:
        return f

#Write a new line in the file, return True if it succeed, else return false
def Write_new_line(path, line):
    try:
        f = open(path, "a+")
        f.write(line)
        f.close()
        return True
    except IOError:
        return False

def Select_file():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()
    return filename