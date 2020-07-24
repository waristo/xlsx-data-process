import os

def toList(fileName):
  f = open(fileName, 'rt')
  fileList = []
  while True:
    line = f.readline()
    if not line :
      break
    fileList.append(line.replace('-KOR',' KOR').split(' ')[1])
  return fileList
  
def allfile(path):
  res = []
  for root, dirs, files in os.walk(path):
    for file in files:
      res.append(os.path.join(root, file))
  return res

def splitTxt(fileName):
  try:
    f = open(fileName, 'rt')
    targets = f.read().split('#')
    i = 0
    for target in targets:
      f2 = open(fileName.replace('.txt', '_cut') + str(i+1) + '.txt', 'wt')
      f2.write(target)
      i+=1
      # print(fileName.replace('.txt', '_cut') + str(i+1) + '.txt' + ' : ' + target)
      # i+=1
  except:
    print(fileName)

def splitAllText():
  fileList = allfile('.')
  targetList = toList('utt2dur_s_28_s')

  for target in targetList:
    location = ''
    for f in fileList:
      if target+'.txt' in f:
        location = f
        break
    if not location :
      print("can't find" + target)
    else:
      splitTxt(f)

def fileDelete():
  fileList = allfile('.')
  for file in fileList:
    if ('Section00' in file) or ('Turn00' in file):
      # print(file)
      os.remove(file)

def fileCheck():
  fileList = allfile('.')
  f = open('syncCheck.txt', 'wt')
  for file in fileList:
    if 'Sync00' in file:
      f.write(file + '\n')
def fileCheck2():
  f = open('syncCheck.txt', 'rt')
  lines = f.readlines()
  prev = 0
  for line in lines:
    number = int(line.split('Sync00')[-1][0])
    if ((number != 1) and (number != prev+1)):
      print(line)
    prev = number
    # print(number)

def syncToCut():
  fileList = allfile('.')
  for file in fileList:
    if 'Sync00' in file:
      try:
        cutIndex = file.index('_no_speaker')
        os.rename(file, file[:cutIndex].replace('Sync00','cut') + '.pcm')
        # print(file[:cutIndex].replace('Sync00','cut') + '.pcm')
      except:
        print(file)

def checker():
  fileList = allfile('.')
  for file in fileList:
    if '_cut' in file:
      if '.pcm' in file:
        if file.replace('.pcm','.txt') not in fileList:
          print(file)
      elif '.txt' in file:
        if file.replace('.txt','.pcm') not in fileList:
          print(file)

def txtView():
  fileList = allfile('.')
  for file in fileList:
    if ('_cut' in file) and ('.txt' in file):
      try:
        f = open(file, 'rt')
        print(file.split('\\')[-1])
        print(f.read())
      except:
        print(file)
        print('ERROR')
# splitAllText()
# fileDelete()
# fileCheck()
# fileCheck2()
# syncToCut()
# checker()
txtView()