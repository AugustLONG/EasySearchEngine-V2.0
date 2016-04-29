#encoding=utf-8

import re
import pickle
import cPickle
from news import News
from invertedIndex import InvertedIndex

def buildInvertedIndex4ContentOfOneDoc(docId, unicodeText):
    textSize = len(unicodeText)
    #init inverted index
    invertedIndex = InvertedIndex()
    #handle english word
    englishWordMatchList = re.finditer(r'[a-zA-Z]+', unicodeText)
    for englishWordMatch in englishWordMatchList:
        word = englishWordMatch.group()
        position = englishWordMatch.span()
        invertedIndex.addWord(word, position[0], docId)
    #handle chinese word
    isChinese = lambda uchar: (uchar >= u'\u4e00' and uchar <= u'\u9fa5')
    i = 0
    while i < textSize - 1:
        while i < textSize - 1 and (not isChinese(unicodeText[i]) or not isChinese(unicodeText[i + 1])):
            i += 1
        if i < textSize - 1:
            word, position = unicodeText[i: i + 2], i
            invertedIndex.addWord(word, position, docId)
            i += 1
    #handle OK.
    return invertedIndex

def buildInvertedIndex4OneDoc(docPath, docId):
    with open(docPath, 'r') as inputFile:
        document = pickle.load(inputFile)
    content = document.title + unicode('。', 'utf-8') + document.content
    return buildInvertedIndex4ContentOfOneDoc(docId, content)

def buildInvertedIndex4Docs():
    print 'read in documents and build sub inverted index...'
    newsTypes = ['人才培养','学校要闻','校友之苑','理论学习','媒体看工大','他山之石','时势关注','校园文化','科研在线','国际合作','服务管理','深度策划','综合新闻']
    for newsType in newsTypes:
        with open('../DocumentsManager/Documents/%s/index.obj' % newsType, 'r') as inputFile:
            indexTuple = pickle.load(inputFile)
        with open('subInvertedIndex.txt', 'w') as outFile:
            for docId in range(indexTuple[0], indexTuple[1] + 1):
                path = '../DocumentsManager/Documents/%s/%d.obj' % (newsType, docId)
                currentInvertedIndex = buildInvertedIndex4OneDoc(path, docId)
                currentInvertedIndex.save2File(outFile)
    print 'read in documents and build sub inverted index OK.'

if __name__ == '__main__':
    buildInvertedIndex4Docs()