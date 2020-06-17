from PIL import Image, ImageDraw, ImageFont  # Allows us to edit images and wrap the text boxes
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

    lines1 = text_wrap(str(message[0]), font, 228)  # splits the messages
    while len(lines1) >= 197.0/line_height - 1:  # adjusts the font size to be fit correctly based off the text
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines1 = text_wrap(str(message[0]), font, 228)
        line_height = font.getsize('hg')[1]
    lines2 = text_wrap(str(message[1]), font, 228)
    while len(lines2) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines2 = text_wrap(str(message[1]), font, 228)
        line_height = font.getsize('hg')[1]
    lines3 = text_wrap(str(message[2]), font, 228)
    while len(lines3) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines3 = text_wrap(str(message[2]), font, 228)
        line_height = font.getsize('hg')[1]
    lines4 = text_wrap(str(message[3]), font, 228)
    while len(lines4) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines4 = text_wrap(str(message[3]), font, 228)
        line_height = font.getsize('hg')[1]
    lines5 = text_wrap(str(message[4]), font, 228)
    while len(lines5) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines5 = text_wrap(str(message[4]), font, 228)
        line_height = font.getsize('hg')[1]
    lines6 = text_wrap(str(message[5]), font, 228)
    while len(lines6) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines6 = text_wrap(str(message[5]), font, 228)
        line_height = font.getsize('hg')[1]
    # By taking the longest length of a line, we get the smallest font size which then trickles down through each loop
    # by taking this smallest font size we guarantee the rest of the boxes will fit

    x = 0  # initializes coordinates to paste text in box and resets y every time
    y = 0
    for line1 in lines1:  # goes through all the lines and draws the text at the specified coordinates
        box_draw.text((x, y), line1, fill=color, font=font)
        y = y + line_height  # goes up by the line height each time
    y = 0  # resets the y and does this process 5 more times
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

    source_image.paste(box_img, (20, 124))  # pastes all the needed boxes on the image
    source_image.paste(box_img2, (335, 124))
    source_image.paste(box_img3, (20, 341))
    source_image.paste(box_img4, (335, 341))
    source_image.paste(box_img5, (20, 559))
    source_image.paste(box_img6, (335, 559))

    variable = 'finalPDF/' + str(variable) + '.png'  # produces the file name to save the file to
    source_image.save(variable)  # saves the file


def letter_5(message, variable):  # see letter_6 for a more in depth walk through of the function
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

    lines1 = text_wrap(str(message[0]), font, 228)  # splits the messages into a text wrap
    while len(lines1) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines1 = text_wrap(str(message[0]), font, 228)
        line_height = font.getsize('hg')[1]

    lines2 = text_wrap(str(message[1]), font, 228)
    while len(lines2) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines2 = text_wrap(str(message[1]), font, 228)
        line_height = font.getsize('hg')[1]

    lines3 = text_wrap(str(message[2]), font, 228)
    while len(lines3) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines3 = text_wrap(str(message[2]), font, 228)
        line_height = font.getsize('hg')[1]

    lines4 = text_wrap(str(message[3]), font, 228)
    while len(lines4) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines4 = text_wrap(str(message[3]), font, 228)
        line_height = font.getsize('hg')[1]

    lines5 = text_wrap(str(message[4]), font, 228)
    while len(lines5) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines5 = text_wrap(str(message[4]), font, 228)
        line_height = font.getsize('hg')[1]

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


def letter_4(message, variable):   # see letter_6 for a more in depth walk through of the function
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

    lines1 = text_wrap(str(message[0]), font, 228)  # splits the messages into a text wrap
    while len(lines1) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines1 = text_wrap(str(message[0]), font, 228)
        line_height = font.getsize('hg')[1]

    lines2 = text_wrap(str(message[1]), font, 228)
    while len(lines2) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines2 = text_wrap(str(message[1]), font, 228)
        line_height = font.getsize('hg')[1]

    lines3 = text_wrap(str(message[2]), font, 228)
    while len(lines3) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines3 = text_wrap(str(message[2]), font, 228)
        line_height = font.getsize('hg')[1]

    lines4 = text_wrap(str(message[3]), font, 228)
    while len(lines4) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines4 = text_wrap(str(message[3]), font, 228)
        line_height = font.getsize('hg')[1]

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


def letter_3(message, variable):   # see letter_6 for a more in depth walk through of the function
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

    lines1 = text_wrap(str(message[0]), font, 228)  # splits the messages into a text wrap
    while len(lines1) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines1 = text_wrap(str(message[0]), font, 228)
        line_height = font.getsize('hg')[1]

    lines2 = text_wrap(str(message[1]), font, 228)
    while len(lines2) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines2 = text_wrap(str(message[1]), font, 228)
        line_height = font.getsize('hg')[1]

    lines3 = text_wrap(str(message[2]), font, 228)
    while len(lines3) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines3 = text_wrap(str(message[2]), font, 228)
        line_height = font.getsize('hg')[1]

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


def letter_2(message, variable):   # see letter_6 for a more in depth walk through of the function
    font_size = 11
    source_image = Image.open("Assets/2 Responses.png").convert("RGBA")  # initialise the drawing with background + font
    font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
    line_height = font.getsize('hg')[1]

    box_img = Image.new('RGBA', (228, 197), "white")  # Makes our 6 white boxes to put text into
    box_draw = ImageDraw.Draw(box_img)

    box_img2 = Image.new('RGBA', (228, 197), "white")
    box_draw2 = ImageDraw.Draw(box_img2)

    color = 'rgb(0, 0, 0)'  # black color for font

    lines1 = text_wrap(str(message[0]), font, 228)  # splits the messages into a text wrap
    while len(lines1) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines1 = text_wrap(str(message[0]), font, 228)
        line_height = font.getsize('hg')[1]

    lines2 = text_wrap(str(message[1]), font, 228)
    while len(lines2) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines2 = text_wrap(str(message[1]), font, 228)
        line_height = font.getsize('hg')[1]

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


def letter_1(message, variable):   # see letter_6 for a more in depth walk through of the function
    font_size = 11
    source_image = Image.open("Assets/1 Responses.png").convert("RGBA")  # initialise the drawing with background + font
    font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
    line_height = font.getsize('hg')[1]

    box_img = Image.new('RGBA', (512, 255), "white")  # Makes our 6 white boxes to put text into
    box_draw = ImageDraw.Draw(box_img)

    color = 'rgb(0, 0, 0)'  # black color for font

    lines1 = text_wrap(str(message[0]), font, 512)  # splits the messages into a text wrap so that it can fit into the box
    while len(lines1) >= 197.0/line_height - 1:
        font_size -= 1
        font = ImageFont.truetype('fonts/DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=font_size)
        lines1 = text_wrap(str(message[0]), font, 228)
        line_height = font.getsize('hg')[1]

    x = 0  # initializes coordinates to paste text in box and resets y every time
    y = 0
    for line1 in lines1:
        box_draw.text((x, y), line1, fill=color, font=font)
        y = y + line_height

    source_image.paste(box_img, (50, 140))

    variable = 'finalPDF/' + str(variable) + '.png'
    source_image.save(variable)
