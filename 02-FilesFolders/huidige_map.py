import os


workdir = os.getcwd()

mapname = ""

while len(mapname) == 0:
    mapname = input("Enter new folder name: ")

    if len(mapname) > 0:
        os.mkdir(mapname)
    else:
        print("Please enter a name.")

print('New folder called "' + mapname + '" was created at path "' + workdir + '"')
