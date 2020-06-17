import openpyxl  # Imports the Library Needed to work with excel documents; column C (person) and D (data)
from ImageEditor import *
from Cleaner import deleter
from MailPrac import *

email_username = "Your_Email_Username@gmail to send from"
email_password = "Password for the above username"

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
while i != 3493:  # how far down the rows to go final value is: 3448
    name = sheet_name['C' + str(i)].value
    response = sheet_name['D' + str(i)].value.replace("\n", " ")

    if name not in name_set:  # if person's name is not in the set add their name to it
        name_set.add(name)  # create an entry in the dictionary for them and
        name_dict[name] = {response}  # add their response as a set
    else:
        name_dict[name].add(response)  # else add their data to already existing set in dict
    i += 1

wb.close()  # Closes file at the end
name_keys = name_dict.keys()  # Gets every name in the file
used_emails = set()  # to keep track of what emails have been used this run
sent_emails = set()  # for when the program runs out of MB on the provided email, the outputted list can be pasted here

server = get_server(email_username, email_password)  # your email and password go here!
for index in name_keys:  # gets data associated with index
    deleter()  # To remove all files in the root directory
    email = index.replace(' ', '.') + '.20@dartmouth.edu'  # makes their email from the name
    print(email)
    item = name_dict[index]  # gets the set of data associated with the email and the size of it
    size = len(item)
    end = size % 6

    if index not in sent_emails:  # if the email hasn't already been sent to
        j = 0
        if size > 5:  # if the size of the responses for that name is greater than 5
            while len(item) > 5:  # while there are more than 5 responses
                i = 0
                reply = {}
                while i < 6:
                    reply[i] = item.pop()  # add all the items to an array in groupings of 6
                    i += 1
                letter_6(reply, 'output' + str(j))  # produces a 6 response letter
                j += 1  # used to keep track of the document names

            if len(item) != 0:  # if removing in groups of 6 still left responses
                i = 0
                reply = {}
                while 0 < len(item):  # pop all the items out
                    reply[i] = item.pop()
                    i += 1

                if len(reply) == 5:  # then sort into their final letter as needed.
                    letter_5(reply, 'output' + str(j))  # produce correct document depending on number of responses
                elif len(reply) == 4:
                    letter_4(reply, 'output' + str(j))
                elif len(reply) == 3:
                    letter_3(reply, 'output' + str(j))
                elif len(reply) == 2:
                    letter_2(reply, 'output' + str(j))
                else:
                    letter_1(reply, 'output' + str(j))
                j += 1
        else:  # if there wasn't more than 6 responses
            if len(item) != 0:
                i = 0
                reply = {}
                while 0 < len(item):  # pop all the items out
                    reply[i] = item.pop()
                    i += 1

                if len(reply) == 5:  # sort all the items to the needed letter
                    letter_5(reply, 'output' + str(j))  # produce correct document depending on number of responses
                elif len(reply) == 4:
                    letter_4(reply, 'output' + str(j))
                elif len(reply) == 3:
                    letter_3(reply, 'output' + str(j))
                elif len(reply) == 2:
                    letter_2(reply, 'output' + str(j))
                else:
                    letter_1(reply, 'output' + str(j))
                j += 1

            try:
                address(email, server, j, email_username)  # send the email
                used_emails.add(email)  # add the email to the used emails list which is the list of emails for this run
            except:
                print("Error, emails failed.")  # if failure print out the used_emails set to be copied into sent_emails
                print(used_emails)
                exit()

print("\n\n\n\n*** I made it to the email list ****\n\n\n\n")  # progress flag!
for ID in email_set:
    if ID not in used_emails and ID not in sent_emails:  # for all the people that haven't already received an email
        try:
            print(ID)
            address(ID, server, 0, email_username)  # send that person an email with no letters.
            used_emails.add(ID)
        except:
            print("Error, emails failed.")  # if failure print out the used_emails set to be copied into sent_emails
            print(used_emails)
            exit()

server.quit()  # exit the server
print("\n\n\n\n*** Succesfully Completed The \"Parting Wishes\" Program! ****\n\n\n\n")  # Yay!
