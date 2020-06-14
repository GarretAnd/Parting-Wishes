import openpyxl  # Imports the Library Needed to work with excel documents; column C (person) and D (data)
from ImageEditor import *
from Cleaner import deleter
from MailPrac import *

file = "Data/Parting Wishes file.xlsx"  # Opening the excel document
wb = openpyxl.load_workbook(file)  # and loading the worksheet I want
sheet_name = wb['Form Responses 1']
name_set = set()  # initializing empty set and empty dict
name_dict = {}

file_2 = "Data/'20s Emails.xlsx"  # Opening the excel document
wb2 = openpyxl.load_workbook(file_2)  # and loading the worksheet I want
sheet_name2 = wb2['Emails']
email_set = set()  # initializing empty set and empty dict

x = 2
while x != 1075:
    dart_email = sheet_name2['A' + str(x)].value
    print(str(dart_email))
    email_set.add(dart_email)
    x += 1
wb2.close()  # Closes file at the end

i = 2  # starting row
while i != 3448:  # how far down the rows to go final value is: 3448
    name = sheet_name['C' + str(i)].value
    print(str(name))
    response = sheet_name['D' + str(i)].value

    if name not in name_set:  # if person's name is not in the set add their name to it
        name_set.add(name)  # create an entry in the dictionary for them and
        name_dict[name] = {response}  # add their response as a set
    else:
        name_dict[name].add(response)  # else add their data to already existing set in dict
    i += 1

wb.close()  # Closes file at the end
name_keys = name_dict.keys()  # Gets every name in the file
used_emails = set()

server = get_server('gd2strems@gmail.com', 'ping987\'')  # Change to: partingwishes2020@gmail.com, Closure1769!
for index in name_keys:  # gets data associated with index
    deleter()  # To remove all files in the root directory
    email = index.replace(' ', '.') + '.20@dartmouth.edu'  # makes their email from the name
    print(email)
    used_emails.add(email)
    item = name_dict[index]  # gets the set of data associated with the email and the size of it
    size = len(item)
    end = size % 6  # Tells us what type of letter we need

    if email == "Hana.C.Warmflash.20@dartmouth.edu":
        j = 0
        if size > 5:
            while len(item) > 5:
                print("The length of the item is: " + str(len(item)))
                i = 0
                reply = {}
                while i < 6:
                    reply[i] = item.pop()
                    i += 1
                letter_6(reply, 'output' + str(j))
                j += 1
                print("J is: " + str(j))
            if len(item) != 0:
                i = 0
                reply = {}
                while i < len(item):
                    reply[i] = item.pop()
                    i += 1

                if len(item) == 5:
                    letter_5(reply, 'output' + str(j))
                elif len(item) == 4:
                    letter_4(reply, 'output' + str(j))
                elif len(item) == 3:
                    letter_3(reply, 'output' + str(j))
                elif len(item) == 2:
                    letter_2(reply, 'output' + str(j))
                else:
                    letter_1(reply, 'output' + str(j))
                j += 1
        else:
            if len(item) != 0:
                i = 0
                reply = {}
                while i < len(item):
                    reply[i] = item.pop()
                    i += 1

                if len(item) == 5:
                    letter_5(reply, 'output' + str(j))
                elif len(item) == 4:
                    letter_4(reply, 'output' + str(j))
                elif len(item) == 3:
                    letter_3(reply, 'output' + str(j))
                elif len(item) == 2:
                    letter_2(reply, 'output' + str(j))
                else:
                    letter_1(reply, 'output' + str(j))

                j += 1

        print("J is " + str(j))
        address(email, server, j)
        break

#for ID in email_set:
    #if ID not in used_emails:
        #print(str(ID))
        #  address(ID, server, 0)

server.quit()
