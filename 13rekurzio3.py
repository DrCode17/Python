import os
import re

def makedir(eleresiUt):
    if len(eleresiUt) > len(os.getcwd()) + 10:
        return

    os.mkdir(eleresiUt+"/1")
    makedir(eleresiUt + "/1")
    os.mkdir(eleresiUt+"/2")
    makedir(eleresiUt + "/2")
    os.mkdir(eleresiUt+"/3")
    makedir(eleresiUt + "/3")

os.mkdir(os.getcwd()+"/mappaErdo")
os.chdir(os.getcwd()+"/mappaErdo")
makedir(os.getcwd())