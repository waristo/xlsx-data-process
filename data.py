import os
import numpy as np
import pandas as pd

def readExcel(fileList, searchFile, attD):
  for f in fileList :
    if (f.find(searchFile) != -1) and (f.find("$") == -1):
      excel = pd.read_excel(f)
      for row in excel.itertuples() :
        fn = str(row.파일명).replace("(","").replace(" ","_").replace(")","")
        # ko = str(row.한국어)
        en = str(row.영어)
        if fn in attD :
          # attD.get(fn)[0] += (" " + ko)
          attD.get(fn)[1] += (" " + en)
        else :
          attD[fn] = ["", en]
      attD = addKorean(attD, excel)
  return attD

def addKorean(attD, excel):
  flag = True
  for row in excel.itertuples() :
    if flag :
      flag = False  
      prvFolder = row.대화번호
      folder = "KOR_" + str(row.대화번호).rstrip().replace("(","").replace(" ","_").replace(")","")
      os.chdir(folder)
      prvFile = row.파일명
      fileName = str(row.파일명).replace("(","").replace(" ","_").replace(")","")
      try :
        f = open(fileName + ".txt", 'rt')
        attD.get(fileName)[0] = f.read()
      except FileNotFoundError:
        attD = checker1(fileName, attD)
        # attD = checker2(fileName, attD)
      except UnicodeDecodeError:
        f = open(fileName + ".txt", 'rt', encoding = 'UTF16')
        attD.get(fileName)[0] = f.read()
    if (prvFolder != row.대화번호) :
      prvFolder = row.대화번호
      folder = "KOR_" + str(row.대화번호).rstrip().replace("(","").replace(" ","_").replace(")","")
      if folder != "KOR_nan" :
        os.chdir("..")
        os.chdir(folder)

    if (prvFile != row.파일명) :
      prvFile = row.파일명
      fileName = str(row.파일명).replace("(","").replace(" ","_").replace(")","")
      try :
        f = open(fileName + ".txt", 'rt')
        attD.get(fileName)[0] = f.read()
      except FileNotFoundError:
        attD = checker1(fileName, attD)
        # attD = checker2(fileName, attD)
        # attD.get(fileName)[0] = "!!! FILE NOT FOUND !!!"
      except UnicodeDecodeError:
        f = open(fileName + ".txt", 'rt', encoding = 'UTF16')
        attD.get(fileName)[0] = f.read()
  os.chdir("..")
  return attD

def makeDict(dirList):
  attD = dict()
  for folder in dirList :
    if os.path.isdir(folder) and (folder.find(".") == -1) :
      os.chdir(folder)
      fileList = os.listdir(os.getcwd())
      attD = readExcel(fileList, ".new.xlsx", attD)

      os.chdir("..")
  return attD


def findNotFound(items, fileName) :
  f = open(fileName, "wt")
  for key, value in items:
    if value[0] == "!!! FILE NOT FOUND !!!":
      f.write(key + "\n")

def checker1(fileName, attD):
  fileList = os.listdir(os.getcwd())
  flag = True
  for f in fileList :
    if (fileName.replace("_","").replace("-","") + ".txt" == f.replace("_","").replace("-","")) :
      try :
        fd = open(f, 'rt')
        attD.get(fileName)[0] = fd.read()
      except UnicodeDecodeError:
        fd = open(f, 'rt', encoding = 'UTF16')
        attD.get(fileName)[0] = fd.read()
      flag = False
      break
  if flag :
    # print(fileName + "  :  " + fileName[-5:])
    attD.get(fileName)[0] = "!!! FILE NOT FOUND !!!"
  return attD

def checker2(fileName, attD):
  fileList = os.listdir(os.getcwd())
  flag = True
  for f in fileList :
    if (fileName[-5:] + ".txt" in f) :
      try :
        fd = open(f, 'rt')
        attD.get(fileName)[0] = fd.read()
      except UnicodeDecodeError:
        fd = open(f, 'rt', encoding = 'UTF16')
        attD.get(fileName)[0] = fd.read()
      flag = False
      break
  if flag :
    # print(fileName + "  :  " + fileName[-5:])
    attD.get(fileName)[0] = "!!! FILE NOT FOUND !!!"
  return attD

attD = makeDict(os.listdir(os.getcwd()))
# findNotFound(attD.items(), "checker1.txt")
# print(len(attD.keys()))
print(attD)