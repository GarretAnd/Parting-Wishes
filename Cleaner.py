import shutil  # All credits for this function goes to Nick Stinemates on stackoverflow
import os  # Link can be found here https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder


def deleter():
    folder = 'finalPDF'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


deleter()
