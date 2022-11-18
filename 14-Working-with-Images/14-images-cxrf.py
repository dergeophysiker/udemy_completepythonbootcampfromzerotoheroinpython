from PIL import Image,ImageShow
ImageShow.WindowsViewer.format = "PNG"


mac=Image.open('example.jpg')
print(type(mac))
#mac.show()
print(mac.filename)
print(mac.format_description)
print(mac.size)

cropped=mac.crop((0,0,100,100))
#cropped.show()

pencils=Image.open('pencils.jpg')
print(pencils.size)
x=0
y=0
w=1950/3
h=1300/10

cropped_pencils = pencils.crop( (x,y,w,h))
#cropped_pencils.show()

halfway = 1993/2
x = halfway - 200
w = halfway + 200
y = 800
h = 1257
littlemac = mac.crop((x,y,w,h))
#littlemac.show()
mac.paste(im=littlemac,box=(0,0))
#mac.show()

red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png').convert('RGBA')
#blue = Image.open('blue_color.png')
print(blue.format_description)
print(blue.getbands())
print(blue.getpalette())
print(blue.getchannel(0))
blue.putalpha(128)
#blue.show()
red.putalpha(128)
#red.show()

blue.paste(im=red,box=(0,0),mask=red)
blue.show()


blue.save("purple1.png")
purple1=Image.open("purple1.png")
purple1.show()