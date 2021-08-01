import os
import shutil


def app():
    # EDIT ME
    origin = r"C:\Users\sievr\Downloads\KKCE\wnioski materiałowe\CE"  # where to search
    newFolderName = "webopt_kopia3"
    keyWord = ["ce"]
    destination = r"C:\Users\sievr\Downloads\KKCE\solution\here_paste_solutions\\" + newFolderName  # where copy results

    # --------------------------------
    readAndPrintInitValues(origin, newFolderName, destination, keyWord)
    createFolderIfNotExist(destination)
    copyAllFiles(origin, destination, keyWord)


def readAndPrintInitValues(origin, newFolderName, destination, keyWord):
    print("\n*** YOUR VALUES ***")
    print("*** source folder\n\t" + origin)
    print("*** destination\n\t" + destination)
    print("*** New folder name\n\t" + newFolderName)
    print("*** Search by this Keywords")
    for key in keyWord:
        print("\t - " + key)
    print("\n")


def createFolderIfNotExist(pathToNewFolder):
    try:
        os.stat(pathToNewFolder)
        print("\n-- Folder already exist,  \n\t", pathToNewFolder, "\n")
    except:
        os.mkdir(pathToNewFolder)
        print("\n++ Folder created! \n\t", pathToNewFolder, "\n")


def filterArray(array, keyWord):
    # array and keywords will be reduced to lowercase
    array = [each_string.lower() for each_string in array]
    keyWord = [each_keyword.lower() for each_keyword in keyWord]
    for key in keyWord:
        array = [item for item in array if key in item]
    return array


def copyAllFiles(origin, destination, keyWord):
    arrayAllFiles = (os.listdir(origin))
    arrayAllFiles = filterArray(arrayAllFiles, keyWord)

    if len(arrayAllFiles) == 0:
        return print("-- Files not found: \n\tempty list")
    print("++ Files found: \t")
    for fileName in arrayAllFiles:
        print("\t" + fileName)
        fullFileName = os.path.join(origin, fileName)
        if os.walk(fullFileName):
            shutil.copy(fullFileName, destination)
    print("\n++ Files copied successfully ")


# app()

from openpyxl import load_workbook
import os
import glob

#uzupełnianie excela
wb = load_workbook('excelData.xlsx')
sheet = wb.active

lastRow = sheet.max_row
for row in sheet.iter_rows(min_row=1, min_col=1, max_row=lastRow, max_col=3):
    # print(row)
    for cell in row:
        el = cell.value
        print(el)
