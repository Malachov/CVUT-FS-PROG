import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        #Spawnutí snake a směr
        self.body = [Vector2(5,10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0,0)
        self.new_block = False
        #Loadování animací snake
        self.head_up = pygame.image.load('Projects/Prochazka/Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Projects/Prochazka/Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Projects/Prochazka/Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Projects/Prochazka/Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('Projects/Prochazka/Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Projects/Prochazka/Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Projects/Prochazka/Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Projects/Prochazka/Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Projects/Prochazka/Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Projects/Prochazka/Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Projects/Prochazka/Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Projects/Prochazka/Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Projects/Prochazka/Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Projects/Prochazka/Graphics/body_bl.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound('Projects/Prochazka/Sound/crunch.wav')

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            #Pozice "bloku" s rectanglem
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)


            if index == 0:
                screen.blit(self.head, block_rect) #hlava
            elif index == len(self.body) - 1: #ocas
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block #blok tělo před
                next_block = self.body[index - 1] - block #blok tělo po
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect) #"rovné" bloky situace - vertikal
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect) #"rovné" bloky situace - horizontal
                else:   #"rohové" bloky pro všechny situace sousedících bloků
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    if previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    if previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    if previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self): #update hlavy pro různé směry
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self): #update ocasu pro různé směry
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:] #přidá nový blok
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False #deaktivuje proměnnou nový blok po snězení jablka
        else:
            body_copy = self.body[:-1] #"zkopíruje" tělo bez nového bloku
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self): #metoda pro zjištění, pokud bylo snězeno jablko pro růst
        self.new_block = True

    def play_crunch_sound(self): #přehrání zvuku
        self.crunch_sound.play()

    def reset(self): #reset po failu
        self.body = [Vector2(5,10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0,0)

class FRUIT:
    def __init__(self):
        self.randomize() #náhodně vložení jablka

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size + 10), int(self.pos.y * cell_size), cell_size, cell_size) #nakreslení rectanglu pro jablko
        screen.blit(apple, fruit_rect)        
        #pygame.draw.rect(screen, (126,166,114), fruit_rect)

    def randomize(self): #metoda pro náhodné generování souřadnic pro další jablko
        self.x = random.randint(0, cell_number-1)
        self.y = random.randint(0, cell_number-1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self): #volání metod na snake a jablko
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self): #update po framech a checknutí stavů
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self): #update herní plochy
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
            
    def check_collision(self): #kontrola spolknutí jablka hadem
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:]: #aby se jablko nespawnulo v hadovi
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number: #check kolize hada s okrajem mapy
            self.game_over()

        for block in self.snake.body[1:]: #kontrola kolize hada sama se sebou
            if block == self.snake.body[0]:
                self.game_over()


    def game_over(self): #reset po failu
        self.snake.reset()

    def draw_grass(self): #kreslení herní plochy, aby každý čtverec měl jiný odstín
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self): #nakreslení skore
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top-3, apple_rect.width + score_rect.width + 6, apple_rect.height + 6)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)

pygame.mixer.pre_init(44100, -16, 2, 512) #nastavení zvuku pro pygame
pygame.init()
cell_size = 40 #počet pixelů v buňce
cell_number = 20 #počet buňek
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size)) #otevření okna
clock = pygame.time.Clock() #hodiny, aby to na každém PC běželo stejně
apple = pygame.image.load('Projects/Prochazka/Graphics/apple_shrinked.png').convert_alpha() #load obrázku jablíčka
game_font = pygame.font.Font('Projects/Prochazka/Font/PoetsenOne-Regular.ttf', 25) #načtení fontu

SCREEN_UPDATE = pygame.USEREVENT #update pokud uživatel něco stiskne
pygame.time.set_timer(SCREEN_UPDATE, 150) #nastavení hodin

main_game = MAIN()

while True: #loop pro běh hry
    for event in pygame.event.get(): #vypnutí hry
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN: #stiskání šipek a kontrola, abych hadem necouval
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)                

    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
