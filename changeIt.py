#!/usr/bin/python

import os
import sys

# Define hybris original names
# hybris IMAGES
# hybrisImagePath=/home/natanael/1-hybris/hybrisTest16400/hybris/bin/ext-data/electronicsstore/resources/electronicsstore/import/sampledata/productCatalogs/electronicsProductCatalog/images/30Wx30H/
#hybrisImagePath = 'C:\\dev\\projects\\sap\\commerce\\y-acc-b2c-6.5\\hybris\\bin\\ext-data\\electronicsstore\\resources\\electronicsstore\\import\\sampledata\\productCatalogs\\electronicsProductCatalog\\images\\30Wx30H'

# Creating the new folders
folderSize30='generatedImages\\30Wx30H'
folderSize65='generatedImages\\65Wx65H'
folderSize95='generatedImages\\96Wx95H'
folderSize300='generatedImages\\300Wx300H'
folderSize515='generatedImages\\515Wx515H'
folderSize1200='generatedImages\\1200Wx1200H'

sourceFolder = 'sourceImages'

def getResizeCommand (pathSourceFile, sourceFileName, targetFileName, size):
    executeCommand = None
    if (size == 30):
        executeCommand = 'magick ' + pathSourceFile + '\\' + sourceFileName + ' -resize x30 ' + folderSize30 + '\\' + targetFileName
    elif (size == 65):
        executeCommand = 'magick ' + pathSourceFile + '\\' + sourceFileName + ' -resize x65 ' + folderSize65 + '\\' + targetFileName
    elif (size == 95):
        executeCommand = 'magick ' + pathSourceFile + '\\' + sourceFileName + ' -resize x95 ' + folderSize95 + '\\' + targetFileName
    elif (size == 300):
        executeCommand = 'magick ' + pathSourceFile + '\\' + sourceFileName + ' -resize x300 ' + folderSize300 + '\\' + targetFileName
    elif (size == 515):
        executeCommand = 'magick ' + pathSourceFile + '\\' + sourceFileName + ' -resize x515 ' + folderSize515 + '\\' + targetFileName
    elif (size == 1200):
        executeCommand = 'magick ' + pathSourceFile + '\\' + sourceFileName + ' -resize x1200 ' + folderSize1200 + '\\' + targetFileName
    return executeCommand



def createFolders():
    if not os.path.exists(folderSize30):
        os.makedirs(folderSize30)
    if not os.path.exists(folderSize65):
        os.makedirs(folderSize65)
    if not os.path.exists(folderSize95):
        os.makedirs(folderSize95)
    if not os.path.exists(folderSize300):
        os.makedirs(folderSize300)
    if not os.path.exists(folderSize515):
        os.makedirs(folderSize515)
    if not os.path.exists(folderSize1200):
        os.makedirs(folderSize1200)

def executeWholeProcess():
    try:

        print('Starting the process...')

        try:
            hybrisImagePath = sys.argv[1]
        except IndexError:
            print('Error! Please check the argument, Hybris products images folder is incorrect !')
            exit()

        sourceImages = os.listdir(sourceFolder)

        totalSourceFiles = len(sourceImages)

        print('Quantity of Source Images: ' + str(totalSourceFiles))

        count = 0

        for fileName in os.listdir(hybrisImagePath):

           print('Source Image File: ' + sourceImages[count])
           print('Hybris File Name: ' + fileName)


           executeCommand = getResizeCommand(sourceFolder, sourceImages[count], fileName, 30)
           os.system(executeCommand)

           executeCommand = getResizeCommand(sourceFolder, sourceImages[count], fileName, 65)
           os.system(executeCommand)

           executeCommand = getResizeCommand(sourceFolder, sourceImages[count], fileName, 95)
           os.system(executeCommand)

           executeCommand = getResizeCommand(sourceFolder, sourceImages[count], fileName, 300)
           os.system(executeCommand)

           executeCommand = getResizeCommand(sourceFolder, sourceImages[count], fileName, 515)
           os.system(executeCommand)

           executeCommand = getResizeCommand(sourceFolder, sourceImages[count], fileName, 1200)
           os.system(executeCommand)

           print('Changed with SUCCESS!')

           if (count < totalSourceFiles-1):
               count += 1
           else:
               count = 0

        print('Process finished!!!')
    except BaseException:
        print('Process finalized with Errors')
        exit()



createFolders()
executeWholeProcess()