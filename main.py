import pygame
import sys
import random
import numpy as np

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

cWidth: int = 100
cHeight: int = 100
rows = cols = 6
pieces = rows * cols
pieces_per_group_row = rows // 2
pieces_per_group = pieces // 2

BKG_COLOR = pygame.Color('grey')
LINE_COLOR = pygame.Color('black')
LINE_WIDTH = 1  # line width
scale=0.9

SUN = 1
MOON = 3
BLANK = 2
piece_choices = [SUN, MOON]

size = cWidth * rows, cHeight * rows

board =  [[BLANK] * cols for i in range(rows)]
boardClickable= [[True] * cols for i in range(rows)]

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tango')


img_sun = pygame.image.load("./image/sun.jpg").convert()
img_moon = pygame.image.load("./image/moon.jpg").convert()
img_equal = pygame.image.load("./image/equal.png").convert()
img_cross = pygame.image.load("./image/cross.png").convert()

def showNotification(text, left, top):
    textSurface = connect4Font.render(text, False, (0, 0, 0))
    screen.blit(textSurface, (left, top))


'''
Rules:
1. Either Sun or Moon in each cell
2. No more than 2 characters may be next to each other,either vertically or horizontally
3. each row or column must contain the same number of each character
4. cells separated by an  = sign must be of the same type
5. Cells separated by an x sign must be of the opposite charater
'''


def is3Connected(row):
    row1 = row[:(pieces_per_group_row)]
    row1.sort()
    cnt = 1
    for i in range(len(row1) - 1):
        if row1[i] + 1 == row1[i + 1]:
            cnt += 1

    flag = (cnt >= pieces_per_group_row)
    return flag


def produceASolution():
    solution = [[BLANK] * rows for i in range(rows)]

    for i in range(rows):
        row = [j for j in range(cols)]
        is3ConnectedFlag = True
        while (is3ConnectedFlag):
            random.shuffle(row)
            is3ConnectedFlag = is3Connected(row)

        for k in range(cols):
            j = row[k]
            solution[i][j] = SUN if k < (pieces_per_group_row) else MOON

    return solution


def initASolution():
    solution = [[BLANK] * cols for i in range(rows)]
    isBadSolution = True

    while (isBadSolution):
        solution = produceASolution()
        isBadSolution = ((breachRule1(solution)) \
                         or (breachRule2(solution)) \
                         or (breachRule3(solution))
                         )

    print(solution)
    return solution


def provideClue(solution, board):
    levelChoice=[0,1,2] # the lower, the easier
    charShowLevels = [10, 8, 6]
    signShowLevels = [14, 12, 10]

    # level=random.choice(levelChoice)

    level = 0

    charShowCnt = charShowLevels[level]
    signShowCnt = signShowLevels[level]

    positions= [i for i in range(pieces)]
    random.shuffle(positions)

    for k in range(charShowCnt):
        tmpPos=positions[k]
        i=tmpPos//rows
        j=tmpPos%rows
        board[i][j]=solution[i][j]
        boardClickable[i][j]=False

    signs=(rows-1)*cols+(cols-1)*rows
    positions = [i for i in range(signs)]
    random.shuffle(positions)

    signPos=[]
    for k in range(signShowCnt):
        tmpPos = positions[k]
        if tmpPos<signs//2:
            d='h' # compare horizonally
            i=tmpPos//(cols-1)
            j=tmpPos%(cols-1)
            if (j+1)>=rows:
                print(tmpPos,d, i,j)
            signChar='=' if(solution[i][j]==solution[i][j+1]) else 'x'
        else:
            tmpPos-=signs//2
            d='v' # compare vertically
            i = tmpPos // rows
            j = tmpPos % rows
            if (i+1)>=cols:
                print(tmpPos,d, i,j)
            signChar = '=' if (solution[i][j] == solution[i+1][j]) else 'x'

        signPos.append((d,i,j,signChar))

    return board, boardClickable, signPos


def switchRowCol(solution):
    rows = len(solution)
    cols = len(solution[0])
    s2 = [[BLANK] * rows for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            s2[i][j] = solution[j][i]

    return s2


def breachRule1(solution):
    for i in range(rows):
        for j in range(cols):
            if solution[i][j] == BLANK:
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


def breachRule3(solution):
    expectSum = (SUN + MOON) * rows / 2

    for i in range(rows):
        sum1 = sum(solution[i])
        if sum1 != expectSum:
            return True

    for j in range(cols):
        sum1 = 0
        for i in range(rows):
            sum1 += solution[i][j]
        if sum1 != expectSum:
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


def updateBoardByClue(signPos):
    # update images
    for i in range(rows):
        for j in range(cols):
            if board[i][j]!=BLANK:
                left = j * cWidth + (cWidth * (1 - scale) + LINE_WIDTH) // 2
                top = i * cHeight + (cHeight * (1 - scale) + LINE_WIDTH) // 2
                if board[i][j]==MOON:
                    screen.blit(pygame.transform.scale(img_moon, (cWidth*scale, cHeight*scale)), (left, top))
                else:
                    screen.blit(pygame.transform.scale(img_sun, (cWidth * scale, cHeight * scale)), (left, top))

    # udpate signs
    signScale=0.2
    for d,i,j,signChar in signPos:
        print(d,i,j,signChar)
        if d=='v':
            left = (j+0.5-signScale/2) * cWidth
            top = (i+1-signScale/2)*cHeight
            if signChar=='=':
                screen.blit(pygame.transform.scale(img_equal, (cWidth*signScale, cHeight*signScale)), (left, top))
            elif signChar=='x':
                screen.blit(pygame.transform.scale(img_cross, (cWidth*signScale, cHeight*signScale)), (left, top))
        elif d=='h':
            left = (j + 1-signScale/2) * cWidth
            top = (i + 0.5-signScale/2) * cHeight

        if signChar == '=':
            screen.blit(pygame.transform.scale(img_equal, (cWidth * signScale, cHeight * signScale)), (left, top))
        elif signChar == 'x':
            screen.blit(pygame.transform.scale(img_cross, (cWidth * signScale, cHeight * signScale)), (left, top))

def getMouseClickPos(pos):
    col = int(pos[0] / cWidth)
    row = int(pos[1] / cHeight)
    return col, row

def isSolved(solution, board):
    rows = len(solution)
    cols = len(solution[0])

    for i in range(rows):
        for j in range(cols):
            if (board[i][j]!=solution[i][j]):
                return False

    return True

def buttonClick(pos, button):

    col = getMouseClickPos(pos)[0]
    row = getMouseClickPos(pos)[1]

    if (not(boardClickable[row][col])):
        return

    left=col*cWidth+(cWidth*(1-scale)+LINE_WIDTH)//2
    top=row*cHeight+(cHeight*(1-scale)+LINE_WIDTH)//2


    if button == 1:  # left click
        # put sun
        board[row][col]=SUN
        print(board)
        screen.blit(pygame.transform.scale(img_sun, (cWidth*scale, cHeight*scale)), (left, top))


    # elif button == 2:  # middle click
    #     board[row][col] = BLANK
    #     print(board)
    #     pygame.display.update()
    elif button == 3:  # right click
        board[row][col] = MOON
        print(board)
        screen.blit(pygame.transform.scale(img_moon, (cWidth*scale, cHeight*scale)), (left, top))

    if (isSolved(solution, board)):
        showNotification('Well Done!', 0,0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    connect4Font = pygame.font.SysFont('Comic Sans MS', 30)

    # produce a solution in back end
    solution = initASolution()

    # generate clue
    board, boardClickable, signPos =  provideClue(solution, board)
    print(board)

    drawBoard()

    updateBoardByClue(signPos)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                buttonClick(event.pos, event.button)

        pygame.display.update()
