"""
   A program to find the average word length over a period of time.
   file: wordLength.py
   author: Akshit Vinit Jain
   language: python3
   created: November 2014
"""
import wordData
import simplePlot


def occurrencesInYear(word, year, words):
    """
    Find the toal occurrences of the input word in the input year.
    :param word (str): The word in question passed in as str
    :param year (int): The year in question passed in as an int
    :param words (dictionary): A dictionary mapping words to lists of YearCount
                               objects
    :return The number of occurrences of the word in the year
    :rtype: integer (int)
    
    """
    occurrences = 0
    if word in words:
        for item in words[word]:
            if year == item.year:
                occurrences += item.count
                return occurrences
    return occurrences
                
def averageWordLength(year, words):
    """
    Find the average length of words in a given year.
    :param year (int): The year in question passed in as an int
    :param words (dictionary): A dictionary mapping words to lists of YearCount
                               objects
    :return The average word length for the year in question
    :rtype: float
    
    """
    totalWordOccur = 0
    totalWordLength = 0
    for word in words:
        if occurrencesInYear(word, year, words) != None:
            totalWordLength += len(word) * occurrencesInYear(word, year, words)
            totalWordOccur += occurrencesInYear(word, year, words)
    if totalWordOccur == 0:
        return totalWordOccur
    else:
        avgWordLength = totalWordLength/totalWordOccur
        return avgWordLength
    
        
def averageWordLengthYears(startYear, endYear, words):
    """
    Find the average length of words over a period of time.
    :param startYear (int): The start year
    :param endYear (int): The end year
    :param words (dictionary): A dictionary mapping words to lists of YearCount
                               objects
    :return The list of float's taht contain the average word lengths by year
            in the increasing order for years between startYear and endYear -
            both inclusive
    :rtype: list

    """
    avgList = []
    while startYear <= endYear:
        avgList.append(averageWordLength(startYear, words))
        startYear += 1
    return avgList

def main():
    """
    The main function.
    :return None
    :rtype: NoneType
    
    """
    fileName = input("Enter word file: ")
    word = input("Enter a word: ")
    year = int(input("Enter a year: "))
    words = wordData.readWordFile(fileName)
    totalOccur = occurrencesInYear(word, year, words)
    print("The word",'"',word,'"', "occurred", totalOccur, \
          "times in the year", year)
    year = int(input("Enter a year: "))
    avgWordLength = averageWordLength(year, words)
    print("The average word length for the year", year,\
          "is", avgWordLength, "letters")
    startYear = int(input("Enter a start year: "))
    endYear = int(input("Enter an end year: "))
    lengthsList = averageWordLengthYears(startYear, endYear, words)
    simplePlot.averageWordLengthPlot(startYear, endYear, lengthsList)
    
               

if __name__ == '__main__':
    main()

    
