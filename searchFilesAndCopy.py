import shutil
from openpyxl import load_workbook
import os
import glob
from datetime import datetime


def app():
    # *********** EDIT ME
    searchFolder = r"C:\Users\sievr\Downloads\KKCE\wnioski materiałowe"
    newFolderName = "1.2"
    keyWords = ["kk"]
    xlsName = "excelData.xlsx"
    excelMaxColumn = 3
    excelMaxRow = 5
    destinationPath = r"C:\Users\sievr\Downloads\KKCE\solution\here_paste_solutions"

    # --------------------------------
    searchSubfolders = "\**"
    origin = searchFolder + searchSubfolders
    destination = os.path.join(destinationPath, nowCurrentTime())

    readAndPrintInitValues(origin, newFolderName, destination, keyWords, xlsName, excelMaxColumn, excelMaxRow)
    xls = readXLSandReturnListOfElements(xlsName, excelMaxColumn, excelMaxRow)
    manipulateXls(xls, destination, origin)


def manipulateXls(xls, destination, origin):
    for item in xls:
        folderName = item[0]
        keywordsTemp = item[1:]
        destinationTemp = (os.path.join(destination, folderName))
        copyAllFiles(origin, destinationTemp, keywordsTemp)


def nowCurrentTime():
    nowTime = datetime.now()
    nowTime = nowTime.strftime("%Y-%m-%d__%H-%M-%S")
    return str(nowTime)


def readAndPrintInitValues(origin, newFolderName, destination, keyWords, xlsName, excelMaxColumn, excelMaxRow):
    print("\n*** YOUR VALUES ***")
    print(
        "*** Excel filename\n\t" + xlsName + " \t\t[MAX_columns: " + str(excelMaxColumn) + ", MAX_rows: " + str(
            excelMaxRow) + "]")
    print("*** source folder\n\t" + origin)
    print("*** destination\n\t" + destination)
    print("*** New folder name\n\t" + newFolderName)
    print("*** Search by this keyWords")
    for key in keyWords:
        print("\t - " + key)
    print("\n")


def readXLSandReturnListOfElements(xlsName, excelMaxColumn, excelMaxRow):
    wb = load_workbook(xlsName)
    sheet = wb.active
    rows_iter = sheet.iter_rows(max_col=excelMaxColumn, max_row=excelMaxRow)
    allValuesFromXLS = [[cell.value for cell in list(row)] for row in rows_iter]
    return allValuesFromXLS


def createFolderIfNotExist(pathToNewFolder):
    if not os.path.exists(pathToNewFolder):
        os.makedirs(pathToNewFolder)
        print("\n++ Folders created! \n\t", pathToNewFolder, "\n")
    else:
        print("\n-- Folder already exist,  \n\t", pathToNewFolder, "\n")


def filterArray(array, keyWords, path):
    # array and keyWordss will be reduced to lowercase
    array = [each_string.lower() for each_string in array]
    keyWords = [each_keyWords.lower() for each_keyWords in keyWords]
    for key in keyWords:
        array = [item for item in array if key in item]
    if len(array) == 0 or not os.path.isfile(path):
        return False
    else:
        return True


def copyAllFiles(origin, destination, keyWords):
    listOfAllFilesFullPath = []
    print("------ KEYWORDS", keyWords)
    print("++ Files found: \t")
    for f in glob.glob(origin, recursive=True):
        if (filterArray([os.path.basename(f)], keyWords, f)):
            listOfAllFilesFullPath.append(f)
            print("\t" + os.path.basename(f))
    if (len(listOfAllFilesFullPath) == 0):
        print("\t-- !! -- \t List is empty\n\n\n")
        return False

    try:
        createFolderIfNotExist(destination)
        for fileName in listOfAllFilesFullPath:
            if os.walk(fileName):
                shutil.copy(fileName, destination)
        print("++ Files copied successfully \n\n\n")
    except:
        print("\n--!!!--\t Fail during copying files")


app()
