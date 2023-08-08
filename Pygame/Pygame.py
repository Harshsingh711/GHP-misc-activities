# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
color = "purple"
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player2_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(color)

    pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.draw.circle(screen, "blue", player2_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 600 * dt
    if keys[pygame.K_s]:
        player_pos.y += 600 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 600 * dt
    if keys[pygame.K_d]:
        player_pos.x += 600 * dt
    if keys[pygame.K_i]:
        player2_pos.y -= 600 * dt
    if keys[pygame.K_k]:
        player2_pos.y += 600 * dt
    if keys[pygame.K_j]:
        player2_pos.x -= 600 * dt
    if keys[pygame.K_l]:
        player2_pos.x += 600 * dt

    if player_pos.y > 720:
        player_pos.y = 0
        color = "yellow"
    if player_pos.y < 0:
        player_pos.y = 720
        color  = "purple"
    if player_pos.x > 1280:
        player_pos.x = 0
        color  = "purple"
    if player_pos.x < 0:
        player_pos.x = 1280
        color  = "yellow"
    if player2_pos.y > 720:
        player2_pos.y = 0
    if player2_pos.y < 0:
        player2_pos.y = 720
    if player2_pos.x > 1280:
        player2_pos.x = 0
    if player2_pos.x < 0:
        player2_pos.x = 1280

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()