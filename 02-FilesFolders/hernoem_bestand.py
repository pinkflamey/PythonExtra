import os

# Bestandsnaam in variabele zetten
bestandsnaam = "demobestand.txt"

# Vraag de huidige map op en sla op in variabele: huidige_map
huidige_map = os.getcwd()

# met de os.path module kun je paden naar bestanden samenstellen
volledige_pad = os.path.join(huidige_map, bestandsnaam)
print("Dit bestand gaan we hernoemen: " + volledige_pad)

new_name = ""
while len(new_name) == 0:
    new_name = input("new name: ")

    nieuwe_volledige_pad = os.path.join(huidige_map, new_name)

    if len(new_name) > 0:
        print("Bestand wordt hernoemd naar: " + nieuwe_volledige_pad)
    else:
        print("Vul een naam in.")

print("renamed")
