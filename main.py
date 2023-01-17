import pygame

from global_values import *
from player import Player, Meter
from utils import *

pygame.init()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project 0")
exit = False

# Instantiate basic screen
paint_game_screen(screen)

# Instantiate player
player = Player(screen, [450, 425, 100, 150])

# Istantiate Fuel Meter
fuel_meter = Meter(screen, [900, 100, 20, 100])

# Define constants
time_elapsed_since_fuel_leak = 0
game_over = False

#Instantiate clock
clock = pygame.time.Clock()
fuel_clock = pygame.time.Clock()


#Game begins, update loop
while not exit:
    print(f"GAME OVER: {game_over}")
    if not game_over:
        print(f"Fuel Meter: {fuel_meter.value}")
        game_over = check_if_game_over(screen, fuel_meter)
        dt = fuel_clock.tick()
        moveLeft = False; moveRight = False; moveUp = False; moveDown = False
        time_elapsed_since_fuel_leak += dt
        # Handle all events while game is ongoing
        for event in pygame.event.get():
            print(f"Event: {event}")

            # Exit case: When cross is pressed, exit status is updated, game is quit
            if event.type == pygame.QUIT:
                exit = True
            
            move_status: list[bool] = handle_event(event)
        
        handle_movement(move_status, player)
        time_elapsed_since_fuel_leak = fuel_meter.leak(time_elapsed_since_fuel_leak)

        paint_game_screen(screen)
        player.update(screen)
        fuel_meter.update(screen)
        pygame.display.flip()
        clock.tick(FPS)
    else:
        paint_game_over_screen(screen)
        # Handle all events while game is ongoing
        for event in pygame.event.get():
            print(f"Event: {event}")

            # Exit case: When cross is pressed, exit status is updated, game is quit
            if event.type == pygame.QUIT:
                exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == K_KP_ENTER:
                    game_over = False
                    fuel_meter = Meter(screen, [900, 100, 20, 100])
                    print(game_over)
        
        pygame.display.flip()

            