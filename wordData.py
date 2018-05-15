"""
   A supporting module used by letterFreq.py, wordFreq.py and wordLength.py
   file: wordData.py
   author: Akshit Vinit Jain
   language: python3
   created: November 2014
"""
from rit_object import *

class YearCount(rit_object):
    """
    Represents a single Year-Count type for a given word, composed of:
    :slot year (int): The year in which the word occured
    :slot count (int): The count of the word in that particular year
    
    """
    __slots__ = ('year', 'count')
    _types = (int, int)
    
    
def createYearCount(fields):
    """
    Initialize and return a new YearCount object.
    :param fields (list of str): A list of strings that represent one line
        in the file.
    :return: the new YearCount object
    :rtype: YearCount
    
    """
    year = int(fields[1])
    count = int(fields[2])
    return YearCount(year,count)


class WordCount(rit_object):
    """
    Represents a single Word-Count type, composed of:
    :slot word (str): The name of word
    :slot count (int): The total count for the word
    
    """
    __slots__ = ('word', 'count')
    _types = (str, int)
    

def createWordCount(word, count):
    """
    Create and return a new WordCount object.
    :param word (str): The name of word
    :param count (int): The total count for the word
    :return: A newly initialized WordCount object
    :rtype: WordCount
    
    """
    return WordCount(word, count)


def readWordFile(fileName):
    """
    Read the entire unigram dataset whose format is:
        word year count
    :param fileName (str): The name of the file
    :return: A dictionary mapping words to lists of YearCount objects
    :rtype: dictionary

    """
    fileName = "data/" + fileName
    words = {}
    for line in open(fileName):
        fields = line.split(',')
        if fields[0] not in words:
            words[fields[0]] = [createYearCount(fields)]
        else:
            words[fields[0]] += [createYearCount(fields)]
    return words

def totalOccurrences(word, words):
    """
    Find the total number of times a word appeared in a given dataset.
    :param word (str): The word for which to calculate the count
    :param words (dictionary): A dictionary mapping words to lists of YearCount
                               objects
    :return: A totalCount of the occurrences of the word
    :rtype: integer (int)
    """
    totalCount = 0
    if word in words:
        for item in words[word]:
            totalCount += item.count
    return totalCount

