"""
   A program that reads an input file full of symbols, and computes a variable
   length code to represent the symbols.
   file: vlc.py
   author: Akshit Vinit Jain
   language: python3
   created: November 2014
"""
import turtle
import string

def init():
    """
    The init function intializes the turtle.
    :return None
    :rtype: NoneType
    
    """

    turtle.title("Histogram: Letter-Frequency")
    turtle.setup(900,550)
    turtle.ht()
    turtle.lt(180)
    turtle.speed(0)
    turtle.up()
    turtle.fd(250)
    turtle.rt(90)
    turtle.fd(180)
    turtle.rt(180)
    turtle.down()

def letterFreqPlot(freqList):
    """
    Plotting a histogram using the letter frquences of the correspnding letters
    sorted alphabetically in the freqList.
    :param freqList (list): A list of floating point values between 0.0 and 1.0.
                            The first entry corresponds to the letter 'a', the
                            second entry to the letter 'b', and so on.
    :return None, draws a histogram of letter frequencies.
    :rtype: NoneType
    
    """
    init()
    num = max(freqList)
    diff = str((max(freqList) - min(freqList))/10)
    diff = diff[:6]
    while num >= 0:
        dp_3 = str(num)
        dp_3 = dp_3[:5]
        turtle.rt(90)
        turtle.fd(20)
        turtle.write(dp_3, align="center", font=("Arial",12,"normal"))
        turtle.bk(20)
        turtle.lt(90)
        pos = turtle.pos()
        num -= float(diff)
        if num < 0:
            break
        turtle.fd(30)
    letterList = list(string.ascii_uppercase)
    while len(letterList) != 0:
        letter = letterList.pop(0)
        turtle.up()
        turtle.fd(20)
        turtle.lt(90)
        turtle.fd(20)
        turtle.write(letter, align="right", font=("",12,"normal"))
        turtle.bk(20)
        turtle.lt(90)
        turtle.fd(20)
        turtle.down()
        turtle.rt(90)
        turtle.fd(20)
        turtle.rt(90)
    turtle.lt(90)
    turtle.up()
    x,y = pos
    turtle.goto(x,y)
    turtle.rt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(300)
    turtle.write("Letter", align="right", font=("Verdana",14,"bold"))
    turtle.goto(x,y)
    turtle.bk(45)
    turtle.lt(90)
    turtle.fd(150)
    turtle.rt(90)
    turtle.write("Frequency", align="right", font=("Verdana",14,"bold"))
    turtle.goto(x,y)
    turtle.lt(90)
    turtle.fd(350)
    turtle.rt(90)
    turtle.fd(370)
    turtle.write("Letter Frequencies", align="right", font=("Verdana",18,"bold"))
    turtle.goto(x,y)
    turtle.down()
    turtle.color("black","blue")
    turtle.begin_fill()
    for freq in freqList:
        turtle.color("black","blue")
        turtle.begin_fill()
        maximumFreq = max(freqList)
        max_dp3 = str(maximumFreq)
        maximumFreq = float(max_dp3[:5])
        freq_dp_3 = str(freq)
        freq_dp_3 = float(freq_dp_3[:5])
        turtle.lt(90)
        turtle.fd((300/maximumFreq) * freq_dp_3)
        turtle.rt(90)
        turtle.fd(20)
        turtle.rt(90)
        turtle.fd((300/maximumFreq) * freq_dp_3)
        turtle.lt(90)
        turtle.end_fill()
       

