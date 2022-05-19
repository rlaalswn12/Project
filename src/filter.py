import os

arr = os.listdir("../data")


def call_dir(tag, caller):
    fileName = []
    for (root, dirs, file) in os.walk("../data"):
        for f in file:
            now = str(f)
            if now.find(caller) != -1:
                fileName.append(str(root) + '\\' + now)

    newFileName = []
    for fname in fileName:
        if fname.find(tag) != -1:
            newFileName.append(fname)
    return newFileName
