import re
import os

downloadFolder = 'C:\\Users\\Brian\\Downloads\\'
documentsFolder = 'C:\\Users\\Brian\\Documents\\'

#Change this to desired folder.
targetFolder = documentsFolder

FileExtRegEx = re.compile('(.*)\.(jpg|pdf|doc|docx|png|xls|xlsx|exe|zip|rar|psd|wav|msi|JPG|ttf|mp4|)$')
folderList = ['Images','Word Documents','.exe Files','Audio Files','Photoshop Files','Compressed Files','Excel Files','PDF Files']

print('Creating folder directories...\n')
for folderName in folderList:
    try:
        os.makedirs(targetFolder + folderName )
    except OSError:
        print("'" + folderName + "' exists. Will skip making folder.")
        pass
 
   
    
for file in os.listdir(targetFolder):
    mo1 = FileExtRegEx.search(file)
    if mo1 != None:
        #print(mo1.group(2))
        #Images
        if mo1.group(2) in ("png","jpg","bmp","gif","JPG"):
            print('Moving ' + file + ' to Images folder...')
            os.rename(targetFolder + file, targetFolder + "Images\\" + file)
        #Word Documents
        elif mo1.group(2) in ("doc","docx"):
            print('Moving ' + file + ' to Word Documents folder...')
            os.rename(targetFolder + file, targetFolder + "Word Documents\\" + file)
        #Exe Files
        elif mo1.group(2) in ("exe"):
            print('Moving ' + file + ' to .exe Files folder...')
            os.rename(targetFolder + file, targetFolder + ".exe Files" + file)
        #PDF
        elif mo1.group(2) in ("pdf"):
            print('Moving ' + file + ' to Word Documents folder...')
            os.rename(targetFolder + file, targetFolder + "PDF Files\\" + file)
        #Audio Files
        elif mo1.group(2) in ("wav","mp4"):
            print('Moving ' + file + ' to Audio Files folder...')
            os.rename(targetFolder + file, targetFolder + "Audio Files\\" + file)
        #Excel Files
        elif mo1.group(2) in ("xls","xlsx"):
            print('Moving ' + file + ' to Excel Files folder...')
            os.rename(targetFolder + file, targetFolder + "Excel Files\\" + file)
        #Photoshop Files
        elif mo1.group(2) in ("psd"):
            print('Moving ' + file + ' to Photoshop Files folder...')
            os.rename(targetFolder + file, targetFolder + "Photoshop Files\\" + file)
        #Compressed files
        elif mo1.group(2) in ("zip","rar"):
            print('Moving ' + file + ' to Compressed Files folder...')
            os.rename(targetFolder + file, targetFolder + "Compressed Files\\" + file)
        
            

print()
print('This folder contains ' + str(len(os.listdir(targetFolder))) + ' Items.')