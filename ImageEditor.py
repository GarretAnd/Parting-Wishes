from PIL import Image, ImageDraw, ImageFont  # Allows us to edit images
from textWrapper import text_wrap

font_size = 11
source_image = Image.open("Assets/6 Responses.png").convert("RGBA")  # initialise the drawing with asset as background
font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
line_height = font.getsize('hg')[1]

box_img = Image.new('RGBA', (228, 197), "white")
box_draw = ImageDraw.Draw(box_img)


(x, y) = (0, 0)
message = "Eureka! This text box should be all set hopefully? I really don't know what I'm doing and I really hope " \
          "this library can save my but" \
          "in a major way, if not this will be a tough look and a lot of manual labor that I am not excited to do. " \
          "Hopefully it will all work... who knows" \
          "worse comes to worse we just do it. We will make it either way and think about how happy this project made" \
          " hana to do. She probably loves" \
          "this shit now and is amazed at how its all possible. CS is so fucken powerful and it's so cool to be able " \
          "to sit down and do this " \
          "stuff for people without fear. It's just amazing what can be accomplished by a little tenacity and some " \
          "computer science fun, am I right? "
color = 'rgb(0, 0, 0)'  # black color

lines = text_wrap(message, font, 228)
print(lines)
# draw the message on the background
for line in lines:
    box_draw.text((x, y), line, fill=color, font=font)
    y = y + line_height

y_box = 147
source_image.paste(box_img, (x, y_box))
source_image.show()
variable = 'finalPDF/TestBounds2.png'
source_image.save(variable)
