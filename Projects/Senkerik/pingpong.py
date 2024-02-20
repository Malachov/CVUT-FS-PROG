import pygame
from pygame.locals import *

pygame.init()

screen_width=600
screen_height=500


fpsClock = pygame.time.Clock()

screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong")

#define font
font= pygame.font.SysFont("Constantia", 30)

#define game variables
live_ball = False
margin=50
cpu_score=0
player_score=0
fps=60
winner=0



#define colours
bg=(50, 25, 50)
white=(255, 255, 255)

def draw_board():
    screen.fill(bg)
    pygame.draw.line(screen, white, (0, margin), (screen_width, margin))



def draw_text(text, font, text_col, x, y):
    img= font.render(text, True, text_col)
    screen.blit(img, (x, y))


class paddle():
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.rect = Rect(self.x, self.y, 20, 100)
        self.speed = 5


    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.rect.move_ip(0, -1*self.speed)
        if key[pygame.K_DOWN]:
            self.rect.move_ip(0, self.speed)   

    def ai(self):
        #ai to move the paddle automaticaly
        # move down
        if self.rect.centery < pong.rect.top and self.rect.bottom < screen_height:
            self.rect.move_ip(0, self.speed)
        # move up
        if self.rect.centery > pong.rect.bottom and self.rect.top > margin:
            self.rect.move_ip(0, -1 * self.speed)


    def draw(self):
        pygame.draw.rect(screen,white,self.rect)

class ball():
    def __init__(self, x, y):
        self.reset(x, y)



    def move(self):
        
        #add colision detection
        #check colision with top margin
        if self.rect.top < margin:
            self.speed_y*= -1
        #check colision with bottom of the screen
        if self.rect.top > screen_height:
            self.speed_y*= -1
        #check colision with paddles
        if self.rect.colliderect(player_paddle): 
            self.speed_x += 0.5
            self.speed_x *= -1
        elif self.rect.colliderect(cpu_paddle):
            self.speed_x += -0.5
            self.speed_x *= -1

        #check for out of bounds
        if self.rect.left < 0:
            self.winner = 1
        if self.rect.right > screen_width:
            self.winner = -1  




        #update ball position
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


        return self.winner


    def draw(self):
        pygame.draw.circle(screen,white,(self.rect.x + self.ball_rad, self.rect.y + self.ball_rad),self.ball_rad)

    def reset(self, x, y):
        self.x = x
        self.y = y 
        self.ball_rad = 8
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = -4
        self.speed_y = 4
        self.winner = 0# 1 means player 1 has, -1 means cpu has scored 

#create paddles
player_paddle= paddle(screen_width - 40, screen_height // 2)
cpu_paddle= paddle(20, screen_height // 2)


#create pong ball
pong = ball(screen_width - 60, screen_height // 2 + 50)
run=True
while run:

    fpsClock.tick(fps)

    draw_board()
    draw_text("CPU: " + str(cpu_score), font, white, 20, 15)
    draw_text("P1: " + str(player_score), font, white, screen_width -100, 15)
    
    
    
    #draw paddles
    player_paddle.draw()
    cpu_paddle.draw()
   
   
    if live_ball == True:
        #move ball
        winner = pong.move()
        if winner == 0:
            #move paddle
            player_paddle.move()
            cpu_paddle.ai()
            #draw ball
            pong.draw()
        else:
            live_ball = False
            if winner == 1:
                player_score += 1
            elif winner == -1:
                cpu_score +=1 




    #print player instuctions
    if live_ball == False:
        if winner == 0:
            draw_text("CLICK ANYWHERE TO START", font, white, 100, screen_height // 2 - 100)
        
        if winner == 1:
            if player_score == 7:
                draw_text("YOU WIN!", font, white, 210, screen_height // 2 - 100)
                draw_text("CLICK ANYWHERE TO ", font, white, 100, screen_height // 2 - 50)
                draw_text("RESTART THE GAME", font, white, 100, screen_height // 2 - 100)
                player_score=0
                cpu_score=0
            else:
                draw_text("YOU SCORED!", font, white, 210, screen_height // 2 - 100)
                draw_text("CLICK ANYWHERE TO CONTINUE", font, white, 60, screen_height // 2 - 50)
        if winner == -1:
            
            if cpu_score == 7:
                draw_text("CPU WIN!", font, white, 210, screen_height // 2 - 100)
                draw_text("CLICK ANYWHERE TO ", font, white, 100, screen_height // 2 - 50)
                draw_text("RESTART THE GAME", font, white, 100, screen_height // 2 - 100)
                player_score=0
                cpu_score=0
            else:
                draw_text("CPU SCORED!", font, white, 210, screen_height // 2 - 100)
                draw_text("CLICK ANYWHERE TO CONTINUE", font, white, 60, screen_height // 2 - 50)


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False:
            live_ball = True
            pong.reset(screen_width - 60, screen_height // 2 + 50)

    pygame.display.update()


pygame.quit()