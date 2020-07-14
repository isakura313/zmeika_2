import pygame, sys, random

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500

DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

SPEED = 4
SIZE = 20
FPS = 10
fpsClock = pygame.time.Clock()
# pygame.mixer.init()
# pygame.mixer.music.load('Frank Sinatra - New York, New York (www.hotplayer.ru).mp3')



def make_new_apple():
    apple_x = random.randint(0, WINDOW_WIDTH - SIZE) # определение позиции
    apple_y = random.randint(0, WINDOW_HEIGHT - SIZE) # определение позиции
    apple = pygame.Rect(apple_x, apple_y, SIZE, SIZE)
    return apple

def add_part_of_snake(snake, snake_tail, head):
    update = [-SIZE * x for x in head]
    if len(snake_tail) == 0:
        snake_tail.append(snake.move(update[0], update[1]))
    else:
        snake_tail.append(snake_tail[len(snake_tail) - 1].move(update[0], update[1]))

def draw_snake(snake, snake_tail, head):
    tmp = snake.move(0, 0)
    head_speed = [SPEED * x  for x in head]
    snake.move_ip(head_speed[0], head_speed[1])
    pygame.draw.rect(DISPLAY, (0, 255, 0), snake)
    if len(snake_tail) == 0:
        return
    pygame.draw.rect(DISPLAY, (0, 0, 0),snake_tail[len(snake_tail) -1])
    colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (100, 100, 0)]
    for i in range(0, len(snake_tail) - 2):
        snake_tail[len(snake_tail) - 2 - i] = snake_tail[len(snake_tail) - 3 -i]
        pygame.draw.rect(DISPLAY, (0,0,255), snake_tail[len(snake_tail) - 2 -i])
    snake_tail[0] = tmp
    pygame.draw.rect(DISPLAY, random.choice(colors), snake_tail[0])


def gaming():
    """ игра начинается здесь"""
    count = 0
    pygame.font.init() #инициализация работы со шрифтами
    # font = pygame.font.Font('2.ttf', 32)
    # pygame.mixer.music.play(loops=-1)
    snake = pygame.Rect(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, SIZE, SIZE)
    snake_tail = []
    head = UP
    apple = make_new_apple() #здесь создавалось яблочко
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and head != RIGHT:
                    head = LEFT
                if event.key == pygame.K_RIGHT and head != LEFT:
                    head = RIGHT
                if event.key == pygame.K_UP and head != DOWN:
                    head = UP
                if event.key == pygame.K_DOWN and head != UP:
                    head = DOWN


        if snake.bottom > WINDOW_HEIGHT or snake.top < 0 or snake.left < 0 or snake.right > WINDOW_WIDTH:
            return
        if len(snake_tail) !=0  and snake.collidelist(snake_tail) < 0 :
            return
        if snake.colliderect(apple):
            #это когда змея сьедает яблоко
            count += 1
            # text = font.render(str(count), True, (0, 255, 0), (0, 0, 255))
            print(count) #чтобы удосстовериться что все работает
            # countRect = pygame.Rect(70, 20, 0 ,0 ) #создание нашего прямоугольника со счетом
            # countRect.center = (100, 100)
            # DISPLAY.blit(text, countRect)
            add_part_of_snake(snake, snake_tail, head)
            apple = make_new_apple()
        DISPLAY.fill((0, 0, 0))
        speed_head = [SPEED * x for x in head]
        snake.move_ip(speed_head[0], speed_head[1])
        draw_snake(snake, snake_tail, head)
        pygame.draw.rect(DISPLAY, (255, 0, 0), apple)
        pygame.display.update()
        fpsClock.tick(FPS)

gaming()
pygame.quit()
sys.exit()
