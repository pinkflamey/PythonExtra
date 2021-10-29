from PIL import Image



def twiceSmaller():
    half_breedte = afbeelding.width // 2
    half_hoogte = afbeelding.height // 2

    nieuwe_afmeting = (half_breedte, half_hoogte)

    kleinere_afbeelding = afbeelding.resize(nieuwe_afmeting)

    kleinere_afbeelding.save("img.png")

    kleinere_afbeelding.show()

def twiceBigger():
    double_breedte = afbeelding.width * 2
    double_hoogte = afbeelding.height * 2

    nieuwe_afmeting = (double_breedte, double_hoogte)

    grotere_afbeelding = afbeelding.resize(nieuwe_afmeting)

    grotere_afbeelding.save("img.png")

    grotere_afbeelding.show()

def start():
    a = input("Enter image name: ")
    if a != "":
        afbeelding = Image.open(str(a))

        breedte = str(afbeelding.width)
        hoogte = str(afbeelding.height)
    else:
        start()

    

start()