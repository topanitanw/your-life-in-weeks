from PIL import Image, ImageDraw, ImageFont
from datetime import date
# from tkinter import *
# import tkcalendar as Calendar
import math
import sys

if len(sys.argv) != 4:
    print("Plese enter your birthdate! (ex: python3 ./main.py 2000 2 23)")
    exit()

if int(sys.argv[1]) < 1:
    print("Plese enter a valid year!")
    exit()

if int(sys.argv[2]) < 1 or int(sys.argv[2]) > 12:
    print("Plese enter a valid month!")
    exit()

if int(sys.argv[3]) < 1 or int(sys.argv[3]) > 31:
    print("Plese enter a valid day!")
    exit()

print("Year: " + sys.argv[1])
print("Month: " + sys.argv[2])
print("Day: " + sys.argv[3])

date1 = date(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
date2 = date.today()
weeks = math.floor(abs(date1 - date2).days / 7)

if date2.year < int(sys.argv[1]):
    print("Plese enter a valid birthdate! (A date before the current day)")
    exit()

if date2.year == int(sys.argv[1]) and date2.month < int(sys.argv[2]):
    print("Plese enter a valid birthdate! (A date before the current day)")
    exit()

if date2.year == int(sys.argv[1]) and date2.month == int(sys.argv[2]) and date2.day < int(sys.argv[3]):
    print("Plese enter a valid birthdate! (A date before the current day)")
    exit()

(W,H) = (1080, 1920)
img = Image.new('RGB', (W, H) , color = 'white')
msg =  "Your life in weeks"
d = ImageDraw.Draw(img)
fntSize = 100
fnt = ImageFont.truetype("myFont.ttf", fntSize)
w, h = d.textsize(msg, font=fnt)
d.text(((W-w)/2, 5), msg, font=fnt ,fill=(0,0,0))


(coord1, coord2) = (25, 100)
fntSize2 = 20
fnt2 = ImageFont.truetype("myFont.ttf", fntSize2)
index = 1

for k in range(1, 52):
    if k == index:
        d.text((coord1, coord2), str(index), font=fnt2 ,fill=(0,0,0))
        if index == 1:
            index = 5
        else:
            index += 5
    coord1 += 20


(x1, y1, x2, y2) = (5, 120, 15, 130)
(coord3, coord4) = (10, 115)
index2 = 0
count = 0

for j in range(0, 90):
    
    if j == index2:
        d.text((coord3, coord4), str(index2), font=fnt2 ,fill=(0,0,0))
        if index2 == 0:
            index2 = 5
        else:
            index2 += 5
    coord4 += 20  

    for i in range(52):
        x1 += 20
        x2 += 20

        if count >= weeks:
            d.rectangle((x1, y1, x2, y2), fill=(255, 255, 255), outline=(0, 0, 0))
        else:
            d.rectangle((x1, y1, x2, y2), fill=(0, 192, 192), outline=(0, 0, 0))

        count += 1

    x1 = 5
    x2 = 15
    y1 += 20
    y2 += 20

img.save('your_life_in_weeks.png')