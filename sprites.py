import pygame
from settings import *

# Load sprites:
# Load background
bg = pygame.transform.scale(pygame.image.load("assets/sprites/background.jpeg"), (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_rect = bg.get_rect(topleft=(0, 0))

# Load sprites of rock, paper, and scissors
RPS_WIDTH, RPS_HEIGHT = 150, 150

rock = pygame.transform.scale(pygame.image.load("assets/sprites/rock.png"), (RPS_HEIGHT, RPS_WIDTH))
paper = pygame.transform.scale(pygame.image.load("assets/sprites/paper.png"), (RPS_HEIGHT, RPS_WIDTH))
scissors = pygame.transform.scale(pygame.image.load("assets/sprites/scissors.png"), (RPS_HEIGHT, RPS_WIDTH))
icon = pygame.image.load("assets/sprites/icon.jpg")
