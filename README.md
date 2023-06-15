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

