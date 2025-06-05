# Imports the CircleShape class, which serves as a base for the Player.
from circleshape import CircleShape
from constants import *  # Imports all constants (like PLAYER_RADIUS).
import pygame  # Imports the Pygame library.


# Defines the Player class, inheriting from CircleShape.
class Player(CircleShape):
    def __init__(self, x, y):  # Constructor for the Player class.
        # Calls the constructor of the parent class (CircleShape) with position and player-specific radius.
        super().__init__(x, y, PLAYER_RADIUS)
        # Initializes the player's rotation angle to 0 degrees.
        self.rotation = 0

    # Calculates the three vertices of the triangle representing the player.
    def triangle(self):
        # Defines a vector pointing forward, rotated by the player's current rotation.
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # Defines a vector pointing to the right, scaled relative to the radius.
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        # Calculates the front vertex of the triangle.
        a = self.position + forward * self.radius
        # Calculates one of the back vertices of the triangle.
        b = self.position - forward * self.radius - right
        # Calculates the other back vertex of the triangle.
        c = self.position - forward * self.radius + right
        return [a, b, c]  # Returns a list of the three vertex coordinates.

    def draw(self, screen):  # Method to draw the player on the screen.
        # Draws a white triangle (polygon) on the screen using the calculated vertices, with a line thickness of 2.
        polygon = pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):  # Method to rotate the player.
        # Updates the player's rotation angle based on turn speed and delta time.
        self.rotation += PLAYER_TURN_SPEED * dt

    # Method to update the player's state based on input.
    def update(self, dt):
        keys = pygame.key.get_pressed()  # Gets the state of all keyboard keys.

        if keys[pygame.K_a]:  # Checks if the 'A' key is pressed.
            # Rotates the player left. The -1 indicates counter-clockwise rotation.
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:  # Checks if the 'D' key is pressed.
            # Rotates the player right.
            self.rotate(dt)
        if keys[pygame.K_w]:  # Checks if the 'W' key is pressed.
            # Moves the player forward.
            self.move(dt)
        if keys[pygame.K_s]:  # Checks if the 'S' key is pressed.
            # Moves the player backward. The -1 indicates reverse movement.
            self.move(-1 * dt)

    # We start with a unit vector pointing straight up from (0, 0) to (0, 1).
    # We rotate that vector by the player's rotation, so it's pointing in the direction the player is facing.
    # We multiply by PLAYER_SPEED * dt. A larger vector means faster movement.
    # Add the vector to our position to move the player.
    def move(self, dt):  # Method to move the player.
        # Calculates the forward direction vector based on the current rotation.
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # Updates the player's position by moving in the forward direction, scaled by speed and delta time.
        self.position += forward * PLAYER_SPEED * dt
