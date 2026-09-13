import pygame
from settings import *

# Load sprites:
# Load background
bg = pygame.transform.scale(pygame.image.load(BACKGROUND_PATH), (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_rect = bg.get_rect(topleft=(0, 0))

# Load sprites of rock, paper, and scissors
rps_width, rps_height = (int(REF_RPS_WIDTH*scale), int(REF_RPS_HEIGHT*scale))

rock = pygame.transform.scale(pygame.image.load(ROCK_PATH), (rps_width, rps_height))
paper = pygame.transform.scale(pygame.image.load(PAPER_PATH), (rps_width, rps_height))
scissors = pygame.transform.scale(pygame.image.load(SCISSORS_PATH), (rps_width, rps_height))
icon = pygame.image.load(ICON_PATH)

# Load fonts:
font = pygame.font.Font(FONT_PATH, int(REF_RESULT_FONT_SIZE*scale))
font_for_choice = pygame.font.Font(FONT_PATH, int(REF_CHOICE_FONT_SIZE*scale))
