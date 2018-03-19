# coding=utf-8
from django.http import HttpResponse
import os
from django.shortcuts import render
from django.template import Context
import linecache
from database.models import folder_readed
from datetime import datetime, timedelta

from chardet import detect

m_sTxtFile = ""

def sort_fun(str):
    start = 0
    end = len(str)
    for i in range(end-1,0,-1):
        if str[i] >= '0' and str[i] <= '9':
            end = i
            break
    for i in range(end-1,0,-1):
        if str[i] < '0' or str[i] > '9':
            start = i+1
            break
    str = str[start:end+1]
    if len(str) == 0:
    	str = '0'
    return int(str)

def SaveCooie(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        rootDir = request.GET['q']
    else:
        message = 'None'
        return HttpResponse(message)
    # sTemp = ''
    # for c in rootDir:
    #     sTemp = sTemp + str(ord(c))
    # folder_readed.objects.create(folder=sTemp)
    folder_readed.objects.create(folder=rootDir)
    return HttpResponse("")

def dir(rootDir):
    contentDic = {}
    listImages = []
    FolderAttributeItems = []
    listTxts = []
    bHasImg = False
    bHasDir = False
    pathDir = os.listdir(rootDir)
    pathDir.sort(key= sort_fun)
    for allDir in pathDir:
        path = os.path.join(rootDir, allDir)
        if os.path.isdir(path):
            bHasDir = True
            sDirFile = allDir.encode('utf-8')
            sAbsolutePath = path.encode('utf-8')
            # sTemp = ''
            # for c in sDirFile:
            #     sTemp = sTemp + str(ord(c))
            # dataFolderReaded = folder_readed.objects.filter(folder=sTemp)  # 标记已经浏览过的内容
            dataFolderReaded = folder_readed.objects.filter(folder=sDirFile)  # 标记已经浏览过的内容
            if dataFolderReaded:
                FolderAttributeItems.append([sAbsolutePath.decode('utf-8'), sDirFile.decode('utf-8'),
                                             'width:500px;height:100px;background-color:#FF0000'])
            else:
                FolderAttributeItems.append(
                    [sAbsolutePath.decode('utf-8'), sDirFile.decode('utf-8'), 'width:500px;height:100px;'])
        if os.path.isfile(path):
            if path.find(".txt") != -1:
                listTxts.append(path)
            elif path.find(".zip") != -1:
                pass
            elif path.find(".rar") != -1:
                pass
            else:
                bHasImg = True
                nIndex = path.find('static')
                sImgfile = path[nIndex:]
                sImgfile = sImgfile.encode('utf-8')
                listImages.append(sImgfile.decode('utf-8'))
    contentDic['rootDir'] = rootDir
    contentDic['ImagesList'] = listImages
    contentDic['TxtList'] = listTxts
    contentDic['FolderAttributeItems'] = FolderAttributeItems
    contentDic['bHasImg'] = bHasImg
    contentDic['bHasDir'] = bHasDir
    return contentDic


def MarkDir(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        rootDir = request.GET['q']
    else:
        message = 'None'
        return HttpResponse(message)
    sNewFileName = rootDir + "_Save"
    os.rename(rootDir, sNewFileName)
    return HttpResponse("Marked")


def OpenTxt(sTxtFile, nPage=1):
    global m_sTxtFile
    contentDic = {}
    m_sTxtFile = sTxtFile
    contentDic['title'] = sTxtFile
    nPageHasLine = 200
    sFileStr = linecache.getlines(sTxtFile)
    nPageNum = len(sFileStr) / nPageHasLine + 1
    sTxt = ""
    nStart = (nPage - 1) * nPageHasLine
    nEnd = min(len(sFileStr), nPage * nPageHasLine)
    for i in range(nStart, nEnd):
        sTxt = sTxt + sFileStr[i] + "<BR>"
    contentDic['content'] = sTxt.decode('gbk').encode('utf-8')
    contentDic['CurrentPage'] = str(nPage)
    contentDic['PageNum'] = str(nPageNum)
    return "Txts.html", contentDic


def OpenTxtPage(request):
    request.encoding = 'utf-8'
    if 'page' in request.GET:
        nPage = int(request.GET['page'].encode('utf-8'))
    else:
        message = 'None'
        return HttpResponse(message)
    nPageHasLine = 200
    sFileStr = linecache.getlines(m_sTxtFile)
    nPageNum = len(sFileStr) / nPageHasLine + 1
    sTxt = ""
    nPage = max(nPage,1)
    nPage = min(nPage, nPageNum)
    nStartLine = (nPage - 1) * nPageHasLine
    nEndLine = min(nPage * nPageHasLine,len(sFileStr))
    for i in range(nStartLine, nEndLine):
        sTxt = sTxt + sFileStr[i] + "<BR>"
    return HttpResponse(sTxt.decode('gbk').encode('utf-8'))


def first(request):
    rootDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static\\images'))
    contentDic = {}
    sHtmlFileName = 'Folders.html'
    if request.POST:
        if request.POST.keys()[0].find(".txt") != -1:
            sHtmlFileName, contentDic = OpenTxt(request.POST.keys()[0])
        else:
            datetimeLastMonth = datetime.now().date() - timedelta(days=30)
            folder_readed.objects.filter(date__lt=datetimeLastMonth).delete()  # 每次第一次访问，删除已经过了一个月的数据
            rootDir = request.POST.keys()[0]
            contentDic = dir(rootDir)
    else:
        contentDic = dir(rootDir.decode('gbk'))
    return render(request, sHtmlFileName, contentDic)
