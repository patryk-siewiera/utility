import os
import shutil


def createFolderIfNotExist(pathToNewFolder):
    try:
        os.stat(pathToNewFolder)
        print("\n-- Folder already exist,  \n\t", pathToNewFolder, "\n")
    except:
        os.mkdir(pathToNewFolder)
        print("\n++ Folder created! \n\t", pathToNewFolder, "\n")


def filterArray(array, keyWord):
    array = [each_string.lower() for each_string in array]
    keyWord = [each_keyword.lower() for each_keyword in keyWord]
    for key in keyWord:
        print(key,array)
        array = [item for item in array if key in item]
    return array


def copyAllFiles(origin, destination, keyWord):
    arrayAllFiles = (os.listdir(origin))
    arrayAllFiles = filterArray(arrayAllFiles, keyWord)
    print(arrayAllFiles)
    for fileName in arrayAllFiles:
        fullFileName = os.path.join(origin, fileName)
        if os.walk(fullFileName):
            shutil.copy(fullFileName, destination)


# ### TO EDIT
origin = r"C:\Users\sievr\Downloads\KKCE\wnioski materiałowe\CE" # where to search
newFolderName = "webopt_kopia2"
destination = r"C:\Users\sievr\Downloads\KKCE\solution\here_paste_solutions\\" + newFolderName # where copy results
keyWord = ["CE"]

createFolderIfNotExist(destination)
copyAllFiles(origin, destination, keyWord)
# #### END OF EDITS

#TODO: load excel
# from openpyxl import load_workbook
# import os
# import glob
#
# #uzupełnianie excela
# wb = load_workbook('ExcelData.xlsx')
# sheet = wb.active
#
# lastRow = sheet.max_row
# for row in sheet.iter_rows(min_row=1, min_col=1, max_row=lastRow, max_col=2):
#     for cell in row:
#         el = cell.value
#         print(el )