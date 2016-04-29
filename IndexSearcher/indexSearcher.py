#encoding=utf-8

import cPickle
from InvertedIndexBuilder.invertedIndex import WordNode, InvertedIndex

class IndexSearcher:
    def __init__(self):
        with open('InvertedIndexBuilder/Hash.obj', 'r') as inFile:
            self.hash = cPickle.load(inFile)

    def search(self, someKey):
        offset = self.hash[someKey]
        with open('InvertedIndexBuilder/Inverted Index.txt', 'r') as inputFile:
            return self.readInvertedIndexInDiskForOneWord(inputFile, offset)

    def readInvertedIndexInDiskForOneWord(self, fileHandler, offset):
        fileHandler.seek(offset)
        line = fileHandler.readline()
        invertedInfomations = []
        wordInfo, wordNodeInfo = line.strip().split(':')
        word = wordInfo.split(',')[0]
        wordNodeStringArray = wordNodeInfo.split(';')
        for wordNodeString in wordNodeStringArray:
            docId, frequency, positionStr = wordNodeString.split('\t')
            docId = int(docId)
            frequency = int(frequency)
            wordNode = WordNode(word, docId, None, frequency)
            for pos in positionStr.split(','):
                wordNode.addPosition(int(pos))
            invertedInfomations.append(wordNode)
        return invertedInfomations