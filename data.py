import os
import numpy as np
import pandas as pd

def makeDict(dirList):
  attD = dict()
  for folder in dirList :
    if os.path.isdir(folder) and (folder.find(".") == -1) :
      os.chdir(folder)
      fileList = os.listdir(os.getcwd())
      for f in fileList :
        if (f.find(".new.xlsx") != -1) and (f.find("$") == -1):
          excel = pd.read_excel(f)
          for row in excel.itertuples() :
            fn = str(row.파일명)
            # ko = str(row.한국어)
            en = str(row.영어)
            if fn in attD :
              # attD.get(fn)[0] + ko
              attD.get(fn)[1] + en
            else :
              attD[fn] = ["", en]
      os.chdir("..")
  return attD

def addKorean(attD):
  pass

attD = makeDict(os.listdir(os.getcwd()))

  
print(attD)
    