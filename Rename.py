# coding=utf-8
import os

def Rename(rootDir):
  pathDir = os.listdir(rootDir)
  for allDir in pathDir:
    path = os.path.join(rootDir,allDir)
    if os.path.isdir(path):#目录
      Rename(path)
      if allDir.find("#") != -1:
        print(path)
        sNewFileName = path.replace("#", "")
        os.rename(path,sNewFileName)
        print(sNewFileName)

def main():
	rootDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'BrowseFile\\static\\images')
	Rename(rootDir)
main()