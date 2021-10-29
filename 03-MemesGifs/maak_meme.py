from PIL import Image, ImageFont, ImageDraw


name = input("Enter file name: ")
achtergrond = Image.open("C:/Users/pinkf/Documents/Mediacollege Amsterdam/Bewijzenmap/Periode 1.1/FLEX (Python)/03-MemesGifs/"+name)

width, height = achtergrond.size
print("Width: " + str(width) + "\nHeight: " + str(height))

a = input("Enter font: ")
b = input("Enter font size: ")
font = ImageFont.truetype(a, int(b))

area = ImageDraw.Draw(achtergrond)

text = input("Enter text: ")

text_width, text_height = area.textsize(text, font=font) 
print("Text width =" + str(text_width) + "\nText height =" + str(text_height))


if input("Center X? (y/n): ").lower() == "y":
    start_x = (width - text_width) / 2
else:
    start_x = int(input("Enter start X: "))
if input("Center Y? (y/n): ").lower() == "y":
    start_y = (width - text_width) / 2
else:
    start_y = int(input("Enter start Y: "))


color_r = int(input("Enter color (x, -, -): "))
color_g = int(input("Enter color (-, x, -): "))
color_b = int(input("Enter color (-, -, x): "))


if input("Text shadow? (y/no): ").lower() == "y":
    area.multiline_text((start_x - 5,start_y - 5), text, font=font, fill=(int(input("Color (x, -, -): ")),int(input("Color (-, x, -): ")),int(input("Color (-, -, x): "))))

area.multiline_text((start_x,start_y), text, font=font, fill=(color_r,color_g,color_b))

a = input("Show image? (y/n): ")
if a.lower() == "y":
    achtergrond.show()
achtergrond.save("new_" + name)