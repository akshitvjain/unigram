"""
   The main program for the second task to find the aggregate Word Counts.
   file: wordFreq.py
   author: Akshit Vinit Jain
   language: python3
   created: November 2014
"""
import wordData
import simplePlot

def swap(lst,i,j):
    """
    The function swaps the WordCount objects at pos i and j in the lst.
    :param lst (list): The list of WordCount objects
    :param i (int): The index of one datum
    :param j (int): The index of the other datum
    :return None
    :rtype: NoneType
    
    """
    hold = lst[i]
    lst[i] = lst[j]
    lst[j] = hold
    
def sort(lst):
    """
    The function sorts the WordCount objects by count using insertion sort.
    :param lst(list): The list of WordCount objects
    :return None
    :rtype: NoneType
    
    """
    for index in range(len(lst) - 1):
        while index > -1 and lst[index].count < lst[index + 1].count:
            swap(lst, index, index + 1)
            index -= 1
    
def wordFrequencies(words):
    """
    Creates a list of WordCount objects.
    :param words (dictionary): A dictionary mapping words to lists of YearCount
                               objects
    :return A list of WordCount objects in decreasing order from most to least
            frequent.
    :rtype: list
 
    """
    freqList = []
    for word in words:
        count = wordData.totalOccurrences(word, words)
        freqList.append(wordData.createWordCount(word, count))
    sort(freqList)
    return freqList

def main():
    """
    The main fucntion.
    :return None
    :rtype: NoneType

    """
    fileName = input("Enter word file: ")
    words = wordData.readWordFile(fileName)
    freqList = wordFrequencies(words)
    rank = int(input("Enter rank" + str((1,len(freqList))) + ":"))
    print("Rank",rank,":", freqList[rank - 1])
    simplePlot.wordFreqPlot(freqList)


if __name__ == '__main__':
    main()

    
