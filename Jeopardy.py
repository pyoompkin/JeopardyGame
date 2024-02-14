from graphics import *
import time, random

win = GraphWin('Jeopardy', 1000, 1000)
win.yUp()
win.setBackground('blue')
       
#Menu Jeopardy Text
winCenter = Point(win.getWidth()/2, 800)
header = Text(winCenter, 'JEOPARDY')
header.setSize(36)
header.setStyle('bold')
header.draw(win)

#Menu 'click anywhere to begin' text
underHeader = Text(Point(win.getWidth()/2, 500), 'Click anywhere to begin')
underHeader.setSize(25)
underHeader.setStyle('italic')
underHeader.draw(win)

#Transition from menu to start game
win.getMouse()
underHeader.undraw()
for movement in range(5):
    header.move(0, 30)
    time.sleep(0.3)

#Extra colors
darkBlue = color_rgb(24, 0, 158)
yellow = color_rgb(236, 247, 22)

#List of clicked boxes
boxesClicked = list()

#Functions
def categoryBox(point1x, point1y, point2x, point2y):
    for box in range(4):
        category = Rectangle(Point(point1x, point1y), Point(point2x, point2y))
        category.setFill(darkBlue)
        category.draw(win)
        
def pointsText(x, y, amount):
    amount = 100
    for text in range(3):
        points_Text = Text(Point(x, y), '{}'.format(amount))
        points_Text.setTextColor(yellow)
        points_Text.setSize(30)
        points_Text.setStyle('bold')
        points_Text.draw(win)
        amount = amount + 100
        y = y - 195

def isBetween(x, end1, end2):
    return end1 <= x <= end2 or end2 <= x <= end1

def isInside(point, rect):
    pt1 = rect.getP1()
    pt2 = rect.getP2()
    return isBetween(point.getX(), pt1.getX(), pt2.getX()) and \
           isBetween(point.getY(), pt1.getY(), pt2.getY())

def undrawAnimation():
    category1text.undraw()
    category1text2.undraw()
    category1_title.undraw()
    time.sleep(0.1)
    
    category2text.undraw()
    category2text2.undraw()
    category2text3.undraw()
    category2_title.undraw()
    time.sleep(0.1)

    cat1PointsText100.undraw()
    category1_100.undraw()
    time.sleep(0.1)

    category3text.undraw()
    category3_title.undraw()
    time.sleep(0.1)

    cat2PointsText100.undraw()
    category2_100.undraw()
    time.sleep(0.1)

    cat1PointsText200.undraw()
    category1_200.undraw()
    time.sleep(0.1)

    category4text.undraw()
    category4_title.undraw()
    time.sleep(0.1)

    cat3PointsText100.undraw()
    category3_100.undraw()
    time.sleep(0.1)

    cat2PointsText200.undraw()
    category2_200.undraw()
    time.sleep(0.1)

    cat1PointsText300.undraw()
    category1_300.undraw()
    time.sleep(0.1)

    cat4PointsText100.undraw()
    category4_100.undraw()
    time.sleep(0.1)

    cat3PointsText200.undraw()
    category3_200.undraw()
    time.sleep(0.1)

    cat2PointsText300.undraw()
    category2_300.undraw()
    time.sleep(0.1)

    cat4PointsText200.undraw()
    category4_200.undraw()
    time.sleep(0.1)

    cat3PointsText300.undraw()
    category3_300.undraw()
    time.sleep(0.1)

    cat4PointsText300.undraw()
    category4_300.undraw()
    time.sleep(0.1)

    instructions.undraw()

def drawAnimation():
    category1_title.draw(win)
    category1text.draw(win)
    category1text2.draw(win)
    time.sleep(0.1)

    category2_title.draw(win)
    category2text.draw(win)
    category2text2.draw(win)
    category2text3.draw(win)
    time.sleep(0.1)

    category1_100.draw(win)
    cat1PointsText100.draw(win)
    time.sleep(0.1)

    category3_title.draw(win)
    category3text.draw(win)
    time.sleep(0.1)

    category2_100.draw(win)
    cat2PointsText100.draw(win)
    time.sleep(0.1)

    category1_200.draw(win)
    cat1PointsText200.draw(win)
    time.sleep(0.1)

    category4_title.draw(win)
    category4text.draw(win)
    time.sleep(0.1)

    category3_100.draw(win)
    cat3PointsText100.draw(win)
    time.sleep(0.1)

    category2_200.draw(win)
    cat2PointsText200.draw(win)
    time.sleep(0.1)

    category1_300.draw(win)
    cat1PointsText300.draw(win)
    time.sleep(0.1)

    category4_100.draw(win)
    cat4PointsText100.draw(win)
    time.sleep(0.1)

    category3_200.draw(win)
    cat3PointsText200.draw(win)
    time.sleep(0.1)

    category2_300.draw(win)
    cat2PointsText300.draw(win)
    time.sleep(0.1)

    category4_200.draw(win)
    cat4PointsText200.draw(win)
    time.sleep(0.1)

    category3_300.draw(win)
    cat3PointsText300.draw(win)
    time.sleep(0.1)

    category4_300.draw(win)
    cat4PointsText300.draw(win)
    time.sleep(0.1)

    instructions.draw(win)
    
#Category 1
'category boxes'
category1_title = Rectangle(Point(25, 900), Point(240, 730))
category1_title.setFill(darkBlue)
category1_title.draw(win)

category1_100 = Rectangle(Point(25, 705), Point(240, 535))
category1_100.setFill(darkBlue)
category1_100.draw(win)

category1_200 = Rectangle(Point(25, 510), Point(240, 340))
category1_200.setFill(darkBlue)
category1_200.draw(win)

category1_300 = Rectangle(Point(25, 315), Point(240, 145))
category1_300.setFill(darkBlue)
category1_300.draw(win)

'category type text'
category1text = Text(Point(133, 850), 'Movie')
category1text2 = Text(Point(133, 790), 'Quotes')
category1text.setTextColor(yellow)
category1text.setSize(30)
category1text.setStyle('bold')
category1text.draw(win)
category1text2.setTextColor(yellow)
category1text2.setSize(30)
category1text2.setStyle('bold')
category1text2.draw(win)

'category points text'
cat1PointsText100 = Text(Point(133, 620), '100')
cat1PointsText100.setTextColor(yellow)
cat1PointsText100.setSize(30)
cat1PointsText100.setStyle('bold')
cat1PointsText100.draw(win)

cat1PointsText200 = Text(Point(133, 430), '200')
cat1PointsText200.setTextColor(yellow)
cat1PointsText200.setSize(30)
cat1PointsText200.setStyle('bold')
cat1PointsText200.draw(win)

cat1PointsText300 = Text(Point(133, 240), '300')
cat1PointsText300.setTextColor(yellow)
cat1PointsText300.setSize(30)
cat1PointsText300.setStyle('bold')
cat1PointsText300.draw(win)

#Category 2
'category boxes'
category2_title = Rectangle(Point(265, 900), Point(485, 730))
category2_title.setFill(darkBlue)
category2_title.draw(win)

category2_100 = Rectangle(Point(265, 705), Point(485, 535))
category2_100.setFill(darkBlue)
category2_100.draw(win)

category2_200 = Rectangle(Point(265, 510), Point(485, 340))
category2_200.setFill(darkBlue)
category2_200.draw(win)

category2_300 = Rectangle(Point(265, 315), Point(485, 145))
category2_300.setFill(darkBlue)
category2_300.draw(win)

'category type text'
category2text = Text(Point(375, 860), 'Food')
category2text2 = Text(Point(380, 810), '&')
category2text3 = Text(Point(375, 765), 'Drink')
category2text.setTextColor(yellow)
category2text.setSize(30)
category2text.setStyle('bold')
category2text.draw(win)
category2text2.setTextColor(yellow)
category2text2.setSize(30)
category2text2.setStyle('bold')
category2text2.draw(win)
category2text3.setTextColor(yellow)
category2text3.setSize(30)
category2text3.setStyle('bold')
category2text3.draw(win)

'category points text'
cat2PointsText100 = Text(Point(375, 620), '100')
cat2PointsText100.setTextColor(yellow)
cat2PointsText100.setSize(30)
cat2PointsText100.setStyle('bold')
cat2PointsText100.draw(win)

cat2PointsText200 = Text(Point(375, 430), '200')
cat2PointsText200.setTextColor(yellow)
cat2PointsText200.setSize(30)
cat2PointsText200.setStyle('bold')
cat2PointsText200.draw(win)

cat2PointsText300 = Text(Point(375, 240), '300')
cat2PointsText300.setTextColor(yellow)
cat2PointsText300.setSize(30)
cat2PointsText300.setStyle('bold')
cat2PointsText300.draw(win)

#Category 3
'category boxes'
category3_title = Rectangle(Point(510, 900), Point(730, 730))
category3_title.setFill(darkBlue)
category3_title.draw(win)

category3_100 = Rectangle(Point(510, 705), Point(730, 535))
category3_100.setFill(darkBlue)
category3_100.draw(win)

category3_200 = Rectangle(Point(510, 510), Point(730, 340))
category3_200.setFill(darkBlue)
category3_200.draw(win)

category3_300 = Rectangle(Point(510, 315), Point(730, 145))
category3_300.setFill(darkBlue)
category3_300.draw(win)

'category type text'
category3text = Text(Point(620, 820), 'Science')
category3text.setTextColor(yellow)
category3text.setSize(30)
category3text.setStyle('bold')
category3text.draw(win)

'category points text'
cat3PointsText100 = Text(Point(620, 620), '100')
cat3PointsText100.setTextColor(yellow)
cat3PointsText100.setSize(30)
cat3PointsText100.setStyle('bold')
cat3PointsText100.draw(win)

cat3PointsText200 = Text(Point(620, 430), '200')
cat3PointsText200.setTextColor(yellow)
cat3PointsText200.setSize(30)
cat3PointsText200.setStyle('bold')
cat3PointsText200.draw(win)

cat3PointsText300 = Text(Point(620, 240), '300')
cat3PointsText300.setTextColor(yellow)
cat3PointsText300.setSize(30)
cat3PointsText300.setStyle('bold')
cat3PointsText300.draw(win)

#Category 4
'category boxes'
category4_title = Rectangle(Point(755, 900), Point(975, 730))
category4_title.setFill(darkBlue)
category4_title.draw(win)

category4_100 = Rectangle(Point(755, 705), Point(975, 535))
category4_100.setFill(darkBlue)
category4_100.draw(win)

category4_200 = Rectangle(Point(755, 510), Point(975, 340))
category4_200.setFill(darkBlue)
category4_200.draw(win)

category4_300 = Rectangle(Point(755, 315), Point(975, 145))
category4_300.setFill(darkBlue)
category4_300.draw(win)

'category type text'
category4text = Text(Point(865, 820), 'Random')
category4text.setTextColor(yellow)
category4text.setSize(30)
category4text.setStyle('bold')
category4text.draw(win)

'category points text'
cat4PointsText100 = Text(Point(865, 620), '100')
cat4PointsText100.setTextColor(yellow)
cat4PointsText100.setSize(30)
cat4PointsText100.setStyle('bold')
cat4PointsText100.draw(win)

cat4PointsText200 = Text(Point(865, 430), '200')
cat4PointsText200.setTextColor(yellow)
cat4PointsText200.setSize(30)
cat4PointsText200.setStyle('bold')
cat4PointsText200.draw(win)

cat4PointsText300 = Text(Point(865, 240), '300')
cat4PointsText300.setTextColor(yellow)
cat4PointsText300.setSize(30)
cat4PointsText300.setStyle('bold')
cat4PointsText300.draw(win)

#Info box
infoBox = Rectangle(Point(25, 120), Point(975, 25))
infoBox.setFill(darkBlue)
infoBox.draw(win)

instructions = Text(Point(win.getWidth()/2, 95), 'Select a box to be given a trivia question. The more points, the harder the question will be. \n The game ends when you gain 1500 points or all the questions have been answered.')
instructions.setStyle('italic')
instructions.setTextColor('yellow')
instructions.draw(win)

totalScore = 0

scoreText = Text(Point(win.getWidth()/2, 50), 'Score: {}'.format(totalScore))
scoreText.setTextColor('white')
scoreText.setStyle('bold')
scoreText.setSize(15)
scoreText.draw(win)

newInstructions = Text(Point(win.getWidth()/2, 110), 'Select which answer you think is correct.')
newInstructions.setStyle('italic')
newInstructions.setTextColor('yellow')

#All boxes = False
category1_100test = False
category1_200test = False
category1_300test = False
category2_100test = False
category2_200test = False
category2_300test = False
category3_100test = False
category3_200test = False
category3_300test = False
category4_100test = False
category4_200test = False
category4_300test = False

#Turn 1
for mouseClick in range(100):
   if totalScore >= 1500 or category1_100test == True and category1_200test == True and category1_300test == True and category2_100test == True and category2_200test == True and category2_300test == True and category3_100test == True and category3_200test == True and category3_300test == True and category4_100test == True and category4_200test == True and category4_300test == True:
      undrawAnimation()
      infoBox.undraw()
      scoreText.undraw()
      finalScore = Text(Point(win.getWidth()/2, 700), "Congratulations! Your final score is:")
      finalScore1 = Text(Point(win.getWidth()/2, 600), "{}".format(totalScore))
      finalScore2 = Text(Point(win.getWidth()/2, 500), "Thanks for playing!")
      finalScore3 = Text(Point(win.getWidth()/2, 400), "Click anywhere to end the game")
      finalScore.setSize(36)
      finalScore.setStyle('bold')
      finalScore1.setSize(36)
      finalScore1.setTextColor('yellow')
      finalScore1.setStyle('bold')
      finalScore2.setSize(36)
      finalScore2.setStyle('bold')
      finalScore2.setSize(36)
      finalScore2.setStyle('bold')
      finalScore3.setSize(25)
      finalScore3.setStyle('italic')
      finalScore.draw(win)
      time.sleep(1)
      finalScore1.draw(win)
      time.sleep(1)
      finalScore2.draw(win)
      time.sleep(1)
      finalScore3.draw(win)
      win.getMouse()
      win.close()

   pt = win.getMouse()

   #category 1 100pts
   if isInside(pt, category1_100):
       if not category1_100test:
          boxesClicked.append(cat1PointsText100)
          undrawAnimation()
          
          'instructions'
          newInstructions.setText('Select which answer you think is correct.')
          newInstructions.draw(win)
          
          'question'
          cat1_100question = Text(Point(win.getWidth()/2, 700), '“Toto, I’ve a feeling we’re')
          cat1_100question1 = Text(Point(win.getWidth()/2, 650), 'not in Kansas anymore.”')
          cat1_100question2 = Text(Point(win.getWidth()/2, 600), 'is a quote from which movie?')
          cat1_100question.setSize(36)
          cat1_100question.setStyle('bold')
          cat1_100question.draw(win)
          cat1_100question1.setSize(36)
          cat1_100question1.setStyle('bold')
          cat1_100question1.draw(win)
          cat1_100question2.setSize(36)
          cat1_100question2.draw(win)
          
          'answers'
          cat1_100answerA = Text(Point(win.getWidth()/2, 500), 'A) Indiana Jones')
          cat1_100answerAclick = Rectangle(Point(335, 530), Point(665, 470))
          
          cat1_100answerB = Text(Point(win.getWidth()/2, 400), 'B) Uncharted')
          cat1_100answerBclick = Rectangle(Point(335, 430), Point(665, 370))
          
          cat1_100answerC = Text(Point(win.getWidth()/2, 300), 'C) Interstellar')
          cat1_100answerCclick = Rectangle(Point(335, 330), Point(665, 270))
          
          cat1_100answerD = Text(Point(win.getWidth()/2, 200), 'D) The Wizard of Oz')
          cat1_100answerDclick = Rectangle(Point(335, 230), Point(665, 170))

          cat1_100answerAclick.setFill('darkBlue')
          cat1_100answerAclick.draw(win)
          cat1_100answerBclick.setFill('darkBlue')
          cat1_100answerBclick.draw(win)
          cat1_100answerCclick.setFill('darkBlue')
          cat1_100answerCclick.draw(win)
          cat1_100answerDclick.setFill('darkBlue')
          cat1_100answerDclick.draw(win)
          cat1_100answerA.setSize(25)
          cat1_100answerA.draw(win)
          cat1_100answerB.setSize(25)
          cat1_100answerB.draw(win)
          cat1_100answerC.setSize(25)
          cat1_100answerC.draw(win)
          cat1_100answerD.setSize(25)
          cat1_100answerD.draw(win)
          
          for mouseClick in range(100):
             pt = win.getMouse()
             
             if isInside(pt, cat1_100answerAclick):
                 cat1_100answerA.setTextColor('red')
                 cat1_100answerB.setTextColor('red')
                 cat1_100answerC.setTextColor('red')
                 cat1_100answerD.setTextColor('green')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat1_100answerBclick):
                 cat1_100answerA.setTextColor('red')
                 cat1_100answerB.setTextColor('red')
                 cat1_100answerC.setTextColor('red')
                 cat1_100answerD.setTextColor('green')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat1_100answerCclick):
                 cat1_100answerA.setTextColor('red')
                 cat1_100answerB.setTextColor('red')
                 cat1_100answerC.setTextColor('red')
                 cat1_100answerD.setTextColor('green')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat1_100answerDclick):
                 cat1_100answerA.setTextColor('red')
                 cat1_100answerB.setTextColor('red')
                 cat1_100answerC.setTextColor('red')
                 cat1_100answerD.setTextColor('green')
                 totalScore = totalScore + 100
                 scoreText.setText('Score: {}'.format(totalScore))
                 newInstructions.setText('Congratulations, that is correct! Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             else:
                 continue
               
          'undraw'
          cat1_100question.undraw()
          time.sleep(0.1)
          cat1_100question1.undraw()
          time.sleep(0.1)
          cat1_100question2.undraw()
          time.sleep(0.1)
          cat1_100answerA.undraw()
          cat1_100answerAclick.undraw()
          time.sleep(0.1)
          cat1_100answerB.undraw()
          cat1_100answerBclick.undraw()
          time.sleep(0.1)
          cat1_100answerC.undraw()
          cat1_100answerCclick.undraw()
          time.sleep(0.1)
          cat1_100answerD.undraw()
          cat1_100answerDclick.undraw()
          time.sleep(0.1)
          newInstructions.undraw()
          
          'draw'
          drawAnimation()
          for boxes in boxesClicked:
              boxes.undraw()
              time.sleep(0.1)
          category1_100test = True
          
       else:
          continue
              
   #category 1 200 pts
   elif isInside(pt, category1_200):
       if not category1_200test:
          boxesClicked.append(cat1PointsText200)
          undrawAnimation()
          
          'instructions'
          newInstructions.setText('Select which answer you think is correct.')
          newInstructions.draw(win)
          
          'question'
          cat1_200question = Text(Point(win.getWidth()/2, 700), 'Fill in the blank:')
          cat1_200question1 = Text(Point(win.getWidth()/2, 650), '“You’re gonna need a ____”')
          cat1_200question2 = Text(Point(win.getWidth()/2, 600), '-Jaws, 1975')
          cat1_200question.setSize(36)
          cat1_200question.setStyle('bold')
          cat1_200question.draw(win)
          cat1_200question1.setSize(36)
          cat1_200question1.draw(win)
          cat1_200question2.setSize(30)
          cat1_200question2.setStyle('italic')
          cat1_200question2.draw(win)
          
          'answers'
          cat1_200answerA = Text(Point(win.getWidth()/2, 500), 'A) Bigger ship')
          cat1_200answerAclick = Rectangle(Point(390, 530), Point(610, 470))
          
          cat1_200answerB = Text(Point(win.getWidth()/2, 400), 'B) Bigger boat')
          cat1_200answerBclick = Rectangle(Point(390, 430), Point(610, 370))
          
          cat1_200answerC = Text(Point(win.getWidth()/2, 300), 'C) Bigger net')
          cat1_200answerCclick = Rectangle(Point(390, 330), Point(610, 270))
          
          cat1_200answerD = Text(Point(win.getWidth()/2, 200), 'D) Bigger gun')
          cat1_200answerDclick = Rectangle(Point(390, 230), Point(610, 170))

          cat1_200answerAclick.setFill('darkBlue')
          cat1_200answerAclick.draw(win)
          cat1_200answerBclick.setFill('darkBlue')
          cat1_200answerBclick.draw(win)
          cat1_200answerCclick.setFill('darkBlue')
          cat1_200answerCclick.draw(win)
          cat1_200answerDclick.setFill('darkBlue')
          cat1_200answerDclick.draw(win)
          cat1_200answerA.setSize(25)
          cat1_200answerA.draw(win)
          cat1_200answerB.setSize(25)
          cat1_200answerB.draw(win)
          cat1_200answerC.setSize(25)
          cat1_200answerC.draw(win)
          cat1_200answerD.setSize(25)
          cat1_200answerD.draw(win)
          
          for mouseClick in range(100):
             pt = win.getMouse()
             
             if isInside(pt, cat1_200answerAclick):
                 cat1_200answerA.setTextColor('red')
                 cat1_200answerB.setTextColor('green')
                 cat1_200answerC.setTextColor('red')
                 cat1_200answerD.setTextColor('red')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 win.getMouse()
                 break
             elif isInside(pt, cat1_200answerBclick):
                 cat1_200answerA.setTextColor('red')
                 cat1_200answerB.setTextColor('green')
                 cat1_200answerC.setTextColor('red')
                 cat1_200answerD.setTextColor('red')
                 totalScore = totalScore + 200
                 scoreText.setText('Score: {}'.format(totalScore))
                 newInstructions.setText('Congratulations, that is correct! Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat1_200answerCclick):
                 cat1_200answerA.setTextColor('red')
                 cat1_200answerB.setTextColor('green')
                 cat1_200answerC.setTextColor('red')
                 cat1_200answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat1_200answerDclick):
                 cat1_200answerA.setTextColor('red')
                 cat1_200answerB.setTextColor('green')
                 cat1_200answerC.setTextColor('red')
                 cat1_200answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             else:
                 continue
               
          'undraw'
          cat1_200question.undraw()
          time.sleep(0.1)
          cat1_200question1.undraw()
          time.sleep(0.1)
          cat1_200question2.undraw()
          time.sleep(0.1)
          cat1_200answerA.undraw()
          cat1_200answerAclick.undraw()
          time.sleep(0.1)
          cat1_200answerB.undraw()
          cat1_200answerBclick.undraw()
          time.sleep(0.1)
          cat1_200answerC.undraw()
          cat1_200answerCclick.undraw()
          time.sleep(0.1)
          cat1_200answerD.undraw()
          cat1_200answerDclick.undraw()
          time.sleep(0.1)
          newInstructions.undraw()
          
          'draw'
          drawAnimation()
          for boxes in boxesClicked:
              boxes.undraw()
              time.sleep(0.1)
          category1_200test = True
          
       else:
          continue

   #category 1 300 pts
   elif isInside(pt, category1_300):
       if not category1_300test:
          boxesClicked.append(cat1PointsText300)
          undrawAnimation()
          
          'instructions'
          newInstructions.setText('Select which answer you think is correct.')
          newInstructions.draw(win)
          
          'question'
          cat1_300question = Text(Point(win.getWidth()/2, 700), 'Fill in the blank:')
          cat1_300question1 = Text(Point(win.getWidth()/2, 650), '“____ on the wall, who is the fairest one of all?”')
          cat1_300question2 = Text(Point(win.getWidth()/2, 600), '-Snow White and the Seven Dwarfs')
          cat1_300question.setSize(36)
          cat1_300question.setStyle('bold')
          cat1_300question.draw(win)
          cat1_300question1.setSize(34)
          cat1_300question1.draw(win)
          cat1_300question2.setSize(28)
          cat1_300question2.setStyle('italic')
          cat1_300question2.draw(win)
          
          'answers'
          cat1_300answerA = Text(Point(win.getWidth()/2, 500), 'A) Magic Mirror')
          cat1_300answerAclick = Rectangle(Point(335, 530), Point(665, 470))
          
          cat1_300answerB = Text(Point(win.getWidth()/2, 400), 'B) Mirror mirror')
          cat1_300answerBclick = Rectangle(Point(335, 430), Point(665, 370))
          
          cat1_300answerC = Text(Point(win.getWidth()/2, 300), 'C) Marvelous mirror')
          cat1_300answerCclick = Rectangle(Point(335, 330), Point(665, 270))
          
          cat1_300answerD = Text(Point(win.getWidth()/2, 200), 'D) Mysterious mirror')
          cat1_300answerDclick = Rectangle(Point(335, 230), Point(665, 170))

          cat1_300answerAclick.setFill('darkBlue')
          cat1_300answerAclick.draw(win)
          cat1_300answerBclick.setFill('darkBlue')
          cat1_300answerBclick.draw(win)
          cat1_300answerCclick.setFill('darkBlue')
          cat1_300answerCclick.draw(win)
          cat1_300answerDclick.setFill('darkBlue')
          cat1_300answerDclick.draw(win)
          cat1_300answerA.setSize(25)
          cat1_300answerA.draw(win)
          cat1_300answerB.setSize(25)
          cat1_300answerB.draw(win)
          cat1_300answerC.setSize(25)
          cat1_300answerC.draw(win)
          cat1_300answerD.setSize(25)
          cat1_300answerD.draw(win)
          
          for mouseClick in range(100):
             pt = win.getMouse()
             
             if isInside(pt, cat1_300answerAclick):
                 cat1_300answerA.setTextColor('green')
                 cat1_300answerB.setTextColor('red')
                 cat1_300answerC.setTextColor('red')
                 cat1_300answerD.setTextColor('red')
                 newInstructions.setText('Congratulations, that is correct! Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 totalScore = totalScore + 300
                 scoreText.setText('Score: {}'.format(totalScore))
                 win.getMouse()
                 break
             elif isInside(pt, cat1_300answerBclick):
                 cat1_300answerA.setTextColor('green')
                 cat1_300answerB.setTextColor('red')
                 cat1_300answerC.setTextColor('red')
                 cat1_300answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat1_300answerCclick):
                 cat1_300answerA.setTextColor('green')
                 cat1_300answerB.setTextColor('red')
                 cat1_300answerC.setTextColor('red')
                 cat1_300answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat1_300answerDclick):
                 cat1_300answerA.setTextColor('green')
                 cat1_300answerB.setTextColor('red')
                 cat1_300answerC.setTextColor('red')
                 cat1_300answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             else:
                 continue
               
          'undraw'
          cat1_300question.undraw()
          time.sleep(0.1)
          cat1_300question1.undraw()
          time.sleep(0.1)
          cat1_300question2.undraw()
          time.sleep(0.1)
          cat1_300answerA.undraw()
          cat1_300answerAclick.undraw()
          time.sleep(0.1)
          cat1_300answerB.undraw()
          cat1_300answerBclick.undraw()
          time.sleep(0.1)
          cat1_300answerC.undraw()
          cat1_300answerCclick.undraw()
          time.sleep(0.1)
          cat1_300answerD.undraw()
          cat1_300answerDclick.undraw()
          time.sleep(0.1)
          newInstructions.undraw()
          
          'draw'
          drawAnimation()
          for boxes in boxesClicked:
              boxes.undraw()
              time.sleep(0.1)
          category1_300test = True
          
       else:
          continue

   #category 2 100pts
   elif isInside(pt, category2_100):
       if not category2_100test:
          boxesClicked.append(cat2PointsText100)
          undrawAnimation()
          
          'instructions'
          newInstructions.setText('Select which answer you think is correct.')
          newInstructions.draw(win)
          
          'question'
          cat2_100question = Text(Point(win.getWidth()/2, 700), '"its finger lickin good"')
          cat2_100question1 = Text(Point(win.getWidth()/2, 650), 'had been the slogan for over 50 years')
          cat2_100question2 = Text(Point(win.getWidth()/2, 600), 'for what restaurant chain?')
          cat2_100question.setSize(36)
          cat2_100question.setStyle('bold')
          cat2_100question.draw(win)
          cat2_100question1.setSize(34)
          cat2_100question1.draw(win)
          cat2_100question2.setSize(34)
          cat2_100question2.draw(win)
          
          'answers'
          cat2_100answerA = Text(Point(win.getWidth()/2, 500), 'A) KFC')
          cat2_100answerAclick = Rectangle(Point(335, 530), Point(665, 470))
          
          cat2_100answerB = Text(Point(win.getWidth()/2, 400), 'B) Popeyes')
          cat2_100answerBclick = Rectangle(Point(335, 430), Point(665, 370))
          
          cat2_100answerC = Text(Point(win.getWidth()/2, 300), 'C) Raising Canes')
          cat2_100answerCclick = Rectangle(Point(335, 330), Point(665, 270))
          
          cat2_100answerD = Text(Point(win.getWidth()/2, 200), 'D) Chick-fil-A')
          cat2_100answerDclick = Rectangle(Point(335, 230), Point(665, 170))

          cat2_100answerAclick.setFill('darkBlue')
          cat2_100answerAclick.draw(win)
          cat2_100answerBclick.setFill('darkBlue')
          cat2_100answerBclick.draw(win)
          cat2_100answerCclick.setFill('darkBlue')
          cat2_100answerCclick.draw(win)
          cat2_100answerDclick.setFill('darkBlue')
          cat2_100answerDclick.draw(win)
          cat2_100answerA.setSize(25)
          cat2_100answerA.draw(win)
          cat2_100answerB.setSize(25)
          cat2_100answerB.draw(win)
          cat2_100answerC.setSize(25)
          cat2_100answerC.draw(win)
          cat2_100answerD.setSize(25)
          cat2_100answerD.draw(win)
          
          for mouseClick in range(100):
             pt = win.getMouse()
             
             if isInside(pt, cat2_100answerAclick):
                 cat2_100answerA.setTextColor('green')
                 cat2_100answerB.setTextColor('red')
                 cat2_100answerC.setTextColor('red')
                 cat2_100answerD.setTextColor('red')
                 newInstructions.setText('Congratulations, that is correct! Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 totalScore = totalScore + 100
                 scoreText.setText('Score: {}'.format(totalScore))
                 win.getMouse()
                 break
             elif isInside(pt, cat2_100answerBclick):
                 cat2_100answerA.setTextColor('green')
                 cat2_100answerB.setTextColor('red')
                 cat2_100answerC.setTextColor('red')
                 cat2_100answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat2_100answerCclick):
                 cat2_100answerA.setTextColor('green')
                 cat2_100answerB.setTextColor('red')
                 cat2_100answerC.setTextColor('red')
                 cat2_100answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat2_100answerDclick):
                 cat2_100answerA.setTextColor('green')
                 cat2_100answerB.setTextColor('red')
                 cat2_100answerC.setTextColor('red')
                 cat2_100answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             else:
                 continue
               
          'undraw'
          cat2_100question.undraw()
          time.sleep(0.1)
          cat2_100question1.undraw()
          time.sleep(0.1)
          cat2_100question2.undraw()
          time.sleep(0.1)
          cat2_100answerA.undraw()
          cat2_100answerAclick.undraw()
          time.sleep(0.1)
          cat2_100answerB.undraw()
          cat2_100answerBclick.undraw()
          time.sleep(0.1)
          cat2_100answerC.undraw()
          cat2_100answerCclick.undraw()
          time.sleep(0.1)
          cat2_100answerD.undraw()
          cat2_100answerDclick.undraw()
          time.sleep(0.1)
          newInstructions.undraw()
          
          'draw'
          drawAnimation()
          for boxes in boxesClicked:
              boxes.undraw()
              time.sleep(0.1)
          category2_100test = True
          
       else:
          continue

   #Category 2 200pts
   elif isInside(pt, category2_200):
       if not category2_200test:
          boxesClicked.append(cat2PointsText200)
          undrawAnimation()
          
          'instructions'
          newInstructions.setText('Select which answer you think is correct.')
          newInstructions.draw(win)
          
          'question'
          cat2_200question = Text(Point(win.getWidth()/2, 700), 'What is the Scoville Scale')
          cat2_200question1 = Text(Point(win.getWidth()/2, 650), 'used to measure in food?')
          cat2_200question.setSize(36)
          cat2_200question.setStyle('bold')
          cat2_200question.draw(win)
          cat2_200question1.setSize(34)
          cat2_200question1.setStyle('bold')
          cat2_200question1.draw(win)
          
          'answers'
          cat2_200answerA = Text(Point(win.getWidth()/2, 500), 'A) Age')
          cat2_200answerAclick = Rectangle(Point(310, 530), Point(690, 470))
          
          cat2_200answerB = Text(Point(win.getWidth()/2, 400), 'B) Nutrition')
          cat2_200answerBclick = Rectangle(Point(310, 430), Point(690, 370))
          
          cat2_200answerC = Text(Point(win.getWidth()/2, 300), 'C) Spiciness')
          cat2_200answerCclick = Rectangle(Point(310, 330), Point(690, 270))
          
          cat2_200answerD = Text(Point(win.getWidth()/2, 200), 'D) Cooking Temperature')
          cat2_200answerDclick = Rectangle(Point(310, 230), Point(690, 170))

          cat2_200answerAclick.setFill('darkBlue')
          cat2_200answerAclick.draw(win)
          cat2_200answerBclick.setFill('darkBlue')
          cat2_200answerBclick.draw(win)
          cat2_200answerCclick.setFill('darkBlue')
          cat2_200answerCclick.draw(win)
          cat2_200answerDclick.setFill('darkBlue')
          cat2_200answerDclick.draw(win)
          cat2_200answerA.setSize(25)
          cat2_200answerA.draw(win)
          cat2_200answerB.setSize(25)
          cat2_200answerB.draw(win)
          cat2_200answerC.setSize(25)
          cat2_200answerC.draw(win)
          cat2_200answerD.setSize(25)
          cat2_200answerD.draw(win)
          
          for mouseClick in range(100):
             pt = win.getMouse()
             
             if isInside(pt, cat2_200answerAclick):
                 cat2_200answerA.setTextColor('red')
                 cat2_200answerB.setTextColor('red')
                 cat2_200answerC.setTextColor('green')
                 cat2_200answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat2_200answerBclick):
                 cat2_200answerA.setTextColor('red')
                 cat2_200answerB.setTextColor('red')
                 cat2_200answerC.setTextColor('green')
                 cat2_200answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat2_200answerCclick):
                 cat2_200answerA.setTextColor('red')
                 cat2_200answerB.setTextColor('red')
                 cat2_200answerC.setTextColor('green')
                 cat2_200answerD.setTextColor('red')
                 newInstructions.setText('Congratulations, that is correct! Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 totalScore = totalScore + 200
                 scoreText.setText('Score: {}'.format(totalScore))
                 win.getMouse()
                 break
             elif isInside(pt, cat2_200answerDclick):
                 cat2_200answerA.setTextColor('red')
                 cat2_200answerB.setTextColor('red')
                 cat2_200answerC.setTextColor('green')
                 cat2_200answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             else:
                 continue
               
          'undraw'
          cat2_200question.undraw()
          time.sleep(0.1)
          cat2_200question1.undraw()
          time.sleep(0.1)
          cat2_200answerA.undraw()
          cat2_200answerAclick.undraw()
          time.sleep(0.1)
          cat2_200answerB.undraw()
          cat2_200answerBclick.undraw()
          time.sleep(0.1)
          cat2_200answerC.undraw()
          cat2_200answerCclick.undraw()
          time.sleep(0.1)
          cat2_200answerD.undraw()
          cat2_200answerDclick.undraw()
          time.sleep(0.1)
          newInstructions.undraw()
          
          'draw'
          drawAnimation()
          for boxes in boxesClicked:
              boxes.undraw()
              time.sleep(0.1)
          category2_200test = True
          
       else:
          continue

   #Category 2 300pts
   elif isInside(pt, category2_300):
       if not category2_300test:
          boxesClicked.append(cat2PointsText300)
          undrawAnimation()
          
          'instructions'
          newInstructions.setText('Select which answer you think is correct.')
          newInstructions.draw(win)
          
          'question'
          cat2_300question = Text(Point(win.getWidth()/2, 700), 'What is the oldest drink')
          cat2_300question1 = Text(Point(win.getWidth()/2, 650), 'in the United States?')
          cat2_300question.setSize(36)
          cat2_300question.setStyle('bold')
          cat2_300question.draw(win)
          cat2_300question1.setSize(34)
          cat2_300question1.setStyle('bold')
          cat2_300question1.draw(win)
          
          'answers'
          cat2_300answerA = Text(Point(win.getWidth()/2, 500), 'A) Coca-cola')
          cat2_300answerAclick = Rectangle(Point(335, 530), Point(675, 470))
          
          cat2_300answerB = Text(Point(win.getWidth()/2, 400), 'B) 7-Up')
          cat2_300answerBclick = Rectangle(Point(335, 430), Point(675, 370))
          
          cat2_300answerC = Text(Point(win.getWidth()/2, 300), 'C) A&W Root Beer')
          cat2_300answerCclick = Rectangle(Point(335, 330), Point(675, 270))
          
          cat2_300answerD = Text(Point(win.getWidth()/2, 200), 'D) Dr. Pepper')
          cat2_300answerDclick = Rectangle(Point(335, 230), Point(675, 170))

          cat2_300answerAclick.setFill('darkBlue')
          cat2_300answerAclick.draw(win)
          cat2_300answerBclick.setFill('darkBlue')
          cat2_300answerBclick.draw(win)
          cat2_300answerCclick.setFill('darkBlue')
          cat2_300answerCclick.draw(win)
          cat2_300answerDclick.setFill('darkBlue')
          cat2_300answerDclick.draw(win)
          cat2_300answerA.setSize(25)
          cat2_300answerA.draw(win)
          cat2_300answerB.setSize(25)
          cat2_300answerB.draw(win)
          cat2_300answerC.setSize(25)
          cat2_300answerC.draw(win)
          cat2_300answerD.setSize(25)
          cat2_300answerD.draw(win)
          
          for mouseClick in range(100):
             pt = win.getMouse()
             
             if isInside(pt, cat2_300answerAclick):
                 cat2_300answerA.setTextColor('red')
                 cat2_300answerB.setTextColor('red')
                 cat2_300answerC.setTextColor('red')
                 cat2_300answerD.setTextColor('green')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat2_300answerBclick):
                 cat2_300answerA.setTextColor('red')
                 cat2_300answerB.setTextColor('red')
                 cat2_300answerC.setTextColor('red')
                 cat2_300answerD.setTextColor('green')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat2_300answerCclick):
                 cat2_300answerA.setTextColor('red')
                 cat2_300answerB.setTextColor('red')
                 cat2_300answerC.setTextColor('red')
                 cat2_300answerD.setTextColor('green')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat2_300answerDclick):
                 cat2_300answerA.setTextColor('red')
                 cat2_300answerB.setTextColor('red')
                 cat2_300answerC.setTextColor('red')
                 cat2_300answerD.setTextColor('green')
                 newInstructions.setText('Congratulations, that is correct! Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 totalScore = totalScore + 300
                 scoreText.setText('Score: {}'.format(totalScore))
                 win.getMouse()
                 break
             else:
                 continue
               
          'undraw'
          cat2_300question.undraw()
          time.sleep(0.1)
          cat2_300question1.undraw()
          time.sleep(0.1)
          cat2_300answerA.undraw()
          cat2_300answerAclick.undraw()
          time.sleep(0.1)
          cat2_300answerB.undraw()
          cat2_300answerBclick.undraw()
          time.sleep(0.1)
          cat2_300answerC.undraw()
          cat2_300answerCclick.undraw()
          time.sleep(0.1)
          cat2_300answerD.undraw()
          cat2_300answerDclick.undraw()
          time.sleep(0.1)
          newInstructions.undraw()
          
          'draw'
          drawAnimation()
          for boxes in boxesClicked:
              boxes.undraw()
              time.sleep(0.1)
          category2_300test = True
          
       else:
          continue

   #category 3 100pts
   elif isInside(pt, category3_100):
       if not category3_100test:
          boxesClicked.append(cat3PointsText100)
          undrawAnimation()
          
          'insrtructions'
          newInstructions.setText('Select which answer you think is correct.')
          newInstructions.draw(win)
          
          'question'
          cat3_100question = Text(Point(win.getWidth()/2, 700), 'What is the largest star')
          cat3_100question1 = Text(Point(win.getWidth()/2, 650), 'in the solar system?')
          cat3_100question.setSize(36)
          cat3_100question.setStyle('bold')
          cat3_100question.draw(win)
          cat3_100question1.setSize(36)
          cat3_100question1.setStyle('bold')
          cat3_100question1.draw(win)
          
          'answers'
          cat3_100answerA = Text(Point(win.getWidth()/2, 500), 'A) Polaris')
          cat3_100answerAclick = Rectangle(Point(335, 530), Point(665, 470))
          
          cat3_100answerB = Text(Point(win.getWidth()/2, 400), 'B) The Sun')
          cat3_100answerBclick = Rectangle(Point(335, 430), Point(665, 370))
          
          cat3_100answerC = Text(Point(win.getWidth()/2, 300), 'C) Sirius')
          cat3_100answerCclick = Rectangle(Point(335, 330), Point(665, 270))
          
          cat3_100answerD = Text(Point(win.getWidth()/2, 200), 'D) Vega')
          cat3_100answerDclick = Rectangle(Point(335, 230), Point(665, 170))

          cat3_100answerAclick.setFill('darkBlue')
          cat3_100answerAclick.draw(win)
          cat3_100answerBclick.setFill('darkBlue')
          cat3_100answerBclick.draw(win)
          cat3_100answerCclick.setFill('darkBlue')
          cat3_100answerCclick.draw(win)
          cat3_100answerDclick.setFill('darkBlue')
          cat3_100answerDclick.draw(win)
          cat3_100answerA.setSize(25)
          cat3_100answerA.draw(win)
          cat3_100answerB.setSize(25)
          cat3_100answerB.draw(win)
          cat3_100answerC.setSize(25)
          cat3_100answerC.draw(win)
          cat3_100answerD.setSize(25)
          cat3_100answerD.draw(win)
          
          for mouseClick in range(100):
             pt = win.getMouse()
             
             if isInside(pt, cat3_100answerAclick):
                 cat3_100answerA.setTextColor('red')
                 cat3_100answerB.setTextColor('green')
                 cat3_100answerC.setTextColor('red')
                 cat3_100answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat3_100answerBclick):
                 cat3_100answerA.setTextColor('red')
                 cat3_100answerB.setTextColor('green')
                 cat3_100answerC.setTextColor('red')
                 cat3_100answerD.setTextColor('red')
                 totalScore = totalScore + 100
                 scoreText.setText('Score: {}'.format(totalScore))
                 newInstructions.setText('Congratulations, that is correct! Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat3_100answerCclick):
                 cat3_100answerA.setTextColor('red')
                 cat3_100answerB.setTextColor('green')
                 cat3_100answerC.setTextColor('red')
                 cat3_100answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat3_100answerDclick):
                 cat3_100answerA.setTextColor('red')
                 cat3_100answerB.setTextColor('green')
                 cat3_100answerC.setTextColor('red')
                 cat3_100answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             else:
                 continue
               
          'undraw'
          cat3_100question.undraw()
          time.sleep(0.1)
          cat3_100question1.undraw()
          time.sleep(0.1)
          cat3_100answerA.undraw()
          cat3_100answerAclick.undraw()
          time.sleep(0.1)
          cat3_100answerB.undraw()
          cat3_100answerBclick.undraw()
          time.sleep(0.1)
          cat3_100answerC.undraw()
          cat3_100answerCclick.undraw()
          time.sleep(0.1)
          cat3_100answerD.undraw()
          cat3_100answerDclick.undraw()
          time.sleep(0.1)
          newInstructions.undraw()
          
          'draw'
          drawAnimation()
          for boxes in boxesClicked:
              boxes.undraw()
              time.sleep(0.1)
          category3_100test = True
          
       else:
          continue

   #category 3 200pts
   elif isInside(pt, category3_200):
       if not category3_200test:
          boxesClicked.append(cat3PointsText200)
          undrawAnimation()
          
          'insrtructions'
          newInstructions.setText('Select which answer you think is correct.')
          newInstructions.draw(win)
          
          'question'
          cat3_200question = Text(Point(win.getWidth()/2, 700), 'What is the largest organ')
          cat3_200question1 = Text(Point(win.getWidth()/2, 650), 'in the human body?')
          cat3_200question.setSize(36)
          cat3_200question.setStyle('bold')
          cat3_200question.draw(win)
          cat3_200question1.setSize(36)
          cat3_200question1.setStyle('bold')
          cat3_200question1.draw(win)
          
          'answers'
          cat3_200answerA = Text(Point(win.getWidth()/2, 500), 'A) Bones')
          cat3_200answerAclick = Rectangle(Point(335, 530), Point(665, 470))
          
          cat3_200answerB = Text(Point(win.getWidth()/2, 400), 'B) Brain')
          cat3_200answerBclick = Rectangle(Point(335, 430), Point(665, 370))
          
          cat3_200answerC = Text(Point(win.getWidth()/2, 300), 'C) Liver')
          cat3_200answerCclick = Rectangle(Point(335, 330), Point(665, 270))
          
          cat3_200answerD = Text(Point(win.getWidth()/2, 200), 'D) Skin')
          cat3_200answerDclick = Rectangle(Point(335, 230), Point(665, 170))

          cat3_200answerAclick.setFill('darkBlue')
          cat3_200answerAclick.draw(win)
          cat3_200answerBclick.setFill('darkBlue')
          cat3_200answerBclick.draw(win)
          cat3_200answerCclick.setFill('darkBlue')
          cat3_200answerCclick.draw(win)
          cat3_200answerDclick.setFill('darkBlue')
          cat3_200answerDclick.draw(win)
          cat3_200answerA.setSize(25)
          cat3_200answerA.draw(win)
          cat3_200answerB.setSize(25)
          cat3_200answerB.draw(win)
          cat3_200answerC.setSize(25)
          cat3_200answerC.draw(win)
          cat3_200answerD.setSize(25)
          cat3_200answerD.draw(win)
          
          for mouseClick in range(100):
             pt = win.getMouse()
             
             if isInside(pt, cat3_200answerAclick):
                 cat3_200answerA.setTextColor('red')
                 cat3_200answerB.setTextColor('red')
                 cat3_200answerC.setTextColor('red')
                 cat3_200answerD.setTextColor('green')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat3_200answerBclick):
                 cat3_200answerA.setTextColor('red')
                 cat3_200answerB.setTextColor('red')
                 cat3_200answerC.setTextColor('red')
                 cat3_200answerD.setTextColor('green')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat3_200answerCclick):
                 cat3_200answerA.setTextColor('red')
                 cat3_200answerB.setTextColor('red')
                 cat3_200answerC.setTextColor('red')
                 cat3_200answerD.setTextColor('green')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat3_200answerDclick):
                 cat3_200answerA.setTextColor('red')
                 cat3_200answerB.setTextColor('red')
                 cat3_200answerC.setTextColor('red')
                 cat3_200answerD.setTextColor('green')
                 totalScore = totalScore + 200
                 scoreText.setText('Score: {}'.format(totalScore))
                 newInstructions.setText('Congratulations, that is correct! Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             else:
                 continue
               
          'undraw'
          cat3_200question.undraw()
          time.sleep(0.1)
          cat3_200question1.undraw()
          time.sleep(0.1)
          cat3_200answerA.undraw()
          cat3_200answerAclick.undraw()
          time.sleep(0.1)
          cat3_200answerB.undraw()
          cat3_200answerBclick.undraw()
          time.sleep(0.1)
          cat3_200answerC.undraw()
          cat3_200answerCclick.undraw()
          time.sleep(0.1)
          cat3_200answerD.undraw()
          cat3_200answerDclick.undraw()
          time.sleep(0.1)
          newInstructions.undraw()
          
          'draw'
          drawAnimation()
          for boxes in boxesClicked:
             boxes.undraw()
             time.sleep(0.1)
          category3_200test = True
          
       else:
          continue

   #category 3 300pts
   elif isInside(pt, category3_300):
       if not category3_300test:
          boxesClicked.append(cat3PointsText300)
          undrawAnimation()
          
          'insrtructions'
          newInstructions.setText('Select which answer you think is correct.')
          newInstructions.draw(win)
          
          'question'
          cat3_300question = Text(Point(win.getWidth()/2, 700), 'What is it called when a liquid')
          cat3_300question1 = Text(Point(win.getWidth()/2, 650), 'is mixed with another liquid?')
          cat3_300question.setSize(36)
          cat3_300question.setStyle('bold')
          cat3_300question.draw(win)
          cat3_300question1.setSize(36)
          cat3_300question1.setStyle('bold')
          cat3_300question1.draw(win)
          
          'answers'
          cat3_300answerA = Text(Point(win.getWidth()/2, 500), 'A) Emulsion')
          cat3_300answerAclick = Rectangle(Point(335, 530), Point(665, 470))
          
          cat3_300answerB = Text(Point(win.getWidth()/2, 400), 'B) Solvent')
          cat3_300answerBclick = Rectangle(Point(335, 430), Point(665, 370))
          
          cat3_300answerC = Text(Point(win.getWidth()/2, 300), 'C) Solute')
          cat3_300answerCclick = Rectangle(Point(335, 330), Point(665, 270))
          
          cat3_300answerD = Text(Point(win.getWidth()/2, 200), 'D) Distillation')
          cat3_300answerDclick = Rectangle(Point(335, 230), Point(665, 170))

          cat3_300answerAclick.setFill('darkBlue')
          cat3_300answerAclick.draw(win)
          cat3_300answerBclick.setFill('darkBlue')
          cat3_300answerBclick.draw(win)
          cat3_300answerCclick.setFill('darkBlue')
          cat3_300answerCclick.draw(win)
          cat3_300answerDclick.setFill('darkBlue')
          cat3_300answerDclick.draw(win)
          cat3_300answerA.setSize(25)
          cat3_300answerA.draw(win)
          cat3_300answerB.setSize(25)
          cat3_300answerB.draw(win)
          cat3_300answerC.setSize(25)
          cat3_300answerC.draw(win)
          cat3_300answerD.setSize(25)
          cat3_300answerD.draw(win)
          
          for mouseClick in range(100):
             pt = win.getMouse()
             
             if isInside(pt, cat3_300answerAclick):
                 cat3_300answerA.setTextColor('green')
                 cat3_300answerB.setTextColor('red')
                 cat3_300answerC.setTextColor('red')
                 cat3_300answerD.setTextColor('red')
                 totalScore = totalScore + 300
                 scoreText.setText('Score: {}'.format(totalScore))
                 newInstructions.setText('Congratulations, that is correct! Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat3_300answerBclick):
                 cat3_300answerA.setTextColor('green')
                 cat3_300answerB.setTextColor('red')
                 cat3_300answerC.setTextColor('red')
                 cat3_300answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat3_300answerCclick):
                 cat3_300answerA.setTextColor('green')
                 cat3_300answerB.setTextColor('red')
                 cat3_300answerC.setTextColor('red')
                 cat3_300answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat3_300answerDclick):
                 cat3_300answerA.setTextColor('green')
                 cat3_300answerB.setTextColor('red')
                 cat3_300answerC.setTextColor('red')
                 cat3_300answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             else:
                 continue
               
          'undraw'
          cat3_300question.undraw()
          time.sleep(0.1)
          cat3_300question1.undraw()
          time.sleep(0.1)
          cat3_300answerA.undraw()
          cat3_300answerAclick.undraw()
          time.sleep(0.1)
          cat3_300answerB.undraw()
          cat3_300answerBclick.undraw()
          time.sleep(0.1)
          cat3_300answerC.undraw()
          cat3_300answerCclick.undraw()
          time.sleep(0.1)
          cat3_300answerD.undraw()
          cat3_300answerDclick.undraw()
          time.sleep(0.1)
          newInstructions.undraw()
          
          'draw'
          drawAnimation()
          for boxes in boxesClicked:
             boxes.undraw()
             time.sleep(0.1)
          category3_300test = True
          
       else:
          continue

   #category 4 100pts
   elif isInside(pt, category4_100):
       if not category4_100test:
          boxesClicked.append(cat4PointsText100)
          undrawAnimation()
          
          'insrtructions'
          newInstructions.setText('Select which answer you think is correct.')
          newInstructions.draw(win)
          
          'question'
          cat4_100question = Text(Point(win.getWidth()/2, 700), 'Where is the world’s')
          cat4_100question1 = Text(Point(win.getWidth()/2, 650), 'tallest building located?')
          cat4_100question.setSize(36)
          cat4_100question.setStyle('bold')
          cat4_100question.draw(win)
          cat4_100question1.setSize(36)
          cat4_100question1.setStyle('bold')
          cat4_100question1.draw(win)
          
          'answers'
          cat4_100answerA = Text(Point(win.getWidth()/2, 500), 'A) Paris')
          cat4_100answerAclick = Rectangle(Point(335, 530), Point(665, 470))
          
          cat4_100answerB = Text(Point(win.getWidth()/2, 400), 'B) Dubai')
          cat4_100answerBclick = Rectangle(Point(335, 430), Point(665, 370))
          
          cat4_100answerC = Text(Point(win.getWidth()/2, 300), 'C) New York')
          cat4_100answerCclick = Rectangle(Point(335, 330), Point(665, 270))
          
          cat4_100answerD = Text(Point(win.getWidth()/2, 200), 'D) China')
          cat4_100answerDclick = Rectangle(Point(335, 230), Point(665, 170))

          cat4_100answerAclick.setFill('darkBlue')
          cat4_100answerAclick.draw(win)
          cat4_100answerBclick.setFill('darkBlue')
          cat4_100answerBclick.draw(win)
          cat4_100answerCclick.setFill('darkBlue')
          cat4_100answerCclick.draw(win)
          cat4_100answerDclick.setFill('darkBlue')
          cat4_100answerDclick.draw(win)
          cat4_100answerA.setSize(25)
          cat4_100answerA.draw(win)
          cat4_100answerB.setSize(25)
          cat4_100answerB.draw(win)
          cat4_100answerC.setSize(25)
          cat4_100answerC.draw(win)
          cat4_100answerD.setSize(25)
          cat4_100answerD.draw(win)
          
          for mouseClick in range(100):
             pt = win.getMouse()
             
             if isInside(pt, cat4_100answerAclick):
                 cat4_100answerA.setTextColor('red')
                 cat4_100answerB.setTextColor('green')
                 cat4_100answerC.setTextColor('red')
                 cat4_100answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat4_100answerBclick):
                 cat4_100answerA.setTextColor('red')
                 cat4_100answerB.setTextColor('green')
                 cat4_100answerC.setTextColor('red')
                 cat4_100answerD.setTextColor('red')
                 totalScore = totalScore + 100
                 scoreText.setText('Score: {}'.format(totalScore))
                 newInstructions.setText('Congratulations, that is correct! Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat4_100answerCclick):
                 cat4_100answerA.setTextColor('red')
                 cat4_100answerB.setTextColor('green')
                 cat4_100answerC.setTextColor('red')
                 cat4_100answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat4_100answerDclick):
                 cat4_100answerA.setTextColor('red')
                 cat4_100answerB.setTextColor('green')
                 cat4_100answerC.setTextColor('red')
                 cat4_100answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             else:
                 continue
               
          'undraw'
          cat4_100question.undraw()
          time.sleep(0.1)
          cat4_100question1.undraw()
          time.sleep(0.1)
          cat4_100answerA.undraw()
          cat4_100answerAclick.undraw()
          time.sleep(0.1)
          cat4_100answerB.undraw()
          cat4_100answerBclick.undraw()
          time.sleep(0.1)
          cat4_100answerC.undraw()
          cat4_100answerCclick.undraw()
          time.sleep(0.1)
          cat4_100answerD.undraw()
          cat4_100answerDclick.undraw()
          time.sleep(0.1)
          newInstructions.undraw()
          
          'draw'
          drawAnimation()
          for boxes in boxesClicked:
              boxes.undraw()
              time.sleep(0.1)
          category4_100test = True
          
       else:
          continue

   #category 4 200pts
   elif isInside(pt, category4_200):
       if not category4_200test:
          boxesClicked.append(cat4PointsText200)
          undrawAnimation()
          
          'insrtructions'
          newInstructions.setText('Select which answer you think is correct.')
          newInstructions.draw(win)
          
          'question'
          cat4_200question = Text(Point(win.getWidth()/2, 700), 'What year was the US')
          cat4_200question1 = Text(Point(win.getWidth()/2, 650), 'Declaration of Independence signed?')
          cat4_200question.setSize(36)
          cat4_200question.setStyle('bold')
          cat4_200question.draw(win)
          cat4_200question1.setSize(36)
          cat4_200question1.setStyle('bold')
          cat4_200question1.draw(win)
          
          'answers'
          cat4_200answerA = Text(Point(win.getWidth()/2, 500), 'A) 1752')
          cat4_200answerAclick = Rectangle(Point(335, 530), Point(665, 470))
          
          cat4_200answerB = Text(Point(win.getWidth()/2, 400), 'B) 1812')
          cat4_200answerBclick = Rectangle(Point(335, 430), Point(665, 370))
          
          cat4_200answerC = Text(Point(win.getWidth()/2, 300), 'C) 1776')
          cat4_200answerCclick = Rectangle(Point(335, 330), Point(665, 270))
          
          cat4_200answerD = Text(Point(win.getWidth()/2, 200), 'D) 1793')
          cat4_200answerDclick = Rectangle(Point(335, 230), Point(665, 170))

          cat4_200answerAclick.setFill('darkBlue')
          cat4_200answerAclick.draw(win)
          cat4_200answerBclick.setFill('darkBlue')
          cat4_200answerBclick.draw(win)
          cat4_200answerCclick.setFill('darkBlue')
          cat4_200answerCclick.draw(win)
          cat4_200answerDclick.setFill('darkBlue')
          cat4_200answerDclick.draw(win)
          cat4_200answerA.setSize(25)
          cat4_200answerA.draw(win)
          cat4_200answerB.setSize(25)
          cat4_200answerB.draw(win)
          cat4_200answerC.setSize(25)
          cat4_200answerC.draw(win)
          cat4_200answerD.setSize(25)
          cat4_200answerD.draw(win)
          
          for mouseClick in range(100):
             pt = win.getMouse()
             
             if isInside(pt, cat4_200answerAclick):
                 cat4_200answerA.setTextColor('red')
                 cat4_200answerB.setTextColor('red')
                 cat4_200answerC.setTextColor('green')
                 cat4_200answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat4_200answerBclick):
                 cat4_200answerA.setTextColor('red')
                 cat4_200answerB.setTextColor('red')
                 cat4_200answerC.setTextColor('green')
                 cat4_200answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat4_200answerCclick):
                 cat4_200answerA.setTextColor('red')
                 cat4_200answerB.setTextColor('red')
                 cat4_200answerC.setTextColor('green')
                 cat4_200answerD.setTextColor('red')
                 totalScore = totalScore + 200
                 scoreText.setText('Score: {}'.format(totalScore))
                 newInstructions.setText('Congratulations, that is correct! Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat4_200answerDclick):
                 cat4_200answerA.setTextColor('red')
                 cat4_200answerB.setTextColor('red')
                 cat4_200answerC.setTextColor('green')
                 cat4_200answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             else:
                 continue
               
          'undraw'
          cat4_200question.undraw()
          time.sleep(0.1)
          cat4_200question1.undraw()
          time.sleep(0.1)
          cat4_200answerA.undraw()
          cat4_200answerAclick.undraw()
          time.sleep(0.1)
          cat4_200answerB.undraw()
          cat4_200answerBclick.undraw()
          time.sleep(0.1)
          cat4_200answerC.undraw()
          cat4_200answerCclick.undraw()
          time.sleep(0.1)
          cat4_200answerD.undraw()
          cat4_200answerDclick.undraw()
          time.sleep(0.1)
          newInstructions.undraw()
          
          'draw'
          drawAnimation()
          for boxes in boxesClicked:
              boxes.undraw()
              time.sleep(0.1)
          category4_200test = True
          
       else:
          continue

   #category 4 300pts
   elif isInside(pt, category4_300):
       if not category4_300test:
          boxesClicked.append(cat4PointsText300)
          undrawAnimation()
          
          'insrtructions'
          newInstructions.setText('Select which answer you think is correct.')
          newInstructions.draw(win)
          
          'question'
          cat4_300question = Text(Point(win.getWidth()/2, 700), 'What was the number')
          cat4_300question1 = Text(Point(win.getWidth()/2, 650), 'one song of 2010?')
          cat4_300question.setSize(36)
          cat4_300question.setStyle('bold')
          cat4_300question.draw(win)
          cat4_300question1.setSize(36)
          cat4_300question1.setStyle('bold')
          cat4_300question1.draw(win)
          
          'answers'
          cat4_300answerA = Text(Point(win.getWidth()/2, 500), 'A) “Tik Tok” by Kesha')
          cat4_300answerAclick = Rectangle(Point(250, 530), Point(750, 470))
          
          cat4_300answerB = Text(Point(win.getWidth()/2, 400), 'B) “Hey, Soul Sister” by Train')
          cat4_300answerBclick = Rectangle(Point(250, 430), Point(750, 370))
          
          cat4_300answerC = Text(Point(win.getWidth()/2, 300), 'C) “California Gurls” by Katy Perry')
          cat4_300answerCclick = Rectangle(Point(250, 330), Point(750, 270))
          
          cat4_300answerD = Text(Point(win.getWidth()/2, 200), 'D) “Rolling in the Deep” by Adele')
          cat4_300answerDclick = Rectangle(Point(250, 230), Point(750, 170))

          cat4_300answerAclick.setFill('darkBlue')
          cat4_300answerAclick.draw(win)
          cat4_300answerBclick.setFill('darkBlue')
          cat4_300answerBclick.draw(win)
          cat4_300answerCclick.setFill('darkBlue')
          cat4_300answerCclick.draw(win)
          cat4_300answerDclick.setFill('darkBlue')
          cat4_300answerDclick.draw(win)
          cat4_300answerA.setSize(25)
          cat4_300answerA.draw(win)
          cat4_300answerB.setSize(25)
          cat4_300answerB.draw(win)
          cat4_300answerC.setSize(25)
          cat4_300answerC.draw(win)
          cat4_300answerD.setSize(25)
          cat4_300answerD.draw(win)
          
          for mouseClick in range(100):
             pt = win.getMouse()
             if isInside(pt, cat4_300answerAclick):
                 cat4_300answerA.setTextColor('green')
                 cat4_300answerB.setTextColor('red')
                 cat4_300answerC.setTextColor('red')
                 cat4_300answerD.setTextColor('red')
                 totalScore = totalScore + 300
                 scoreText.setText('Score: {}'.format(totalScore))
                 newInstructions.setText('Congratulations, that is correct! Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat4_300answerBclick):
                 cat4_300answerA.setTextColor('green')
                 cat4_300answerB.setTextColor('red')
                 cat4_300answerC.setTextColor('red')
                 cat4_300answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat4_200answerCclick):
                 cat4_300answerA.setTextColor('green')
                 cat4_300answerB.setTextColor('red')
                 cat4_300answerC.setTextColor('red')
                 cat4_300answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             elif isInside(pt, cat4_300answerDclick):
                 cat4_300answerA.setTextColor('green')
                 cat4_300answerB.setTextColor('red')
                 cat4_300answerC.setTextColor('red')
                 cat4_300answerD.setTextColor('red')
                 newInstructions.setText('Unfortunately that is incorrect. Click anywhere to continue.')
                 newInstructions.setStyle('italic')
                 newInstructions.setTextColor('yellow')
                 win.getMouse()
                 break
             else:
                 continue
               
          'undraw'
          cat4_300question.undraw()
          time.sleep(0.1)
          cat4_300question1.undraw()
          time.sleep(0.1)
          cat4_300answerA.undraw()
          cat4_300answerAclick.undraw()
          time.sleep(0.1)
          cat4_300answerB.undraw()
          cat4_300answerBclick.undraw()
          time.sleep(0.1)
          cat4_300answerC.undraw()
          cat4_300answerCclick.undraw()
          time.sleep(0.1)
          cat4_300answerD.undraw()
          cat4_300answerDclick.undraw()
          time.sleep(0.1)
          newInstructions.undraw()
          
          'draw'
          drawAnimation()
          for boxes in boxesClicked:
              boxes.undraw()
              time.sleep(0.1)
          category4_300test = True
          
       else:
          continue

   else:
      continue

#Code I couldn't figure out (timer).
#User needs to wait until timer loop is done before they can click.
#Want user to be able to click while the timer is going instead of needing to wait.
'''
remainingTime = 15
for seconds in range(15):
   if isInside(pt, cat1_100answerAclick) or isInside(pt, cat1_100answerBclick) or isInside(pt, cat1_100answerCclick) or isInside(pt, cat1_100answerDclick):
      break
   else:
      clock = Text(Point(130, 75), "Remaining Time: {} seconds".format(remainingTime))
      clock.draw(win)
      time.sleep(1)
      clock.undraw()
      remainingTime = remainingTime - 1
'''
