for i in range(190000):
    takeOf = int(input("How many times did you take of: "))
    figure8 = int(input("How many times did you do the figure 8: "))
    bigHole = int(input("How many times did you fly through the big hole: "))
    smallHole = int(input("How many times did you fly through the small hole: "))
    yellowHoop = int(input("How many times did you fly through the yellow hoop: "))
    greenHoop = int(input("How many times did you fly through the green hoop: "))
    box = int(input("What box did you land on (1 for big, 2 for small, 0 for none):"))
    totalScore = str(takeOf*10 + figure8*40 + bigHole*20 + smallHole*40 + yellowHoop*15 + greenHoop*15 + box*20)
    playAgain=input("Your score was " + totalScore + " do you want to play again(0 for no and 1 for yes) : ")
    if(playAgain == 0):
        break