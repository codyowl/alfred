import os
import subprocess
import time
from os.path import expanduser
from termcolor import colored


HOME_PATH = expanduser("~/")

INSTALLATION_FOLDER = "Alfred"

INSTALLATION_FOLDER_PATH = HOME_PATH + INSTALLATION_FOLDER

INSTALLATION_DETAILS_FILE = "Installation_notes"

JAVA_IDE = "eclipse"

TOOLS = raw_input(
"""
Please select a thing from the following for setting up the environment:
1.Java
2.Android
3.python
4.webdevelopment
""")

def installation_checker(tool):
    time.sleep(5)
    if tool == 'java':
        command = '%s -version' % (tool)
        command_executer = os.system(command)
    else:   
        command = '%s --version' % (tool)
        command_executer = os.system(command)

    if command_executer !=0:
        print colored("%s is not installed,let me install that for you master bruce" % (tool), 'blue')
        installer(tool=tool) 
    else:
        print colored("%s is already installed master bruce" % (tool), 'blue') 
    installation_notes_creator(tool=tool, directory=INSTALLATION_FOLDER, file=INSTALLATION_DETAILS_FILE)     
    time.sleep(5)    
    #ide checker
    command = '%s --version' % (JAVA_IDE)
    command_executer = os.system(command)
    if command_executer !=0:
        print colored("%s is not installed,let me install that for you master bruce" % (JAVA_IDE), 'blue')
        installer(tool=JAVA_IDE)    
       
def installer(tool=None):
    if tool == 'java':
        print colored("Installing java master bruce.....", "green")
        time.sleep(3)
        command = 'sudo apt-get install default-jre'    
        os.system(command)
        
    elif tool == 'eclipse':
        print colored("Installing eclipse master bruce....", "green")
        time.sleep(3)
        command = 'sudo apt-get install eclipse'    
        os.system(command)

def path_checker_and_setter(tool=None):
    # if tool == 'java':
    #     command = 'echo $JAVA_HOME'  
    #     command_executer = subprocess.check_output(command, shell=True) 
    #     if command_executer = '\n':
    #         command =  
    # return command_executer 
    if tool == 'java':
        command = 'which java'
        command_executer = subprocess.check_output(command, shell=True)
    return command_executer          

def installation_notes_creator(tool=None, directory=None, file=None):
    try:
        if not os.path.exists(directory):
            time.sleep(2)
            print colored("Creating directory for installation notes master bruce", "green")
            os.makedirs(os.path.join(HOME_PATH, directory))
            time.sleep(2)
            print colored("Directory named '%s' created, all the informations regarding installations will be in a file named '%s'" % (directory,file), "magenta") 
    except:
        pass
    #calling path checker function to get installed path    
    path_checker_function = path_checker(tool=tool)   
    file_opener = open(os.path.join(INSTALLATION_FOLDER_PATH, file), 'wb')
    content = """ 
    %s Details :
    ============
        Path    : %s  
    """ % (tool, path_checker_function)
    file_opener.write(content)
    file_opener.close()
    
if TOOLS == '1':
    print installation_checker("java")   

elif TOOLS == '2':
    print installation_checker("Android")

elif TOOLS == '3':
    print installation_checker("python")

elif TOOLS == '4':
    print installation_checker("webdevelopment")





#def installation_directory_checker(folder, home_path, installation_folder):
#    if not os.path.exists(folder):
#        director_creater = os.makedirs(os.path.join(HOME_PATH, INSTALLATION_FOLDER)
    #else:
    #    print "Installation notes will be in %s as %s" % (installation_folder, installation_file)

       
        



