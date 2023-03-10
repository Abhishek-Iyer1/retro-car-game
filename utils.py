import pygame
from pygame.locals import *
from pygame.event import Event
from pygame import Surface
from global_values import *
from player import Player, Meter

def paint_game_screen(screen: Surface):
    # Make a background environment for retro racing car game
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, [MIN_X, MIN_Y, MAX_X // 5, MAX_Y])
    pygame.draw.rect(screen, GREY, [MAX_X // 5, MIN_Y, MAX_X * 2 // 5, MAX_Y])
    pygame.draw.rect(screen, GREY, [MAX_X * 2 // 5, MIN_Y, MAX_X * 3 // 5, MAX_Y])
    pygame.draw.rect(screen, GREY, [MAX_X * 3 // 5, MIN_Y, MAX_X * 4 // 5, MAX_Y])
    pygame.draw.rect(screen, GREEN, [MAX_X * 4 // 5, MIN_Y, MAX_X, MAX_Y])
    pygame.draw.line(screen, BLACK, [MAX_X // 5,MIN_Y], [MAX_X // 5, MAX_Y], MAX_X // 200)
    pygame.draw.line(screen, YELLOW, [MAX_X * 2 // 5,MIN_Y], [MAX_X * 2 // 5, MAX_Y], MAX_X // 200)
    pygame.draw.line(screen, YELLOW, [MAX_X * 3 // 5,MIN_Y], [MAX_X * 3 // 5, MAX_Y], MAX_X // 200)
    pygame.draw.line(screen, BLACK, [MAX_X * 4 // 5,MIN_Y], [MAX_X * 4 // 5, MAX_Y], MAX_X // 200)

    for x in [MAX_X // 5 + MAX_X // 10, MAX_X // 2, MAX_X //2 + MAX_X // 5]:
        for y in range(10, MAX_X * 3 // 5, MAX_Y // 12):
            pygame.draw.line(screen, WHITE, [x, y], [x, y+ MAX_Y // 40], width = (MAX_X // 333 if ((MAX_X // 333) > 1 ) else round(MAX_X / 333)))

def handle_event(event: Event) -> list[bool]:
    global moveLeft, moveRight, moveUp, moveDown
    if event.type == KEYDOWN:
        # Handle movement keys LEFT, RIGHT, UP, DOWN
        print(event.key)
        if event.key == K_LEFT or event.key == K_a:
            moveRight = False
            moveLeft = True
        if event.key == K_RIGHT or event.key == K_d:
            moveLeft = False
            moveRight = True
        if event.key == K_UP or event.key == K_w:
            moveDown = False
            moveUp = True
        if event.key == K_DOWN or event.key == K_s:
            moveUp = False
            moveDown = True

    elif event.type == KEYUP:
        if event.key == K_ESCAPE:
            exit = True
        if event.key == K_LEFT or event.key == K_a:
            moveLeft = False
        if event.key == K_RIGHT or event.key == K_d:
            moveRight = False
        if event.key == K_UP or event.key == K_w:
            moveUp = False
        if event.key == K_DOWN or event.key == K_s:
            moveDown = False
    else:
        moveLeft = False
        moveRight = False
        moveUp = False
        moveDown = False

    return [moveLeft, moveRight, moveUp, moveDown]


def handle_movement(move_status: list[bool], player: Player):
    moveLeft, moveRight, moveUp, moveDown = move_status
    if player.left > (MAX_X // 5) and moveLeft: 
        player.move_left()
    if player.right < (MAX_X * 4 // 5) and moveRight:
        player.move_right()
    if player.top > MIN_Y and moveUp:
        player.move_up()
    if player.bottom < MAX_Y and moveDown:
        player.move_down()

def check_if_game_over(screen: Surface, fuel_meter: Meter):
    print(fuel_meter.value)
    if fuel_meter.value <= 0:
        game_over = True
    else:
        game_over = False
    return game_over

def paint_game_over_screen(screen: Surface):
    screen.fill(WHITE)
    font = pygame.font.SysFont('arial', 60, bold=True)
    text = font.render("GAME OVER", True, BLACK)
    screen.blit(text, (MAX_X // 2 - 120, MAX_Y // 2 - 60))