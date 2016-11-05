import os
import subprocess
from os.path import expanduser
from termcolor import colored


HOME_PATH = expanduser("~/")

INSTALLATION_FOLDER = "PYTHON_INSTALLER"

INSTALLATION_FILE = "INSTALLATION_NOTES"

TOOLS = raw_input(
"""
Please select a thing from the following to begin :
1.Java
2.Android
3.python
4.webdevelopment
""")

def installation_checker(tool):
    if tool == 'java':
        command = '%s -version' % (tool)
        command_executer = os.system(command)
    else:   
        command = '%s --version' % (tool)
        command_executer = os.system(command)

    if command_executer !=0:
        print colored("%s is not installed,let me install that for you master bruce" % (tool), 'blue')
        installer(tool=tool) #installer to install the things.
    else:
        print colored("%s is already installed master bruce" % (tool), 'blue') 


def installer(tool=None):
    if tool == 'java':
        print colored("Installing java master bruce.....", "green")
        command = 'sudo apt-get install default-jre'    
        os.system(command)
        print "Installing eclipse master bruce....."
        # command = 

# def ide_installer(tool=None):
#     if tool == 'java':
#         print colored('CHECKING WHETHER ECLIPSE IS INSTALLED OR NOT, MASTER BRUCE', 'green')
#         command = 

    
if TOOLS == '1':
    print installation_checker("java")   

elif TOOLS == '2':
    print installation_checker("Android")

elif TOOLS == '3':
    print installation_checker("python")

elif TOOLS == '4':
    print installation_checker("webdevelopment")


def installation_notes_creator(tool, version):
    file_opener = open('installer', 'wb')
    content = """
             Title : %s
             Version : %s
             path : %s
             """
    file_opener.close()


#def installation_directory_checker(folder, home_path, installation_folder):
#    if not os.path.exists(folder):
#        director_creater = os.makedirs(os.path.join(HOME_PATH, INSTALLATION_FOLDER)
    #else:
    #    print "Installation notes will be in %s as %s" % (installation_folder, installation_file)

       
        



