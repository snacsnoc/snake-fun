# lets make a snake game


import pygame

pygame.init()

window_size = (500, 500)
screen = pygame.display.set_mode(window_size)

# Create the snake
snake = [(200, 200), (210, 200), (220, 200)]

# Create the food
food = (230, 210)

# Initialize the snake's starting position
snake_x = 300
snake_y = 300

# Set the snake's speed
snake_speed = 5

# Create the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the food
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food[0], food[1], 10, 10))

    # Check for arrow key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_x -= snake_speed
    if keys[pygame.K_RIGHT]:
        snake_x += snake_speed
    if keys[pygame.K_UP]:
        snake_y -= snake_speed
    if keys[pygame.K_DOWN]:
        snake_y += snake_speed

    # Draw the snake at its new position
    pygame.draw.rect(screen, (255, 255, 255), (snake_x, snake_y, 10, 10))

    print(f"snake position x: {snake_x} y: {snake_y}")

    if (snake_x, snake_y) == (food[0], food[1]):
        print("collision")

    # Update the screen
    pygame.display.update()

    # Wait a bit before checking for events
    pygame.time.wait(100)

pygame.quit()
