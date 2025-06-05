SCREEN_WIDTH = 1280  # Defines the width of the game screen in pixels.
SCREEN_HEIGHT = 720  # Defines the height of the game screen in pixels.

ASTEROID_MIN_RADIUS = 20  # Defines the minimum radius for an asteroid.
# Defines the number of different sizes or types of asteroids.
ASTEROID_KINDS = 3
# Defines the rate at which asteroids spawn, in seconds.
ASTEROID_SPAWN_RATE = 0.8
# Calculates the maximum radius for an asteroid based on minimum radius and kinds.
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

PLAYER_RADIUS = 20  # Defines the radius of the player's ship.
# Defines how fast the player's ship can turn, in degrees per second.
PLAYER_TURN_SPEED = 300
# Defines the movement speed of the player's ship, in pixels per second.
PLAYER_SPEED = 200
