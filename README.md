# unigram
Extract additional high level information from a dataset that contains the frequencies of words from various written sources. The dataset for this project contains data from the year 1800 to the year 2008. It is a subset of approximately 3 terabytes of data that was originally compiled by [Google](http://storage.googleapis.com/books/ngrams/books/datasetsv2.html).

The goal of this project is to obtain some new information from the available unigram dataset.

### Python Modules:
  - letterFreq.py: the relative letter frequencies of letters in the English language,
  - wordFreq.py: the aggregate word counts and the distribution of word frequencies, and
  - wordLength.py: the length of the average written word over the periods of time for
which data are available.

### Dataset:
Data format for .csv unigram files.   Each line has entries that are comma separated.

- The first entry in each row is the word.
- The second entry is the year.
- The third entry is the the number of times that the word appeared in any
book that year.
