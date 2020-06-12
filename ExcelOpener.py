import openpyxl  # Imports the Library Needed to work with excel documents; column C (person) and D (data)
from PIL import Image, ImageDraw, ImageFont  # Allows us to edit images

file = "Parting Wishes file.xlsx"  # Opening the excel document
wb = openpyxl.load_workbook(file)  # and loading the worksheet I want
sheet_name = wb['Form Responses 1']

name_set = set()  # initializing empty set and empty dict
name_dict = {}

i = 2  # might not start at 2, check starting point in future
while i != 687:  # put last number of rows here in future
    print(i)
    name = sheet_name['C' + str(i)].value
    response = sheet_name['D' + str(i)].value

    if name not in name_set:  # if person's name is not in the set add their name to it
        name_set.add(name)  # create an entry in the dictionary for them and
        name_dict[name] = {response}  # add their response as a set
    else:
        name_dict[name].add(response)  # else add their data to already existing set in dict
    i += 1

wb.save(file)  # Saves file at the end
name_keys = name_dict.keys()

for index in name_keys:  # gets data associated with index
    email = index.replace(' ', '.') + '.20@dartmouth.edu'  # makes their email from the name
    print(email)
    item = name_dict[index]  # gets the set of data associated with the email and the size of it
    size = len(item)
    end = size % 6  # Tells us what type of letter we need

    for response in item:
        print(response)

# im = Image.open("6 Responses.png")  # How to open a image will pillow
# im.show()

image = Image.open("6 Responses.png")  # initialise the drawing context with the image object as background
draw = ImageDraw.Draw(image)
(x, y) = (46, 124)
font = ImageFont.truetype('DartmouthRuzickaGeneral/DartmouthRuzicka-Regular.ttf', size=45)
