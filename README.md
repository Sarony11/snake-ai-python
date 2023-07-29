# Snake game though reinforcement learning

## Introduction
Why waste time playing video games when you can train an AI to do it for you? Ok, maybe playing yourself is more fun but training an AI can be more educational.

Reinforcement learning is a type of machine learning that enables an agent to learn in an environment by trial and error using feedback from its own actions and experiences.

First you will create the game using Python and Pygame. Then you will create and train a neural network using PyTorch that can play the game better than most humans.

Patrick Loeber, also known as Python Engineer, created this course. He has created many popular courses related to Python and machine learning.

The girl and snake art for this course were created by Rachel Likes Pizza.

Here is what is what you will do in this four-part course:
- Learn the basics of Reinforcement Learning and Deep Q Learning
- Setup the environment and implement a snake game
- Implement an agent to control the game
- Create and train a neural network to play the game

## References
https://www.freecodecamp.org/news/train-an-ai-to-play-a-snake-game-using-python/
https://www.youtube.com/watch?v=L8ypSXwyBds

# Steps

## Step 0: Install requirements
1. Install Miniconda --> https://docs.conda.io/en/latest/miniconda.html
2. Create .gitignore file.

## Step 1: Setup the general environment
When start working in python I usually create the virtual environment and I prepare the requirements.txt. You can do it this like so:

```shell
conda create -n pygame_env python=3.6
conda activate pygame_env
pip install -r requirements.txt
```

## Step 2: Download the snake game
```bash
wget https://raw.githubusercontent.com/patrickloeber/python-fun/master/snake-pygame/snake_game.py
wget https://github.com/patrickloeber/python-fun/raw/master/snake-pygame/arial.ttf
```
