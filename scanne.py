import os


def getAllFileFromDirectory(directory, temp):
    try:
        files = os.listdir(directory)
        for file in files:
            if (os.path.isdir(directory + file)):
                if file[0] == '.': continue  # i added this because i'm on a UNIX system

                print(directory + file)
                getAllFileFromDirectory(directory + file, temp)
            elif (os.path.isfile(directory + file) and os.path.getsize(directory + file) > 35000000):
                temp.write(os.path.abspath(file))

    except Exception:
        print("denied")


def getFilesOutOfTheLimit():
    basePath = "/"
    tempFile = open('temp.txt', 'w')

    getAllFileFromDirectory(basePath, tempFile)
    tempFile.close()
    print("Get all files ... Done !")


getFilesOutOfTheLimit()

