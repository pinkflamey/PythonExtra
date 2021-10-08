import io
import os
import time

# Bestand in read-only (r) mode openen
bestand = open("test.txt", "r")
bestand2 = open("test2.txt", "r")

# Alle tekst lezen met read() en opslaan in de variabele: inhoud
frame1 = bestand.read()
frame2 = bestand2.read()

for x in range(100):
    os.system("cls")
    print(frame1)
    time.sleep(0.20)
    os.system("cls")
    print(frame2)
    time.sleep(0.20)
