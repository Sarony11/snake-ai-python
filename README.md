# Snake game though reinforcement learning

## Step 1: Setup the general environment
When start working in python I usually create the virtual environment and I prepare the requirements.txt. You can do it this like so:

```shell
python3 -m venv env
source env/bin/activate
touch requirements.txt
echo "pygame==2.4.0" > requirements.txt
pip3 install -r requirements.txt
```
Also, creating the .gitignore from the begining its a great idea :)

Once you have Pygame installed, create a new Python file and import the necessary modules and also define some constants for the game, such as the screen size, the size of the snake and food, and the colors:

```python
import pygame
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SNAKE_SIZE = 20
FOOD_SIZE = 20
SNAKE_COLOR = (0, 255, 0)  # Green
FOOD_COLOR = (255, 0, 0)  # Red
BACKGROUND_COLOR = (0, 0, 0)  # Black
```

## Step 2: Initialize the Game Window
In this step, we'll initialize the game window using Pygame and define the main game loop. Add the following code:

```python
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(10)  # Controls the speed of the game, adjust as needed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
```

In this code, we initialize Pygame, create the game window with the specified dimensions, set the window caption, and create a clock object to control the game's frame rate. The game loop runs as long as the `running` variable is True. It handles quitting the game when the user closes the window.

The game loop also fills the screen with the background color and updates the display. Run the program to check if the game window opens successfully and if you can close it without errors.

```shell
python main.py
```
## Step 3: Create the Snake
In this step, we'll create the snake and enable it to move around the game window. We'll represent the snake as a list of coordinates, where each coordinate represents a segment of the snake's body.

Add the following code to your program, below the `running = True` line:

```python
snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]  # Snake starts at the center of the screen
direction = "RIGHT"  # Initial direction

def move_snake():
    head = snake[0]
    x, y = head

    if direction == "UP":
        y -= SNAKE_SIZE
    elif direction == "DOWN":
        y += SNAKE_SIZE
    elif direction == "LEFT":
        x -= SNAKE_SIZE
    elif direction == "RIGHT":
        x += SNAKE_SIZE

    new_head = (x, y)
    snake.insert(0, new_head)
    snake.pop()  # Remove the last segment to maintain the size of the snake

def draw_snake(screen):
    for segment in snake:
        x, y = segment
        pygame.draw.rect(screen, SNAKE_COLOR, (x, y, SNAKE_SIZE, SNAKE_SIZE))

```

In this code, we initialize the snake list with a single coordinate representing the snake's head at the center of the screen. The `direction` variable keeps track of the current movement direction of the snake.

The `move_snake` function updates the snake's position based on the current direction. It removes the last segment of the snake to maintain its size and inserts the new head segment at the front of the snake.

The `draw_snake` function is responsible for rendering the snake on the game screen. It iterates over each segment of the snake and draws a rectangle representing each segment using the `pygame.draw.rect` function.

Now, within the game loop, add the following code:

```python
while running:
    clock.tick(10)  # Controls the speed of the game, adjust as needed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)
    move_snake()        # It will update the position
    draw_snake(screen)  # It will renden the snake on the screen
    pygame.display.update()
```

This will call the `move_snake` and `draw_snake` functions within each iteration of the game loop to update and render the snake.

Try running the program now and observe the snake moving on the screen.

## Step 4: Add Keyboard Input
In this step, we'll enable keyboard input to control the movement of the snake. We'll use the arrow keys to change the direction of the snake.

Add the following code below the `direction = "RIGHT"` line:

```python
def change_direction(new_direction):
    global direction

    if new_direction == pygame.K_UP and direction != "DOWN":
        direction = "UP"
    elif new_direction == pygame.K_DOWN and direction != "UP":
        direction = "DOWN"
    elif new_direction == pygame.K_LEFT and direction != "RIGHT":
        direction = "LEFT"
    elif new_direction == pygame.K_RIGHT and direction != "LEFT":
        direction = "RIGHT"

def handle_key_press():
    keys = pygame.key.get_pressed()

    for key in keys:
        if keys[key]:
            change_direction(key)
```

In this code, the `change_direction` function takes a new direction as input and updates the `direction` variable if the new direction is valid. It ensures that the snake cannot turn back on itself by checking the current direction.

The `handle_key_press` function retrieves the current state of the keyboard and iterates over the pressed keys. It calls the `change_direction` function with the corresponding arrow key if any of the arrow keys are pressed.

Now, within the game loop, add the following code:

```python
while running:
    clock.tick(10)  # Controls the speed of the game, adjust as needed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)
    move_snake()        # It will update the position
    draw_snake(screen)  # It will renden the snake on the screen
    handle_key_press()  # It allows the snake moviment
    pygame.display.update()
```

This will call the `handle_key_press` function within each iteration of the game loop to handle keyboard input and update the snake's direction accordingly.

Run the program and try using the arrow keys to change the snake's direction. The snake should respond to the key presses and move accordingly.
