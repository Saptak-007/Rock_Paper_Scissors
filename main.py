import pygame
pygame.init()
import sys
import random
from settings import *
from sprites import *

# Setting up the screen
# SCREEN = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")
pygame.display.set_icon(icon.convert_alpha())

# Converting all the sprites
rock = rock.convert_alpha()
rock_rect = rock.get_rect()

paper = paper.convert_alpha()
paper_rect = paper.get_rect()

scissors = scissors.convert_alpha()
scissors_rect = scissors.get_rect()

# Setting the coordinates of the rps sprites using dynamic coordinates:
# Calculating the dynamic positions
y_sprites = SCREEN_HEIGHT*0.7
leftover_width = SCREEN_WIDTH - (rock_rect.width+paper_rect.width+scissors_rect.width)
gap_between_sprites = leftover_width / 4 # 4 = no.of sprites + 1 (since 1 more gap remains)

# Applying the calculated postions
rock_rect.topleft = (gap_between_sprites, y_sprites)
paper_rect.topleft = (rock_rect.right + gap_between_sprites, y_sprites)
scissors_rect.topleft = (paper_rect.right + gap_between_sprites, y_sprites)




class Game:
    def __init__(self):
        self.choices = {
            "rock": 1,
            "paper": 2,
            "scissors": 3
        }
        self.winner_outcomes = {
            0: "draw",
            1: "player",
            2: "computer"
        }

        self.result = None
        self.player_choice = None
        self.computer_choice = None
        self.toast = None

    def get_computer_choice(self):
        return random.randint(1, 3)

    def get_player_choice(self):
        while True:
            for event in pygame.event.get():
                # Checking if the user wants to quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Checking fpr the user's choice
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        if rock_rect.collidepoint(mouse_pos):
                            return self.choices['rock']

                        elif paper_rect.collidepoint(mouse_pos):
                            return self.choices['paper']

                        elif scissors_rect.collidepoint(mouse_pos):
                            return self.choices['scissors']

            # Rendering the sprites to the screen
            SCREEN.blit(bg, bg_rect)
            SCREEN.blit(rock, rock_rect)
            SCREEN.blit(paper, paper_rect)
            SCREEN.blit(scissors, scissors_rect)

            pygame.display.update()

    # This is different from the above function:
    # converts the numerical choices(used in internal logic) into its corresponding name.
    def get_name_from_choice(self, num_choice):
        for name, value in self.choices.items():
            if value==num_choice:
                return name

    def get_result(self):
        # Read the "result_logic.md" for understanding why we used:
        # (self.player_choice - self.computer_choice)%3        
        return self.winner_outcomes[(self.player_choice - self.computer_choice)%3]

    def set_text(self):
        if self.result == "draw":
            self.toast = font.render('Its a draw!!', True, (149, 150, 72))
            self.toast_rect = self.toast.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        elif self.result == "player":
            self.toast = font.render('YOU WIN!!', True, (11, 158, 18))
            self.toast_rect = self.toast.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        elif self.result == "computer":
            self.toast = font.render('YOU LOSE!!', True, (189, 0, 0))
            self.toast_rect = self.toast.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    def run(self):
        self.player_choice = self.get_player_choice()
        self.computer_choice = self.get_computer_choice()
        self.result = self.get_result()
        self.set_text()

        # set choices of player and computer in text variables using font
        choice_text_player = font_for_choice.render(f"Player's choice: {self.get_name_from_choice(self.player_choice).capitalize()}", True, (136, 22, 184))
        choice_text_player_rect = choice_text_player.get_rect(topleft=(0, 0))
        choice_text_computer = font_for_choice.render(f"Computer's choice: {self.get_name_from_choice(self.computer_choice).capitalize()}", True, (225, 225, 0))
        choice_text_computer_rect = choice_text_computer.get_rect(topright=(SCREEN_WIDTH, 0))

        while True:
            for event in pygame.event.get():
                # Checking if the user wants to quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return False
                    elif event.key == pygame.K_q:
                        return True

            # Rendering bg, toast, player's choice, computer's choice
            SCREEN.blit(bg, bg_rect)

            SCREEN.blit(self.toast, self.toast_rect)
            SCREEN.blit(choice_text_player, choice_text_player_rect)
            SCREEN.blit(choice_text_computer, choice_text_computer_rect)

            # Rendering quit text, play again text:
            # (1) Making the text, text_rect
            quit_text = font.render("Press 'q' to quit!!", True, (214, 182, 219))
            quit_text_rect =  quit_text.get_rect()

            play_again_text = font.render("Press SPACE to play again!!", True, (156, 126, 155))
            play_again_text_rect =  play_again_text.get_rect()

            # (2) Calculating the dynamic coordinates
            x_text = SCREEN_WIDTH/2
            leftover_height = SCREEN_HEIGHT - (self.toast_rect.bottom + quit_text_rect.height + play_again_text_rect.height)
            gap_between_text = leftover_height/3

            quit_text_rect.midtop = (x_text, self.toast_rect.bottom + gap_between_text)
            play_again_text_rect.midtop = (x_text, quit_text_rect.bottom + gap_between_text)

            SCREEN.blit(quit_text, quit_text_rect)
            SCREEN.blit(play_again_text, play_again_text_rect)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    while True:
        if game.run():
            break
