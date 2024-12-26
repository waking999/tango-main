import pygame
import sys
import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

cWidth: int = 100
cHeight = 100
rows = 6
cols = 6
pieces = rows * rows
pieces_per_group = pieces / 2

BKG_COLOR = pygame.Color('grey')
LINE_COLOR = pygame.Color('black')
LINE_WIDTH = 1  # line width

SUN = 1
MOON = 3
BLANK = 2
piece_choices = [SUN,MOON]

size = cWidth * rows, cHeight * rows
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tango')


def showNotification(text):
    textSurface = connect4Font.render(text, False, (0, 0, 0))
    screen.blit(textSurface, (0, 0))


'''
Rules:
1. Either Sun or Moon in each cell
2. No more than 2 characters may be next to each other,either vertically or horizontally
3. each row or column must contain the same number of each character
4. cells separated by an  = sign must be of the same type
5. Cells separated by an x sign must be of the opposite charater
'''


def produceASolution():
    solution = [[BLANK] * rows for i in range(rows)]
    sunTlCnt=0
    sunRCnt=0
    sunConCnt=0

    moonTlCnt=0
    moonRCnt=0
    moonConCnt=0

    i=0

    while i<rows:
        print(f'i={i}')
        sunRCnt=0
        sunConCnt=0

        moonRCnt = 0
        moonConCnt = 0

        j=0
        isBadRow=True
        while j<cols:
            print(f'j={j}')
            tempPiece=random.choice(piece_choices)
            if tempPiece==SUN:
                sunTlCnt+=1 # restart from the current row
                sunRCnt+=1 # restart from the current row
                sunConCnt+=1 # restart from the current row
                if sunTlCnt>pieces_per_group: # totally pieces_per_group pieces for each group
                    print(f'more than 18 sun.')
                    isBadRow=True
                    break
                elif sunConCnt>=3: # no 3 or more connected
                    print(f'more than 3 sun connected.')
                    isBadRow=True
                    break
                elif sunRCnt>=(cols/2): # no more than half be the same character
                    print(f'more than 3 sun each row.')
                    isBadRow=True
                    break
                else:
                    isBadRow=False
                    solution[i][j]=tempPiece
                    j += 1
                    continue
            else:
                moonTlCnt += 1
                moonRCnt += 1
                moonConCnt += 1
                if moonTlCnt>pieces_per_group: # totally pieces_per_group pieces for each group
                    print(f'more than 18 moon connected.')
                    isBadRow = True
                    i -= 1 # restart from the current row
                    break
                elif moonConCnt >= 3:  # no 3 or more connected
                    isBadRow=True
                    print(f'more than 3 moon connected.')
                    break
                elif moonRCnt >= (cols / 2):  # no more than half be the same character
                    isBadRow = True
                    print(f'more than 3 moon each row.')
                    break
                else:
                    isBadRow = False
                    solution[i][j] = tempPiece
                    j+=1
                    continue

            if isBadRow:
                i-=1

            i+=1 # next row



    return solution

def initASolution():
    solution = [[BLANK] * rows for i in range(rows)]
    isBadSolution=True

    while(isBadSolution):
        solution=produceASolution()
        isBadSolution = ((breachRule1(solution)) \
                         or (breachRule2(solution))
                         )
        print(isBadSolution)

    print(solution)
    return solution


def breachRule1(solution):
    for i in range(rows):
        for j in range(cols):
            if solution[i][j]==BLANK:
                return True

    return False

def breachRule2(solution):
    for i in range(rows):
        for j in range(cols):
            if (((i - 2) >= 0) \
                and ((i - 1) >= 0) \
                and (solution[i][j] != BLANK) \
                and (solution[i - 1][j] != BLANK) \
                and (solution[i - 2][j] != BLANK) \
                and (solution[i][j] == solution[i - 1][j]) \
                and (solution[i][j] == solution[i - 2][j]) \
            ):  # up cell
                return True
            if (((i + 2) < cols) \
                and ((i + 1) < cols) \
                and (solution[i][j] != BLANK) \
                and (solution[i + 1][j] != BLANK) \
                and (solution[i + 2][j] != BLANK) \
                and (solution[i][j] == solution[i + 1][j]) \
                and (solution[i][j] == solution[i + 2][j]) \
            ):  # down cell
                return True
            if (((j - 2) >= 0) \
                and ((j - 1) >= 0) \
                and (solution[i][j] != BLANK) \
                and (solution[i][j - 1] != BLANK) \
                and (solution[i][j - 2] != BLANK) \
                and (solution[i][j] == solution[i][j - 1]) \
                and (solution[i][j] == solution[i][j - 2]) \
            ):  # left cell
                return True
            if (((j + 2) < rows) \
                and ((j + 1) < rows) \
                and (solution[i][j] != BLANK) \
                and (solution[i][j + 1] != BLANK) \
                and (solution[i][j + 2] != BLANK) \
                and (solution[i][j] == solution[i][j + 1]) \
                and (solution[i][j] == solution[i][j + 2]) \
            ):  # right cell
                return True

    return False


"""
draw the board, including background and horizon and vertical lines
"""


def drawBoard():
    # draw board background
    pygame.draw.rect(screen, BKG_COLOR, [0, 0, cWidth * cols, cHeight * rows])

    # draw horizon lines
    lLeft = 0
    lWidth = lLeft + cWidth * cols
    for r in range(rows):
        lTop = r * cHeight
        pygame.draw.line(screen, LINE_COLOR, (lLeft, lTop), (lWidth, lTop), LINE_WIDTH)

    # draw vertical lines
    lTop = 0
    lHeight = lTop + cHeight * rows
    for c in range(cols):
        lLeft = c * cWidth
        pygame.draw.line(screen, LINE_COLOR, (lLeft, lTop), (lLeft, lHeight), LINE_WIDTH)

    # draw vertical lines
    lTop = 0
    lHeight = lTop + cHeight * rows
    for c in range(rows):
        lLeft = c * cWidth
        pygame.draw.line(screen, LINE_COLOR, (lLeft, lTop), (lLeft, lHeight), LINE_WIDTH)


def buttonClick(pos, button):
    # button: 1: left, 2: middle, 3:right

    print(pos)
    print(button)
    if button == 1:  # left click
        # put sun
        pass
    elif button == 2:  # middle click
        # clear
        pass
    elif button == 3:  # right click
        # put moon
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    connect4Font = pygame.font.SysFont('Comic Sans MS', 30)

    solution=initASolution()

    drawBoard()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                buttonClick(event.pos, event.button)

        pygame.display.update()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
