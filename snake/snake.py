import pygame
import random
import time
pygame.mixer.init()
pygame.init()


white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 238, 0)
black = (0, 0, 0)
maroon = (59, 0, 0)
blue = (0, 112, 146)

p = pygame.display.set_mode((1200,600))
pygame.display.set_caption("This is a Game")
pygame.display.update()
clock1 = pygame.time.Clock()
font = pygame.font.SysFont(None,55)
bgimg = pygame.image.load("img4.jpg")
bgimg = pygame.transform.scale(bgimg,(1200 , 600))


def text_win(text , color , x , y):
    screen_text = font.render(text , True , color)
    p.blit(screen_text,[x,y])

def plot_snake(gameWindow , color , snake_list , sx1 , sx2):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow , color , [ x , y , sx1 , sx2])  

def welcome():
    exit_game = False
    while not exit_game :
        p.fill(black)
        text_win(("WELCOME TO THE SNAKE JAZZ") , white , 295 , 200)
        text_win(("PRESS BAR to continue") , white , 380 , 250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.load("Beep.mp3")
                pygame.mixer.music.play()
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("middle.mp3")
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock1.tick(60)

def gameloop():
        x = 45
        y = 45
        size_1 = 10
        size_2 = 10
        exit_game = False
        fps = 40
        vel_x = 5
        vel_y = 0
        food_x = random.randint(0 , 1190)
        food_y = random.randint(0 , 590)
        score = 0
        snake_list =[]
        snake_lenth = 1
        game_over = False
        while not exit_game:
            if game_over == True:
                pygame.mixer.music.load("Beep.mp3")
                pygame.mixer.music.play()
                p.fill(white)
                text_win("Game Over PRESS ENTER to continue" , maroon , 245 , 230)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            welcome() 
                    if event.type == pygame.QUIT:
                        exit_game = True             

            else:
                
                x = x + vel_x
                y = y + vel_y
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True
                        pygame.mixer.music.load("Beep.mp3")
                        pygame.mixer.music.play() 

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            vel_x = 5
                            vel_y = 0
                        if event.key == pygame.K_LEFT:
                            vel_x = -5
                            vel_y = 0
                        if event.key == pygame.K_DOWN:
                            vel_y = 5
                            vel_x = 0
                        if event.key == pygame.K_UP:
                            vel_y = -5
                            vel_x = 0
                        if event.key == pygame.K_3:
                            score += 10    
                p.fill(white)
                p.blit(bgimg, (0,0))
                if abs(x - food_x)<6 and abs(y - food_y)<6:
                    score = score+10
                    food_x = random.randint(0 , 1190)
                    food_y = random.randint(0 , 520)
                    snake_lenth += 15
                    # with open("highscore.txt" , "w") as file:
                    #     file.write(str(score))
                    with open("highscore.txt") as file2:
                        high = file2.read()
                        if score >= int(high):
                            high = score
                            with open("highscore.txt" , "w") as f:
                                f.write(str(high))
                                pygame.mixer.music.load("Beep.mp3")
                                pygame.mixer.music.play() 

                           
                head = []
                head.append(x)
                head.append(y)
                snake_list.append(head)
                
                if len(snake_list)>snake_lenth:
                    del snake_list[0] 

                # pygame.draw.rect(p , black , [ x , y , size_1 , size_2])
                pygame.draw.rect(p , red , [ food_x , food_y , size_1 , size_2])
                plot_snake(p , black , snake_list , size_1 , size_2)
                text_win(("SCORE: " + str(score)),blue,5,10)
                with open("highscore.txt") as file2:
                        high = file2.read()
                text_win(("HIGHSCORE: "+str(high)), blue, 850,10) 

                if head in snake_list[:-1]:
                    game_over = True 
                if (x == 0) or (x > 1200) or (y == 0) or (y>600):
                    game_over = True    
            
            pygame.display.update()
            clock1.tick(fps)  


welcome()
pygame.quit()
quit()


