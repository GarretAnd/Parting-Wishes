from PIL import Image, ImageDraw, ImageFont  # Allows us to edit images

image = Image.open("Practice.png")  # initialise the drawing context with the image object as background
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=20)

(x, y) = (50, 120)
message = "Eureka!"
color = 'rgb(0, 0, 0)'  # black color

# draw the message on the background
draw.text((x, y), message, fill=color, font=font)
image.show()
variable = 'word' + '.png'
image.save(variable)
