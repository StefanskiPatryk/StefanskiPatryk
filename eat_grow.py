import pygame
import random
import time

character_image = pygame.image.load('character.png')
owoc_image = pygame.image.load('fruit.png')

scaled_character_image = pygame.transform.scale(character_image, (int(character_image.get_width() * 0.2), int(character_image.get_height() * 0.2)))
scaled_owoc_image = pygame.transform.scale(owoc_image, (int(owoc_image.get_width() * 0.2), int(owoc_image.get_height() * 0.2)))

pygame.init()

background_color = (255, 255, 255)
(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')

class Owoc:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

running = True
owoce = []
licznik_owocow = 0

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

character_x, character_y = width // 2, height // 2
last_fruit_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.time()

    if current_time - last_fruit_time > 1.5: 
        if random.randint(0, 100) < 5:
            x = random.randint(0, width - 32)
            y = 0
            owoc = Owoc(x, y, scaled_owoc_image)
            owoce.append(owoc)
            last_fruit_time = current_time

    for owoc in owoce:
        owoc.y += 1
        if owoc.y > height:
            owoce.remove(owoc)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and character_x > 0:
        character_x -= 5
    if keys[pygame.K_RIGHT] and character_x < width - 32:
        character_x += 5
    if keys[pygame.K_UP] and character_y > 0:
        character_y -= 5
    if keys[pygame.K_DOWN] and character_y < height - 32:
        character_y += 5
    character_x = max(0, min(width-120, character_x))
    for owoc in owoce:
        if (
            character_x < owoc.x + 32 and
            character_x + 32 > owoc.x and
            character_y < owoc.y + 32 and
            character_y + 32 > owoc.y
        ):
            owoce.remove(owoc)
            licznik_owocow += 1

    screen.fill(background_color)

    for owoc in owoce:
        screen.blit(owoc.image, (owoc.x, owoc.y))

    screen.blit(scaled_character_image, (character_x, character_y))

    text = font.render(f'Zebrane owoce: {licznik_owocow}', True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
