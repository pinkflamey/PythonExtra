import io
import os

bestand = open("names.txt", "r")

line = bestand.readline()

while line:
    line = line.strip()
    line = line.strip("\n")
    os.mkdir(line)
    line = bestand.readline()
