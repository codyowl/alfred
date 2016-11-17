import os
import subprocess
import time
from os.path import expanduser
from termcolor import colored
import getpass


USER_NAME = getpass.getuser()

HOME_PATH = expanduser("~/")

INSTALLATION_FOLDER = "Alfred"

INSTALLATION_FOLDER_PATH = HOME_PATH + INSTALLATION_FOLDER

INSTALLATION_DETAILS_FILE = "Installation_notes"

JAVA_IDE = "eclipse"

TOOLS = raw_input(
"""
Please select a thing from the following to begin setting up the environment master %s :
1.Java
2.Android
3.python
4.Apache-tomcat
5.editors
"""% (USER_NAME)) 

def installation_checker(tool):
    if tool == 'java':
        time.sleep(2)
        command = '%s -version' % (tool)
        command_executer = os.system(command)
        if command_executer !=0:
            print colored("%s is not installed,let me install that for you master %s" % (tool, USER_NAME), 'blue')
            installer(tool=tool) 
        else:
            print colored("%s is already installed master %s" % (tool,USER_NAME), 'blue') 
        time.sleep(2)
        #checking IDE
        command = '%s --version' % (JAVA_IDE)
        command_executer = os.system(command)
        if command_executer !=0:
            print colored("%s is not installed,let me install that for you master %s" % (JAVA_IDE, USER_NAME), 'blue')
            installer(tool=JAVA_IDE) 

        installation_notes_creator(tool=tool, directory=INSTALLATION_FOLDER, file=INSTALLATION_DETAILS_FILE)     
        time.sleep(5)   
    #for android    
    elif tool == 'Android':
        time.sleep(2)
        installer(tool=tool)    

    #for python
    elif tool == 'python':
        #checking pip
        time.sleep(2)
        print colored("Checking pip... master %s", "green") % (USER_NAME)
        pip_command = "pip list"
        pip_command_executer = os.system(pip_command)
        if pip_command_executer != 0:
            print colored("Pip is not installed, let me install that for you master %s", 'blue')%(USER_NAME)
            installer(tool='pip')

        #checking django
        time.sleep(2)
        print colored("Checking django .... master %s", "green") % (USER_NAME)
        django_command = "%s -c 'import django; print(django.get_version())'" % (tool)
        django_command_executer = os.system(django_command)
        if django_command_executer !=0:
            print colored("Django is not installed, let me install that for you master %s", 'blue') % (USER_NAME)
            installer(tool='django')
        else:
            print colored("Django is already here master %s.. you can check the installation notes for further details", 'green') % (USER_NAME)
        installation_notes_creator(tool=tool, directory=INSTALLATION_FOLDER, file=INSTALLATION_DETAILS_FILE)   
    #for tomcat 
    elif tool == 'Apache-tomcat':
        time.sleep(2)
        installer(tool=tool)

    #for editors
        #for sublime
    elif tool == 'sublime':
        time.sleep(2)
        command = "subl --version"
        command_executer = os.system(command)
        if command_executer != 0:
            print colored("Sublime is not installed, let me install that for your master %s", "blue") % (USER_NAME)
            installer(tool=sublime)
        else:
            print colored("Sublime is already here master %s... ") % (USER_NAME)                
    
    else:   
        command = '%s --version' % (tool)
        command_executer = os.system(command)


#Installer function
def installer(tool=None):
    if tool == 'java':
        print colored("Installing java master %s.....", "green") % (USER_NAME)
        time.sleep(3)
        command = 'sudo apt-get install default-jre'    
        os.system(command)
    elif tool == 'eclipse':
        print colored("Installing eclipse master %s....", "green") % (USER_NAME)
        time.sleep(3)
        command = 'sudo apt-get install eclipse'    
        os.system(command)
    elif tool == 'Android':
        print colored("Installing android studion master %s....", "green") % (USER_NAME)
        time.sleep(3)
        repository_command = 'sudo add-apt-repository ppa:ubuntu-desktop/ubuntu-make'
        update_command = 'sudo apt-get update'
        ubuntu_make_command = 'sudo apt-get install ubuntu-make'
        studio_command = 'umake android'
        os.system(repository_command)
        os.system(update_command)
        os.system(ubuntu_make_command)
        os.system(studio_command)    
    elif tool == 'Apache-tomcat':
        print colored("Installing apache tomcat server master %s...", "green") % (USER_NAME)
        time.sleep(3)
        update_command = 'sudo apt-get update'
        tomcat_command = 'sudo apt-get install tomcat7'
        os.system(update_command)
        os.system(tomcat_command)
    elif tool == 'pip':
        print colored("Installing pip master %s.....", "green") % (USER_NAME)
        time.sleep(3)
        update_command = 'sudo apt-get update'
        pip_command = 'sudo apt-get -y install python-pip'
        os.system(update_command)
        os.system(pip_command)     
    elif tool == 'django':
        print colored("Installing django master %s.....", "green") % (USER_NAME)
        time.sleep(3)
        command = 'pip install django'
        os.system(command) 
    
    #editors:
    elif tool == 'sublime':
        print colored("Installing %s master %s .....", "green") % (USER_NAME)
        time.sleep(3)
        ppa_command = "sudo add-apt-repository ppa:webupd8team/sublime-text-3"
        update_command = "sudo apt-get update"
        install_command = "sudo apt-get install sublime-text-installer"
        os.system(ppa_command)
        os.system(update_command)
        os.system(install_command)




def path_checker_and_setter(tool=None):
    # if tool == 'java':
    #     command = 'echo $JAVA_HOME'  
    #     command_executer = subprocess.check_output(command, shell=True) 
    #     if command_executer = '\n':
    #         command =  
    # return command_executer 
    if tool == 'java':
        command = 'which %s' % (tool)
        command_executer = subprocess.check_output(command, shell=True)
    elif tool == 'python':
        command = 'which %s' % (tool)
        command_executer = subprocess.check_output(command, shell=True)
    return command_executer            

def installation_notes_creator(tool=None, directory=None, file=None):
    try:
        if not os.path.exists(directory):
            time.sleep(2)
            print colored("Creating directory for installation notes master %s", "green") % (USER_NAME)
            os.makedirs(os.path.join(HOME_PATH, directory))
            time.sleep(2)
            print colored("Directory named '%s' created, all the informations regarding installations will be in a file named '%s'" % (directory,file), "magenta") 
    except:
        pass
    #calling path checker function to get installed path    
    path_checker_function = path_checker_and_setter(tool=tool)   
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
    print colored("Python is already here... master %s", "blue") % (USER_NAME)
    print installation_checker("python")  
    # path_checker_and_setter("python")

elif TOOLS == '4':
   print installation_checker("Apache-tomcat") 

elif TOOLS == '5':
   print colored("Please select an editor from the following editors.. master %s", "blue") % (USER_NAME)
   editors = raw_input(
"""
1.sublime
"""
)
   if editors == '1':
       print installation_checker("sublime")






       
        



