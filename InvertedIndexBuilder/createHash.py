#encoding=utf-8

import pickle
import cPickle
from news import News
from invertedIndex import InvertedIndex

def loadInvertedIndex():
    wordPosition = {}
    with open('Inverted Index.txt', 'r') as inputFile:
        prevOffset = inputFile.tell()
        line = inputFile.readline()
        while line.strip():
            head = line.strip().split(':')[0]
            word = unicode(head.split(',')[0], 'utf-8')
            wordPosition[word] = prevOffset
            prevOffset = inputFile.tell()
            line = inputFile.readline()
    return wordPosition

def saveFinalInvertedIndexAsFile():
    wordPosition = loadInvertedIndex()
    with open('Hash.obj', 'w') as outFile:
        cPickle.dump(wordPosition, outFile)
    print len(wordPosition)
    print 'save Hash OK.'

if __name__ == '__main__':
    saveFinalInvertedIndexAsFile()