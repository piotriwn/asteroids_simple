import pygame  # Imports the Pygame library.


# Base class for game objects
# Defines a class CircleShape that inherits from pygame.sprite.Sprite, making it a Pygame sprite.
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):  # Constructor for the CircleShape class.
        # we will be using this later
        # Checks if the instance has a 'containers' attribute (used for sprite groups).
        if hasattr(self, "containers"):
            # Calls the parent class (Sprite) constructor, potentially adding it to sprite groups.
            super().__init__(self.containers)
        else:
            super().__init__()  # Calls the parent class (Sprite) constructor.

        # Creates a 2D vector for the object's position.
        self.position = pygame.Vector2(x, y)
        # Creates a 2D vector for the object's velocity, initialized to zero.
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius  # Stores the radius of the circle.

    def draw(self, screen):  # Method to draw the object on the screen.
        # sub-classes must override
        # Placeholder; this method should be implemented by subclasses to define how the object is drawn.
        pass

    def update(self, dt):  # Method to update the object's state.
        # sub-classes must override
        # Placeholder; this method should be implemented by subclasses to define how the object's state changes over time (dt).
        pass
