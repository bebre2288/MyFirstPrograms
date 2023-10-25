# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import os
pygame.joystick.init()
# joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
joysticks = pygame.joystick.Joystick(0)
joysticks.init()
WIDTH = 500
HEIGHT = 480
FPS = 40
list = ['badge_1.png','badge_12.png' ]
print("random.choice используется для выбора случайного элемента из списка - ", random.choice(list))
# настройка папки ассетов
game_folder = os.path.dirname(__file__)
img_folder = os.path.join('c:\prj\prg', 'img')
player_img = pygame.image.load(os.path.join(img_folder, 'badge_01.png'))
mob_img=pygame.image.load(os.path.join(img_folder,'eee_sm.png'))
mob_img2=pygame.image.load(os.path.join(img_folder, 'badge_1.png'))
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.top =HEIGHT -10
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
        if keystate[pygame.K_UP]:
            self.speedy = -8
        if self.speedx == 0 and self.speedy == 0:
            j_updown = round(pygame.joystick.Joystick(0).get_axis(1)) 
            j_rightleft = round(pygame.joystick.Joystick(0).get_axis(0)) 
            self.speedx = j_rightleft*8
            self.speedy = j_updown*8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        self.speedx = 0
        self.rect.y += self.speedy
        if self.rect.bottom> HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        self.speedy = 0
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mob_img
        self.rect = self.image.get_rect()
        print (self.rect.width)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 6)
        self.speedx = random.randrange(-3, 3)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
    def update(self):
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()

bullets = pygame.sprite.Group()
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
    font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
def show_go_screen():
    draw_text(screen, "!ТЕБЯ УЖАЛИЛ ПЧЕЛОБАВ!", 29, WIDTH / 2, HEIGHT / 5)
    draw_text(screen, "на клавиатуре стрелки для управления ", 22,
              WIDTH / 2, HEIGHT / 3)
    draw_text(screen, "пробел для стрельбы", 22,
              WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Press a key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
            if pygame.joystick.Joystick(0).get_button(4) == 1:
                waiting = False
def show_screen():
    draw_text(screen, "пауза", 64, WIDTH / 2, HEIGHT / 5)
    draw_text(screen, "Press a key(L2) to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")
                if event.button == 6:
                    waiting = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    waiting = False 
                    game_paused = False
# Цикл игры
score=0
game_over = True
game_paused = False
running = True
while running:
    score+=1/40
    if game_over:
        score+=0
        print("И СНОВА ДРАТУТИ!")
        show_go_screen ()
        game_over = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        powerups = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(8):
            newmob()
        score=0
        clock.tick(1)
    if game_paused:
        show_screen ()
        game_paused = False
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
              player.shoot()
        elif event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYAXISMOTION:
            print("Joystick button pressed.")
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.", event.button)
            if event.button == 6:
                game_paused = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                game_paused = True
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == 5:
                player.shoot()
        elif event.type == pygame.JOYBUTTONUP:
            if event.button == 0:
                print('333333')
        elif event.type == pygame.JOYBUTTONUP:
            if event.button == 7:
                print('333333')
    # Обновление
    all_sprites.update()
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
     # Проверка, не ударил ли моб игрока
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        player.lives = 0
    # Если игрок умер, игра окончена
    if player.lives == 0:
        print("GAME-OVER!")
        game_over = True
    # Рендеринг
    screen.fill(BLUE)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    font_name = pygame.font.match_font('arial')
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
pygame.quit()