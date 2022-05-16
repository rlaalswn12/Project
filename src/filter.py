import os

arr = os.listdir("C:/Users\82109\PycharmProjects\Project_B2\Project_B2\data")


def call_dir(tag, caller):
    fileName = []
    for (root, dirs, file) in os.walk("C:/Users\82109\PycharmProjects\Project_B2\Project_B2\data"):
        for f in file:
            now = str(f)
            if now.find(caller) != -1:
                fileName.append(str(root) + '\\' + now)

    newFileName = []
    for fname in fileName:
        if fname.find(tag) != -1:
            newFileName.append(fname)
    return newFileName
