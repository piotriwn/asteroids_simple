# Imports the Pygame library, which is used for developing 2D games.
import pygame
from constants import *
from player import Player  # Imports the Player class from the player.py file.


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()  # Initializes all imported Pygame modules.
    # Creates the game window with the specified width and height.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Creates a Clock object, which can be used to control the game's framerate.
    clock = pygame.time.Clock()
    # Initializes delta time (dt), which will store the time elapsed since the last frame.
    dt = 0
    # Creates an instance of the Player class, positioned at the center of the screen.
    # Creates a sprite group to hold all objects that need their update method called.
    updatables = pygame.sprite.Group()
    # Creates a sprite group to hold all objects that need to be drawn.
    drawables = pygame.sprite.Group()
    # Assigns these groups to the Player class so instances are automatically added.
    Player.containers = (drawables, updatables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:  # Main game loop. The game continues to run as long as this loop is active.
        # Gets all events from the Pygame event queue (e.g., keyboard presses, mouse movements).
        for event in pygame.event.get():
            # Checks if the event is the user clicking the window's close button.
            if event.type == pygame.QUIT:
                return  # Exits the main function, thereby ending the game.
        # Fills the entire screen with black. This clears the screen for the new frame.
        screen.fill("black")
        # Calls the update method for all sprites in the 'updatables' group.
        updatables.update(dt)
        # Calls the draw method of the player object to draw it on the screen.
        for drawable in drawables:  # Iterates through all sprites in the 'drawables' group.
            # Calls the draw method for each sprite to render it on the screen.
            drawable.draw(screen)
        # Updates the full display surface to the screen, showing what's been drawn.
        pygame.display.flip()
        # Limits the game to 60 frames per second and returns the time since the last tick in milliseconds, then converts to seconds.
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
