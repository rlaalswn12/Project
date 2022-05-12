import os

lot_id = []
wafer_id = []
device_id = []

print('Input lot_id:')

# input
lot_id = input()

print('Input wafer_id:')

# input
wafer_id = input()

print('Input device_id:')

# input
device_id = input()


rootDir = 'dat/HY202103'
for subdir, dirs, files in os.walk(rootDir):
    for file in files:
        directory_of_file = subdir
        file_name = file.split()
        if any('LMZ' in s for s in file_name):
            print(os.path.join(file))
