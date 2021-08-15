import pygame
import time 

from pygame.constants import MOUSEBUTTONDOWN

# board = [ [ 3, 1, 6, 5, 7, 8, 4, 9, 2 ],
#          [ 5, 2, 9, 1, 3, 4, 7, 6, 8 ],
#          [ 4, 8, 7, 6, 2, 9, 5, 3, 1 ],
#          [ 2, 6, 3, 0, 1, 5, 9, 8, 7 ],
#          [ 9, 7, 4, 8, 6, 0, 1, 2, 5 ],
#          [ 8, 5, 1, 7, 9, 2, 6, 4, 3 ],
#          [ 1, 3, 8, 0, 4, 7, 2, 0, 6 ],
#          [ 6, 9, 2, 3, 5, 1, 8, 7, 4 ],
#          [ 7, 4, 5, 0, 8, 6, 3, 1, 0 ] ]


# board2 = [ [ 3, 1, 6, 5, 7, 8, 4, 9, 2 ],
#          [ 5, 2, 9, 1, 3, 4, 7, 6, 8 ],
#          [ 4, 8, 7, 6, 2, 9, 5, 3, 1 ],
#          [ 2, 6, 3, 0, 1, 5, 9, 8, 7 ],
#          [ 9, 7, 4, 8, 6, 0, 1, 2, 5 ],
#          [ 8, 5, 1, 7, 9, 2, 6, 4, 3 ],
#          [ 1, 3, 8, 0, 4, 7, 2, 0, 6 ],
#          [ 6, 9, 2, 3, 5, 1, 8, 7, 4 ],
#          [ 7, 4, 5, 0, 8, 6, 3, 1, 0 ] ]

# All colors used 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
green2 = (92,182,107)
dark_green = (4,75,20)
blue = (50, 153, 213)

pygame.init()

dis_width = 450
dis_height = 500
 
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Sudoku by Nassos')
myFont = pygame.font.SysFont("Arial", 25, True)
clock = pygame.time.Clock()

solved_board = [ [ 1, 5, 6, 2, 6, 2, 3, 4, 8 ],
                [ 2, 5, 9, 1, 4, 6, 2, 9, 1 ],
                [ 3, 7, 9, 5, 8, 1, 4, 6, 2 ],
                [ 9, 3, 7, 9, 2, 5, 1, 4, 1 ],
                [ 5, 8, 1, 5, 2, 7, 9, 3, 5 ],
                [ 1, 5, 7, 4, 8, 8, 1, 5, 7 ],
                [ 9, 7, 2, 2, 6, 1, 5, 4, 1 ],
                [ 6, 4, 4, 1, 5, 2, 6, 3, 9 ],
                [ 7, 9, 2, 8, 7, 4, 2, 1, 2 ] ]

board = [ [ 1, 0, 6, 0, 0, 2, 3, 0, 0 ],
         [ 0, 5, 0, 0, 0, 6, 0, 9, 1 ],
         [ 0, 0, 9, 5, 0, 1, 4, 6, 2 ],
         [ 0, 3, 7, 9, 0, 5, 0, 0, 0 ],
         [ 5, 8, 1, 0, 2, 7, 9, 0, 0 ],
         [ 0, 0, 0, 4, 0, 8, 1, 5, 7 ],
         [ 0, 0, 0, 2, 6, 0, 5, 4, 0 ],
         [ 0, 0, 4, 1, 5, 0, 6, 0, 9 ],
         [ 9, 0, 0, 8, 7, 4, 2, 1, 0 ] ]


board2 = [ [ 1, 0, 6, 0, 0, 2, 3, 0, 0 ],
         [ 0, 5, 0, 0, 0, 6, 0, 9, 1 ],
         [ 0, 0, 9, 5, 0, 1, 4, 6, 2 ],
         [ 0, 3, 7, 9, 0, 5, 0, 0, 0 ],
         [ 5, 8, 1, 0, 2, 7, 9, 0, 0 ],
         [ 0, 0, 0, 4, 0, 8, 1, 5, 7 ],
         [ 0, 0, 0, 2, 6, 0, 5, 4, 0 ],
         [ 0, 0, 4, 1, 5, 0, 6, 0, 9 ],
         [ 9, 0, 0, 8, 7, 4, 2, 1, 0 ] ]


def backtrack():

    for i in range(9):
        for j in range(9):
            if board2[i][j] == 0:    # It must be solved
                flag = False 
                
                for z in range(9):
                    if isSafe(i,j,z+1) == True:
                        board2[i][j] = z + 1;
                        flag = True

                        if isSolved() == True:
                            print("EEEEEEEEE")
                            return True
                        # backtrack()

                if flag == False:                # number is 0 and it didnt changed
                    print("--------------")
                    for k in range(9):
                        print(board[k])
                    if isSolved() == True:
                            print("EEEEEEEEE")
                            return True
                    backtrack()
                  
               

# def backtrack2(): 
#     for i in range(9):
#         for j in range(9):
#             if ((board2[i][j] == 0) or (board[i][j] == 0 and (isSafe(i,j, board2[i][j]) == False))):    # It must be solved
#                 print("gia row " , i , " col " ,j , " num: " , board2[i][j])
#                 for z in range(9):
#                     if isSafe(i,j,z+1) == True:

                        

#                         if i == 8 and j == 8:
#                             if isSolved == True:
#                                 print("EEEEEEEEE")
#                                 return True
#                             else:
#                                 flag = True
#                                 # backtrack()
#                         backtrack()

def isSolved(boole = False):
    for i in range(9):
        for j in range(9):
            if (isSafe(i, j, board2[i][j]) == False) or board2[i][j] == 0:
                if boole == True:
                    print("row " , i , " col " ,j , " num: " , board2[i][j])
                return False
    return True

# Checks whether it will be legal to assign num to the given row, col
def isSafe(row, col, num):
   
    # Check if we find the same num in the similar row , we return false
    for x in range(9):
        if board2[row][x] == num:
            return False
 
    # Check if we find the same num in the similar column , we retutn false
    for x in range(9):
        if board2[x][col] == num:
            return False
 
    # Check if we find the same num in the particular 3*3 matrix, return false
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board2[i + startRow][j + startCol] == num:
                return False
    return True


def drawGrid():
    blockSize = 50 # Set the size of the grid block
    
    # Draw the horizontal lines
    pygame.draw.line(dis, black, (0, 150), (dis_width, 150), 4)
    pygame.draw.line(dis, black, (0, 300), (dis_width, 300), 4)
    pygame.draw.line(dis, black, (0, 450), (dis_width, 450), 4)
    
    # Draw the vertical lines
    pygame.draw.line(dis, black, (150, 0), (150, dis_height - 50), 4)
    pygame.draw.line(dis, black, (300, 0), (300, dis_height - 50), 4)

    for x in range(0, dis_width, blockSize):
        for y in range(0, dis_height - 50, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(dis, black, rect, 1)

def displayBoard(startTime):

    dis.fill(white)
    drawGrid()
    displayNumbers()
    pygame.display.update()

def gameLoop():
    
    game_over = False
    game_close = False
    startTime = time.time()

    displayBoard(startTime)
    while not game_over:
         
        white_rect = pygame.Rect(0, 455, dis_width, 455)
        pygame.draw.rect(dis, white, white_rect)
        randNumLabel = myFont.render("Time: " + str(time.time() - startTime), 1, black)
        dis.blit(randNumLabel, (340, 465))
        pygame.display.update()

        while game_close == True:
            # message("You Lost! Press C-Play Again or Q-Quit", red)
            # Your_score(Length_of_snake - 1)
            # pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
         
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = pos[0]
                posy = pos[1]
                x_block = (pos[0] // 50) * 50
                y_block = (pos[1] // 50) * 50
                if y_block > 400:
                    continue
                displayBoard(startTime)
                pygame.draw.rect(dis, red, (x_block, y_block, 50, 50), 4)
                pygame.display.update()
                print("to x einai: ",x_block , " kai to y einai: " , y_block)

            if event.type == pygame.KEYDOWN:        # Get the number pressed
                num = -10
                if event.key == pygame.K_1:
                    num = 1
                if event.key == pygame.K_2:
                    num = 2
                if event.key == pygame.K_3:
                    num = 3
                if event.key == pygame.K_4:
                    num = 4
                if event.key == pygame.K_5:
                    num = 5
                if event.key == pygame.K_6:
                    num = 6
                if event.key == pygame.K_7:
                    num = 7
                if event.key == pygame.K_8:
                    num = 8
                if event.key == pygame.K_9:
                    num = 9
                if num == -10:
                    pass
                print("patithike to: " , num)
                solved_board_i = posx // 50;
                solved_board_j = posy // 50;
                print("to x einai: ",posx , " kai to y einai: " , posy)
                print("solved board: " , solved_board[solved_board_j][solved_board_i], " to i einai: " , solved_board_j , " kai to j einai: ", solved_board_i)
                
                # If the number is correct
                if num == solved_board[solved_board_j][solved_board_i]:
                    board[solved_board_j][solved_board_i] = num
                    displayBoard(startTime)
                else:                   # Get a strike
                    pass

                
                

        
          
# ---------------------------------------------------------------- MAIN ---------------------------------------------------------------- #

def displayNumbers():
    width = 19;
    height = 12;
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                randNumLabel = myFont.render(str(board[i][j]), 1, black)
                dis.blit(randNumLabel, (width, height))
            width+=50
        height+=50
        width = 19


for i in range(9):
    print(board[i])

# backtrack()

print( "----------------------------------------------------------------" )
# for i in range(9):
#     print(board2[i])

#Check if board is solved or not
if isSolved(True):
    print("The board is solved!")
else:
    print("The board is not solved!")

gameLoop()
