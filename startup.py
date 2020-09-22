import subprocess

subprocess.call("python model.py 200 20 30", shell = True)
# attempted to use sys.argv to read parameters from command line, 
# but could not get it to work