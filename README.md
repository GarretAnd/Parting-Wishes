#Parting Wishes Program
Code written by GarretAnd. Idea made in collaboration with Hana Warmflash, Mary Tobin, and Rebecca Wade.

## Purpose
Due to the hectic nature of the term spring term at Dartmouth during 2020, an idea for students to give parting wishes 
to graduating seniors was surmised in response to an Engs 12 final project asking for creative ways to give seniors some
closure. Thus the Parting Wishes Program was created which would allow students to send responses to seniors who would 
then receive cards. 

## Setup 
To run the program, connect a google forms to a google sheets, where students email is taken, then they can select a
seniors name to send a message to (make it a list option in google sheets with the cleaned names of all the seniors), 
and have them submit a text box limited to 750 characters. 

*Tip: Open up the desktop version of Outlook, do an extended search, then filter it based off department to get the
students in the class list. Save all the emails in a separate file, in another file clean the data (remove the .s and 
the .year@dartmouth.edu) and use that as the list for the form

After getting both the email list and the excel set up, when you finish taking in data from the google form, close it
then download the google sheets as an .xlsx file. Plug both the files into the Data directory and adjust the variables
throughout the script. 

When all is said and done you should be good to go to run it.

##Running 
While running you will have to be conscious of the emails. Google emails can only send up to 250 MB of data through 
3rd party authorization. So you will have to swap emails at some time throughout the project. For running it during 20S
4 different parting wishes emails were used. Since it will fail midway through sending, an exception is set up so that
the emails it had made it through are spit out, plug this data into the `sent_emails` set on line 43 of the "WishMaker.py"
program. Then switch the email and run it again. To use the gmail, always make sure access to less secure apps is disabled,
so that you can remotely use them.

##Summary
Hopefully this program is used multiple times and iterated on to improve! The seniors that knew I did the program said they
really liked it and it made a difference, so hopefully it can continue to do so! Crazy what code can do and how it can 
affect the people around us :)

Happy Coding! ~GarretAnd
