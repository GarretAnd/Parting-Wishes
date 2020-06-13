import openpyxl  # Imports the Library Needed to work with excel documents; column C (person) and D (data)
from PIL import Image, ImageDraw, ImageFont  # Allows us to edit images

file = "Parting Wishes file.xlsx"  # Opening the excel document
wb = openpyxl.load_workbook(file)  # and loading the worksheet I want
sheet_name = wb['Form Responses 1']

name_set = set()  # initializing empty set and empty dict
name_dict = {}

i = 2  # starting row
while i != 100:  # how far down the rows to go final value is: 3448
    name = sheet_name['C' + str(i)].value
    response = sheet_name['D' + str(i)].value

    if name not in name_set:  # if person's name is not in the set add their name to it
        name_set.add(name)  # create an entry in the dictionary for them and
        name_dict[name] = {response}  # add their response as a set
    else:
        name_dict[name].add(response)  # else add their data to already existing set in dict
    i += 1

wb.close()  # Closes file at the end
name_keys = name_dict.keys()  # Gets every name in the file


for index in name_keys:  # gets data associated with index
    email = index.replace(' ', '.') + '.20@dartmouth.edu'  # makes their email from the name
    item = name_dict[index]  # gets the set of data associated with the email and the size of it
    size = len(item)
    end = size % 6  # Tells us what type of letter we need

    for response in item:
        print(response)
