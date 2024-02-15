from PIL import Image
import os


def checkInFolder(dirIn):
    if not os.path.exists(dirIn):
        print(f'Folder: {dirIn} does not exist.\n')
        quit()


def checkIfEmpty(dirIn):
    if not os.listdir(dirIn):
        print('Your ' + dirIn + ' folder is empty. \n')
        quit()


def createOutFolder(dirOut):
    if not os.path.exists(dirOut):
        os.makedirs(dirOut)


def resizeImages(dirIn, dirOut, pixel1, pixel2):
    print("\nResizing images... \n")
    for filename in os.listdir(dirIn):
        img = Image.open(f"{dirIn}/{filename}")
        new_img = img.resize((int(pixel1), int(pixel2)))
        new_img.save(f'{dirOut}/{filename[:-4]}_{pixel1}x{pixel2}.jpg')
        print(filename + ' resized to ' + str(pixel1) + 'x' + str(pixel2) + ' successfully \n')
    print('All images resized successfully')


# Paths
path = input('Enter your images folder name: ')

checkInFolder(path)
checkIfEmpty(path)

pathOut = './' + path + '_resized'

firstParam = input('Enter desired 1st pixel parameter : ')
secondParam = input('Enter desired 2nd pixel parameter: ')

createOutFolder(pathOut)
resizeImages(path, pathOut, firstParam, secondParam)
