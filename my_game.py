import pygame
import random
import sys

pygame.init()

width = 1000
height = 800

screen = pygame.display.set_mode((width, height))

enemy = pygame.image.load("bunny1_walk1.png")
player = pygame.image.load("alien_jump.png")

PLAYER_DEFAULT_IMAGE_SIZE = (64, 128)
ENEMY_DEFAULT_IMAGE_SIZE = (40, 60)

player = pygame.transform.scale(player, PLAYER_DEFAULT_IMAGE_SIZE)
enemy = pygame.transform.scale(enemy, ENEMY_DEFAULT_IMAGE_SIZE)

player_rect = player.get_rect()
enemy_rect = enemy.get_rect()

enemy_rect.topleft = (800, 480)
player_rect.topleft = (350, 200)

sound1 = pygame.mixer.Sound("8bit_bomb_explosion.wav")
sound2 = pygame.mixer.Sound("xeon6.ogg")
sound2.play()

pygame.mixer.music.set_volume(0.5)

font_name = pygame.font.SysFont("sitkatext", 69)

score = 0
sayac = 30  # Başlangıç süresi (saniye)
speed = 20  # Karakter hızı
FPS = 30  # Oyun hızı
clock = pygame.time.Clock()

def show_game_over(score):
    screen.fill((0, 0, 0))
    game_over_text = font_name.render("Oyun Bitti!", True, (255, 255, 255))
    game_over_rect = game_over_text.get_rect(center=(width / 2, height / 2 - 50))
    screen.blit(game_over_text, game_over_rect)

    score_text = font_name.render(f"Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(width / 2, height / 2 + 50))
    screen.blit(score_text, score_rect)

    pygame.display.update()
    pygame.time.delay(2000)  # 2 saniye bekleyin
    pygame.quit()
    sys.exit()

open = True
frame_counter = 0
while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= speed
    elif pressed_keys[pygame.K_RIGHT] and player_rect.right < width:
        player_rect.x += speed
    elif pressed_keys[pygame.K_UP] and player_rect.top > 0:
        player_rect.y -= speed
    elif pressed_keys[pygame.K_DOWN] and player_rect.bottom < height:
        player_rect.y += speed

    # Her saniye başında sayacı azalt
    frame_counter += 1
    if frame_counter == FPS:
        frame_counter = 0
        sayac -= 1

    if sayac <= 0:
        show_game_over(score)

    text2 = font_name.render(f"Süre: {sayac}", True, (255, 255, 255))
    text2_rect = text2.get_rect(topleft=(10, 10))

    text = font_name.render(f"Score: {score}", True, (255, 255, 255))
    text_rect = text.get_rect(topright=(width - 10, 10))

    pygame.draw.rect(screen, (255, 255, 255), enemy_rect, 1)
    pygame.draw.rect(screen, (255, 255, 255), player_rect, 1)

    if player_rect.colliderect(enemy_rect):
        score += 1
        enemy_rect.x = random.randint(0, width - 50)
        enemy_rect.y = random.randint(0, height - 50)
        sound1.play()

    screen.fill((0, 0, 0))
    screen.blit(text2, text2_rect)
    screen.blit(text, text_rect)
    screen.blit(enemy, enemy_rect)
    screen.blit(player, player_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
