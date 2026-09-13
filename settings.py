# Current windows size
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 700

# REFERENCE:
# Reference resolution used for scaling
REF_SCREEN_WIDTH, REF_SCREEN_HEIGHT = 940, 650

# Base sizes at the reference resolution
REF_CHOICE_FONT_SIZE = 36
REF_RESULT_FONT_SIZE = 50
REF_RPS_WIDTH, REF_RPS_HEIGHT = 135, 135

# Calculating scaling
scale = min(SCREEN_WIDTH/REF_SCREEN_WIDTH, SCREEN_HEIGHT/REF_SCREEN_HEIGHT)

# Asset paths
FONT_PATH = "assets/fonts/font.ttf"
BACKGROUND_PATH = "assets/sprites/background.jpeg"
ROCK_PATH = "assets/sprites/rock.png"
PAPER_PATH = "assets/sprites/paper.png"
SCISSORS_PATH = "assets/sprites/scissors.png"
ICON_PATH = "assets/sprites/icon.jpg"
