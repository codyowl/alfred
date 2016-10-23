import os
import subprocess
from os.path import expanduser

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

	if command_executer != '0':
		print "%s is not installed,let me install that for you master Bruce" % (tool)

def installer(tool):
	if tool == 'java':
		command = 'sudo apt-get install default-jre'			

	
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


def installation_directory_checker(folder, home_path, installation_folder):
    if not os.path.exists(folder):
        director_creater = os.makedirs(os.path.join(HOME_PATH, INSTALLATION_FOLDER)
    else:
        print "Installation notes will be in %s as %s" % (installation_folder, installation_file)

       
        



