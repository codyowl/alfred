import os
import subprocess



TOOLS = raw_input("""
		Please select a thing from the following to begin :
		1.Java
		2.Android
		3.C
		4.python
		""")

def installation_checker(tool):
	try:
		if tool == 'java':
			command = '%s -version' % (tool)
			os.system(command)
		else:   
			command = '%s --version' % (tool)
			os.system(command)
	except Exception:
		raise e

if TOOLS == '1':
	print installation_checker("R")    



