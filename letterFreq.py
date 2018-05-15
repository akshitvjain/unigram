"""
   The main program to compute the frequency of the letters and plot a
   histogram.
   file: letterFreq.py
   author: Akshit Vinit Jain
   language: python3
   created: November 2014
"""
import string
import wordData
import letterHist


def letterFreq(words):
    """
    Compute the letter frequency values.
    :param words (dictionary): A dictionary mapping words to lists of YearCount
                               objects
    :return: A list containing the relative frequency of letters scaled by the
             total letter count in alphabetical order.
    :rtype: list
    
    """
    letterDict = {}
    freqList = []
    letterList = list(string.ascii_lowercase)
    totalOccur = 0
    for word in words:
        totalOccur += len(word) * wordData.totalOccurrences(word, words)
        for item in word:
            if item not in letterDict:
                letterDict[item] = wordData.totalOccurrences(word, words)
            else:
                letterDict[item] += wordData.totalOccurrences(word, words)
    while len(letterList) != 0:
        letter = letterList.pop(0)
        if letter not in letterDict:
            freqList.append(float(0))
        else:
            freq = letterDict[letter] / totalOccur
            freqList.append(freq)
    return freqList


def main():
    """
    The main function.
    :return None
    :rtype: NoneType
    
    """
    fileName = input("Enter word file: ")
    word = input("Enter word: ")
    words = wordData.readWordFile(fileName)
    print("Total occurrences of", word, ":",
          wordData.totalOccurrences(word, words))
    freqList = letterFreq(words)
    print("Letter frequencies:", freqList)
    letterHist.letterFreqPlot(freqList)
    input("Hit Enter to EXIT")


if __name__ == '__main__':
    main()
        
