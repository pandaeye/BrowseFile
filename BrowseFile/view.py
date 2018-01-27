# coding=utf-8
from django.http import HttpResponse
import os
from django.shortcuts import render
from django.template import Context
import linecache

from chardet import detect
m_sTxtFile = ""
m_nCurrentPage = 0

def dir(rootDir):
    contentDic = {}
    listImages = []
    dicFolderAttribute = {}
    listTxts = []
    bHasImg = False
    bHasDir = False
    pathDir = os.listdir(rootDir)
    for allDir in pathDir:
        path = os.path.join(rootDir, allDir)
        if os.path.isdir(path):
            sDirFile = allDir.encode('utf-8')
            sAbsolutePath = path.encode('utf-8')
            dicFolderAttribute[sAbsolutePath.decode('utf-8')] = sDirFile.decode('utf-8')
        if os.path.isfile(path):
            if path.find(".txt") != -1:
                listTxts.append(path)
            elif path.find(".zip") != -1:
                pass
            elif path.find(".rar") != -1:
                pass
            else:
                nIndex = path.find('static')
                sImgfile = path[nIndex:]
                sImgfile = sImgfile.encode('utf-8')
                listImages.append(sImgfile.decode('utf-8'))
    contentDic['Path'] = rootDir
    contentDic['ImagesList'] = listImages
    contentDic['TxtList'] = listTxts
    contentDic['FolderAttributeDic'] = dicFolderAttribute
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

def OpenTxt(sTxtFile,nPage = 1):
    global m_sTxtFile
    global m_nCurrentPage
    contentDic = {}
    m_sTxtFile = sTxtFile
    m_nCurrentPage = nPage
    contentDic['title'] = sTxtFile
    nPageHasLine = 200
    sFileStr = linecache.getlines(sTxtFile)
    nPageNum = len(sFileStr) / nPageHasLine
    sTxt = ""
    for i in range((nPage - 1) * nPageHasLine, nPage * nPageHasLine):
        sTxt = sTxt + sFileStr[i] + "<BR>"
    contentDic['content'] = sTxt.decode('gbk').encode('utf-8')
    sPageInfo = str(nPage) + '/' + str(nPageNum)
    contentDic['PageInfo'] = sPageInfo
    return "Txts.html", contentDic

def OpenTxtPage(request):
    global m_nCurrentPage
    request.encoding = 'utf-8'
    if 'page' in request.GET:
        m_nCurrentPage = m_nCurrentPage + int(request.GET['page'].encode('utf-8'))
        nPage = m_nCurrentPage
    else:
        message = 'None'
        return HttpResponse(message)
    nPageHasLine = 200
    sFileStr = linecache.getlines(m_sTxtFile)
    nPageNum = len(sFileStr) / nPageHasLine
    sTxt = ""
    if nPage < 1:
        nPage = 1
    if nPage > nPageNum:
        nPage = nPageNum
    for i in range((nPage - 1) * nPageHasLine, nPage * nPageHasLine):
        sTxt = sTxt + sFileStr[i] + "<BR>"
    return HttpResponse(sTxt.decode('gbk').encode('utf-8'))

def first(request):
    rootDir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','static\\images'))
    contentDic = {}
    sHtmlFileName = 'Folders.html'
    if request.POST:
         if request.POST.keys()[0].find(".txt") != -1:
             sHtmlFileName,contentDic = OpenTxt(request.POST.keys()[0])
         else:
            rootDir = request.POST.keys()[0]
            contentDic = dir(rootDir)
    else:
        contentDic = dir(rootDir.decode('gbk'))
    return render(request,sHtmlFileName,contentDic)