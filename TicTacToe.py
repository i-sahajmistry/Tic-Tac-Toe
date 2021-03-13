import pygame
import time

pygame.init()
screen = pygame.display.set_mode((600, 532))
pygame.display.set_caption('TicTacToe')

line = pygame.image.load('images/Board.png')

player1 = pygame.image.load('images/x.png')
player2 = pygame.image.load('images/o.png')
slant = pygame.image.load('images/red line.png')
slant1 = pygame.image.load('images/slant.png')
horizontal = pygame.image.load('images/red line horizontal.png')
vertical = pygame.image.load('images/red line vertical.png')
winnerO = pygame.image.load('images/Winner o.png')
winnerX = pygame.image.load('images/Winner x.png')

occupiedGrid = {}

currentPlayer = player1


gridC = [
         [(0, 0), ((600 // 3), 0), ((600 // 3) * 2, 0)],
         [(0, (532 // 3)), ((600 // 3), (532 // 3)), ((600 // 3) * 2, (532 // 3))],
         [(0, (532 // 3) * 2), ((600 // 3), (532 // 3) * 2), ((600 // 3) * 2, (532 // 3) * 2)]
]

winningGridCombinations = [
                           [gridC[0][0], gridC[0][1], gridC[0][2]],
                           [gridC[1][0], gridC[1][1], gridC[1][2]],
                           [gridC[2][0], gridC[2][1], gridC[2][2]],
                           [gridC[0][0], gridC[1][0], gridC[2][0]],
                           [gridC[0][1], gridC[1][1], gridC[2][1]],
                           [gridC[0][2], gridC[1][2], gridC[2][2]],
                           [gridC[0][0], gridC[1][1], gridC[2][2]],
                           [gridC[0][2], gridC[1][1], gridC[2][0]]
]


def getGridNumber(coordinates):

    if coordinates[0] < 600 // 3 and coordinates[1] < 532 // 3:
        grid = gridC[0][0]
        return grid
    elif coordinates[0] < (600 // 3) * 2 and coordinates[1] < 532 // 3:
        grid = gridC[0][1]
        return grid
    elif coordinates[0] < (600 // 3) * 3 and coordinates[1] < 532 // 3:
        grid = gridC[0][2]
        return grid

    elif coordinates[0] < 600 // 3 and coordinates[1] < (532 // 3) * 2:
        grid = gridC[1][0]
        return grid
    elif coordinates[0] < (600 // 3) * 2 and coordinates[1] < (532 // 3) * 2:
        grid = gridC[1][1]
        return grid
    elif coordinates[0] < (600 // 3) * 3 and coordinates[1] < (532 // 3) * 2:
        grid = gridC[1][2]
        return grid

    elif coordinates[0] < 600 // 3 and coordinates[1] < (532 // 3) * 3:
        grid = gridC[2][0]
        return grid
    elif coordinates[0] < (600 // 3) * 2 and coordinates[1] < (532 // 3) * 3:
        grid = gridC[2][1]
        return grid
    elif coordinates[0] < (600 // 3) * 3 and coordinates[1] < (532 // 3) * 3:
        grid = gridC[2][2]
        return grid


def changePlayer():
    global currentPlayer
    if currentPlayer == player1:
        currentPlayer = player2
    else:
        currentPlayer = player1


def checkWinner():
    player1Grid = []
    player2Grid = []
    for grid in occupiedGrid:
        if occupiedGrid[grid] == player1:
            player1Grid.append(grid)
        else:
            player2Grid.append(grid)
    for combination in winningGridCombinations:
        count1 = 0
        count2 = 0
        for j in combination:
            if j in player1Grid:
                count1 += 1
            if j in player2Grid:
                count2 += 1
        if count1 == 3:
            return combination
        if count2 == 3:
            return combination


def announceWinner(winnerGrid, winnerPlayer):
    global occupiedGrid, WinnerGrid, WinnerPlayer, running
    if winnerGrid == gridC[0]:
        screen.blit(horizontal, (0, -177))
    elif winnerGrid == gridC[1]:
        screen.blit(horizontal, (0, 0))
    elif winnerGrid == gridC[2]:
        screen.blit(horizontal, (0, 177))
    elif winnerGrid == [gridC[0][0], gridC[1][0], gridC[2][0]]:
        screen.blit(vertical, (-200, 0))
    elif winnerGrid == [gridC[0][1], gridC[1][1], gridC[2][1]]:
        screen.blit(vertical, (0, 0))
    elif winnerGrid == [gridC[0][2], gridC[1][2], gridC[2][2]]:
        screen.blit(vertical, (200, 0))
    elif winnerGrid == [gridC[0][0], gridC[1][1], gridC[2][2]]:
        screen.blit(slant1, (0, 0))
    elif winnerGrid == [gridC[0][2], gridC[1][1], gridC[2][0]]:
        screen.blit(slant, (0, 0))
    screen.blit(line, (-1, -1))
    pygame.display.update()

    time.sleep(1)

    if winnerPlayer == player1:
        screen.blit(winnerX, (20, 2))
    else:
        screen.blit(winnerO, (20, 2))
    pygame.display.update()
    x = True
    while x:
        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                running = False
                x = False

            if Event.type == pygame.KEYUP:
                if Event.key == pygame.K_RETURN:
                    x = False
                    occupiedGrid = {}


running = True
while running:
    WinnerGrid = None
    WinnerPlayer = None
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos()
            Grid = getGridNumber(position)
            if Grid not in occupiedGrid:
                occupiedGrid[Grid] = currentPlayer
                WinnerGrid = checkWinner()
                WinnerPlayer = currentPlayer
                changePlayer()

    for i in occupiedGrid:
        screen.blit(occupiedGrid[i], (i[0] + 36, i[1] + 25))
    if WinnerGrid is not None:
        announceWinner(WinnerGrid, WinnerPlayer)
    screen.blit(line, (-1, -1))
    pygame.display.update()
