#!/bin/python
import os, shutil
home = os.environ["HOME"]

def IfnotExistPathCreateIt(path):
	if not os.path.exists(path):
		os.makedirs(path)
		return True
	return False

"""check folders"""
print IfnotExistPathCreateIt("%s/.local/bin"%home)
shutil.copy2("./houdini","%s/.local/bin"%home)

print IfnotExistPathCreateIt("%s/.local/share/icons"%home)
shutil.copy2("./houdini_logo.png","%s/.local/share/icons"%home)
print IfnotExistPathCreateIt("%s/.local/share/applications"%home)
shutil.copy2("./notawhale_houdini.desktop","%s/.local/share/applications"%home)