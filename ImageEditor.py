from PIL import Image, ImageDraw, ImageFont  # Allows us to edit images
from textWrapper import text_wrap


def letter_6(message, variable):
    font_size = 11
    source_image = Image.open("Assets/6 Responses.png").convert("RGBA")  # initialise the drawing with background + font
    font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)

    line_height = font.getsize('hg')[1]

    box_img = Image.new('RGBA', (228, 197), "white")  # Makes our 6 white boxes to put text into
    box_draw = ImageDraw.Draw(box_img)

    box_img2 = Image.new('RGBA', (228, 197), "white")
    box_draw2 = ImageDraw.Draw(box_img2)

    box_img3 = Image.new('RGBA', (228, 197), "white")
    box_draw3 = ImageDraw.Draw(box_img3)

    box_img4 = Image.new('RGBA', (228, 197), "white")
    box_draw4 = ImageDraw.Draw(box_img4)

    box_img5 = Image.new('RGBA', (228, 197), "white")
    box_draw5 = ImageDraw.Draw(box_img5)

    box_img6 = Image.new('RGBA', (228, 197), "white")
    box_draw6 = ImageDraw.Draw(box_img6)

    color = 'rgb(0, 0, 0)'  # black color for font

    lines1 = text_wrap(str(message[0]), font, 228)  # splits the messages into a text wrap so that it can fit into the box
    lines2 = text_wrap(str(message[1]), font, 228)
    lines3 = text_wrap(str(message[2]), font, 228)
    lines4 = text_wrap(str(message[3]), font, 228)
    lines5 = text_wrap(str(message[4]), font, 228)
    lines6 = text_wrap(str(message[5]), font, 228)

    x = 0  # initializes coordinates to paste text in box and resets y every time
    y = 0
    for line1 in lines1:
        box_draw.text((x, y), line1, fill=color, font=font)
        y = y + line_height

    y = 0
    for line2 in lines2:
        box_draw2.text((x, y), line2, fill=color, font=font)
        y = y + line_height

    y = 0
    for line3 in lines3:
        box_draw3.text((x, y), line3, fill=color, font=font)
        y = y + line_height

    y = 0
    for line4 in lines4:
        box_draw4.text((x, y), line4, fill=color, font=font)
        y = y + line_height

    y = 0
    for line5 in lines5:
        box_draw5.text((x, y), line5, fill=color, font=font)
        y = y + line_height

    y = 0
    for line6 in lines6:
        box_draw6.text((x, y), line6, fill=color, font=font)
        y = y + line_height

    source_image.paste(box_img, (20, 124))
    source_image.paste(box_img2, (335, 124))
    source_image.paste(box_img3, (20, 341))
    source_image.paste(box_img4, (335, 341))
    source_image.paste(box_img5, (20, 559))
    source_image.paste(box_img6, (335, 559))

    variable = 'finalPDF/' + str(variable) + '.png'
    source_image.save(variable)


def letter_5(message, variable):
    font_size = 11
    source_image = Image.open("Assets/5 Responses.png").convert("RGBA")  # initialise the drawing with background + font
    font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
    line_height = font.getsize('hg')[1]

    box_img = Image.new('RGBA', (228, 197), "white")  # Makes our 6 white boxes to put text into
    box_draw = ImageDraw.Draw(box_img)

    box_img2 = Image.new('RGBA', (228, 197), "white")
    box_draw2 = ImageDraw.Draw(box_img2)

    box_img3 = Image.new('RGBA', (228, 197), "white")
    box_draw3 = ImageDraw.Draw(box_img3)

    box_img4 = Image.new('RGBA', (228, 197), "white")
    box_draw4 = ImageDraw.Draw(box_img4)

    box_img5 = Image.new('RGBA', (228, 197), "white")
    box_draw5 = ImageDraw.Draw(box_img5)

    color = 'rgb(0, 0, 0)'  # black color for font

    lines1 = text_wrap(str(message[0]), font, 228)  # splits the messages into a text wrap so that it can fit into the box
    lines2 = text_wrap(str(message[1]), font, 228)
    lines3 = text_wrap(str(message[2]), font, 228)
    lines4 = text_wrap(str(message[3]), font, 228)
    lines5 = text_wrap(str(message[4]), font, 228)

    x = 0  # initializes coordinates to paste text in box and resets y every time
    y = 0
    for line1 in lines1:
        box_draw.text((x, y), line1, fill=color, font=font)
        y = y + line_height

    y = 0
    for line2 in lines2:
        box_draw2.text((x, y), line2, fill=color, font=font)
        y = y + line_height

    y = 0
    for line3 in lines3:
        box_draw3.text((x, y), line3, fill=color, font=font)
        y = y + line_height

    y = 0
    for line4 in lines4:
        box_draw4.text((x, y), line4, fill=color, font=font)
        y = y + line_height

    y = 0
    for line5 in lines5:
        box_draw5.text((x, y), line5, fill=color, font=font)
        y = y + line_height

    source_image.paste(box_img, (20, 124))
    source_image.paste(box_img2, (335, 124))
    source_image.paste(box_img3, (20, 341))
    source_image.paste(box_img4, (335, 341))
    source_image.paste(box_img5, (20, 559))

    variable = 'finalPDF/' + str(variable) + '.png'
    source_image.save(variable)


def letter_4(message, variable):
    font_size = 11
    source_image = Image.open("Assets/4 Responses.png").convert("RGBA")  # initialise the drawing with background + font
    font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
    line_height = font.getsize('hg')[1]

    box_img = Image.new('RGBA', (228, 197), "white")  # Makes our 6 white boxes to put text into
    box_draw = ImageDraw.Draw(box_img)

    box_img2 = Image.new('RGBA', (228, 197), "white")
    box_draw2 = ImageDraw.Draw(box_img2)

    box_img3 = Image.new('RGBA', (228, 197), "white")
    box_draw3 = ImageDraw.Draw(box_img3)

    box_img4 = Image.new('RGBA', (228, 197), "white")
    box_draw4 = ImageDraw.Draw(box_img4)

    color = 'rgb(0, 0, 0)'  # black color for font

    lines1 = text_wrap(str(message[0]), font, 228)  # splits the messages into a text wrap so that it can fit into the box
    lines2 = text_wrap(str(message[1]), font, 228)
    lines3 = text_wrap(str(message[2]), font, 228)
    lines4 = text_wrap(str(message[3]), font, 228)

    x = 0  # initializes coordinates to paste text in box and resets y every time
    y = 0
    for line1 in lines1:
        box_draw.text((x, y), line1, fill=color, font=font)
        y = y + line_height

    y = 0
    for line2 in lines2:
        box_draw2.text((x, y), line2, fill=color, font=font)
        y = y + line_height

    y = 0
    for line3 in lines3:
        box_draw3.text((x, y), line3, fill=color, font=font)
        y = y + line_height

    y = 0
    for line4 in lines4:
        box_draw4.text((x, y), line4, fill=color, font=font)
        y = y + line_height

    source_image.paste(box_img, (20, 124))
    source_image.paste(box_img2, (335, 124))
    source_image.paste(box_img3, (20, 341))
    source_image.paste(box_img4, (20, 559))

    variable = 'finalPDF/' + str(variable) + '.png'
    source_image.save(variable)


def letter_3(message, variable):
    font_size = 11
    source_image = Image.open("Assets/3 Responses.png").convert("RGBA")  # initialise the drawing with background + font
    font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
    line_height = font.getsize('hg')[1]

    box_img = Image.new('RGBA', (228, 197), "white")  # Makes our 6 white boxes to put text into
    box_draw = ImageDraw.Draw(box_img)

    box_img2 = Image.new('RGBA', (228, 197), "white")
    box_draw2 = ImageDraw.Draw(box_img2)

    box_img3 = Image.new('RGBA', (228, 197), "white")
    box_draw3 = ImageDraw.Draw(box_img3)

    color = 'rgb(0, 0, 0)'  # black color for font

    lines1 = text_wrap(str(message[0]), font, 228)  # splits the messages into a text wrap so that it can fit into the box
    lines2 = text_wrap(str(message[1]), font, 228)
    lines3 = text_wrap(str(message[2]), font, 228)

    x = 0  # initializes coordinates to paste text in box and resets y every time
    y = 0
    for line1 in lines1:
        box_draw.text((x, y), line1, fill=color, font=font)
        y = y + line_height

    y = 0
    for line2 in lines2:
        box_draw2.text((x, y), line2, fill=color, font=font)
        y = y + line_height

    y = 0
    for line3 in lines3:
        box_draw3.text((x, y), line3, fill=color, font=font)
        y = y + line_height

    source_image.paste(box_img, (20, 124))
    source_image.paste(box_img2, (20, 341))
    source_image.paste(box_img3, (20, 559))

    variable = 'finalPDF/' + str(variable) + '.png'
    source_image.save(variable)


def letter_2(message, variable):
    font_size = 11
    source_image = Image.open("Assets/2 Responses.png").convert("RGBA")  # initialise the drawing with background + font
    font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
    line_height = font.getsize('hg')[1]

    box_img = Image.new('RGBA', (228, 197), "white")  # Makes our 6 white boxes to put text into
    box_draw = ImageDraw.Draw(box_img)

    box_img2 = Image.new('RGBA', (228, 197), "white")
    box_draw2 = ImageDraw.Draw(box_img2)

    color = 'rgb(0, 0, 0)'  # black color for font

    lines1 = text_wrap(str(message[0]), font, 228)  # splits the messages into a text wrap so that it can fit into the box
    lines2 = text_wrap(str(message[1]), font, 228)

    x = 0  # initializes coordinates to paste text in box and resets y every time
    y = 0
    for line1 in lines1:
        box_draw.text((x, y), line1, fill=color, font=font)
        y = y + line_height

    y = 0
    for line2 in lines2:
        box_draw2.text((x, y), line2, fill=color, font=font)
        y = y + line_height

    source_image.paste(box_img, (20, 150))
    source_image.paste(box_img2, (335, 150))

    variable = 'finalPDF/' + str(variable) + '.png'
    source_image.save(variable)


def letter_1(message, variable):
    font_size = 11
    source_image = Image.open("Assets/1 Responses.png").convert("RGBA")  # initialise the drawing with background + font
    font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
    line_height = font.getsize('hg')[1]

    box_img = Image.new('RGBA', (512, 255), "white")  # Makes our 6 white boxes to put text into
    box_draw = ImageDraw.Draw(box_img)

    color = 'rgb(0, 0, 0)'  # black color for font

    lines1 = text_wrap(str(message), font, 512)  # splits the messages into a text wrap so that it can fit into the box

    x = 0  # initializes coordinates to paste text in box and resets y every time
    y = 0
    for line1 in lines1:
        box_draw.text((x, y), line1, fill=color, font=font)
        y = y + line_height

    source_image.paste(box_img, (50, 140))

    variable = 'finalPDF/' + str(variable) + '.png'
    source_image.save(variable)


# test call of functions
#mes = {
#    0: 'Omphalotus nidiformis, or ghost fungus, is a bioluminescent gilled mushroom that occurs primarily in southern Australia and Tasmania, and has been reported from India. The cream-coloured fan- or funnel-shaped caps, up to 30 cm (12 in) across, have shades of orange, brown, purple, or bluish-black. The white or cream gills run down the length of the stalk, which is up to 8 cm (3 in) long and tapers in thickness to the base. The fungus is both saprotrophic and parasitic, and its fruit bodies are generally found growing in overlapping clusters on a wide variety of dead or dying trees. First described scientifically in 1844, O. nidiformis (from Latin for ' + ') was known by several names before Orson K. Miller Jr. assigned its current name in 1994. Similar in',
#    1: 'Omphalotus nidiformis, or ghost fungus, is a bioluminescent gilled mushroom that occurs primarily in southern Australia and Tasmania, and has been reported from India. The cream-coloured fan- or funnel-shaped caps, up to 30 cm (12 in) across, have shades of orange, brown, purple, or bluish-black. The white or cream gills run down the length of the stalk, which is up to 8 cm (3 in) long and tapers in thickness to the base. The fungus is both saprotrophic and parasitic, and its fruit bodies are generally found growing in overlapping clusters on a wide variety of dead or dying trees. First described scientifically in 1844, O. nidiformis (from Latin for ' + ') was known by several names before Orson K. Miller Jr. assigned its current name in 1994. Similar in',
#    2: 'Omphalotus nidiformis, or ghost fungus, is a bioluminescent gilled mushroom that occurs primarily in southern Australia and Tasmania, and has been reported from India. The cream-coloured fan- or funnel-shaped caps, up to 30 cm (12 in) across, have shades of orange, brown, purple, or bluish-black. The white or cream gills run down the length of the stalk, which is up to 8 cm (3 in) long and tapers in thickness to the base. The fungus is both saprotrophic and parasitic, and its fruit bodies are generally found growing in overlapping clusters on a wide variety of dead or dying trees. First described scientifically in 1844, O. nidiformis (from Latin for ' + ') was known by several names before Orson K. Miller Jr. assigned its current name in 1994. Similar in',
#    3: 'Omphalotus nidiformis, or ghost fungus, is a bioluminescent gilled mushroom that occurs primarily in southern Australia and Tasmania, and has been reported from India. The cream-coloured fan- or funnel-shaped caps, up to 30 cm (12 in) across, have shades of orange, brown, purple, or bluish-black. The white or cream gills run down the length of the stalk, which is up to 8 cm (3 in) long and tapers in thickness to the base. The fungus is both saprotrophic and parasitic, and its fruit bodies are generally found growing in overlapping clusters on a wide variety of dead or dying trees. First described scientifically in 1844, O. nidiformis (from Latin for ' + ') was known by several names before Orson K. Miller Jr. assigned its current name in 1994. Similar in',
#    4: 'Omphalotus nidiformis, or ghost fungus, is a bioluminescent gilled mushroom that occurs primarily in southern Australia and Tasmania, and has been reported from India. The cream-coloured fan- or funnel-shaped caps, up to 30 cm (12 in) across, have shades of orange, brown, purple, or bluish-black. The white or cream gills run down the length of the stalk, which is up to 8 cm (3 in) long and tapers in thickness to the base. The fungus is both saprotrophic and parasitic, and its fruit bodies are generally found growing in overlapping clusters on a wide variety of dead or dying trees. First described scientifically in 1844, O. nidiformis (from Latin for ' + ') was known by several names before Orson K. Miller Jr. assigned its current name in 1994. Similar in',
#    5: 'Omphalotus nidiformis, or ghost fungus, is a bioluminescent gilled mushroom that occurs primarily in southern Australia and Tasmania, and has been reported from India. The cream-coloured fan- or funnel-shaped caps, up to 30 cm (12 in) across, have shades of orange, brown, purple, or bluish-black. The white or cream gills run down the length of the stalk, which is up to 8 cm (3 in) long and tapers in thickness to the base. The fungus is both saprotrophic and parasitic, and its fruit bodies are generally found growing in overlapping clusters on a wide variety of dead or dying trees. First described scientifically in 1844, O. nidiformis (from Latin for ' + ') was known by several names before Orson K. Miller Jr. assigned its current name in 1994. Similar in'}

#letter_6(mes, 'output0')
#letter_5(mes, 'output1')
#letter_4(mes, 'output2')
#letter_3(mes, 'output3')
#letter_2(mes, 'output4')
#letter_1(mes, 'output5')
