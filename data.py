import os
import numpy as np
import pandas as pd

dirList = os.listdir(os.getcwd())

for folder in dirList :
  if os.path.isdir(folder) and (folder.find(".") == -1) :
    os.chdir(folder)
    fileList = os.listdir(os.getcwd())
    for f in fileList :
      if f.find(".xlsx") != -1 :
        excel = pd.read_excel(f)
    os.chdir("..")
    