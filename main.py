import pygame
pygame.init()
import random
from settings import *
from game_assets import *

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
        self.toast_rect = None

    def get_computer_choice(self):
        return random.randint(1, 3)

    def set_computer_choice(self):
        self.computer_choice = self.get_computer_choice()

    def get_player_choice(self, mouse_pos):
        # Checking for the user's choice
        if rock_rect.collidepoint(mouse_pos):
            return self.choices['rock']

        elif paper_rect.collidepoint(mouse_pos):
            return self.choices['paper']

        elif scissors_rect.collidepoint(mouse_pos):
            return self.choices['scissors']

        return None # if user clicked somewhere other than the rps images

    # This is different from the above function:
    # converts the numerical choices(used in internal logic) into its corresponding name.
    def get_name_from_choice(self, num_choice):
        for name, value in self.choices.items():
            if value == num_choice:
                return name       

    def get_result(self):
        # Read the "result_logic.md" for understanding why we used:
        # (self.player_choice - self.computer_choice)%3        
        return self.winner_outcomes[(self.player_choice - self.computer_choice)%3]

    def set_result(self):
        self.result = self.get_result() 

    def set_toast(self):
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
        while True:
            # Rendering background
            SCREEN.blit(bg, bg_rect)

            for event in pygame.event.get():
                # Checking if the user wants to quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.player_choice is not None:
                        self.player_choice = None
                        self.computer_choice = None
                        self.result = None
                        self.toast = None
                        self.toast_rect = None

                    elif event.key == pygame.K_q and self.player_choice is not None:
                        return True
                    
                # Getting player's choice
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.player_choice is None:
                    # self.player_choice = self.get_player_choice(pygame.mouse.get_pos())
                    self.player_choice = self.get_player_choice(event.pos)

            if self.player_choice is not None:
                if self.computer_choice is None:
                    # Set computer choice
                    self.set_computer_choice()

                    # Setting the result
                    self.set_result()

                    # Setting the toast
                    self.set_toast()

                    # set choices of player and computer in text variables using font
                    player_choice_text = font_for_choice.render(f"Player's choice: {self.get_name_from_choice(self.player_choice).capitalize()}", True, (136, 22, 184))
                    player_choice_text_rect = player_choice_text.get_rect(topleft=(0, 0))

                    computer_choice_text = font_for_choice.render(f"Computer's choice: {self.get_name_from_choice(self.computer_choice).capitalize()}", True, (225, 225, 0))
                    computer_choice_text_rect = computer_choice_text.get_rect(topright=(SCREEN_WIDTH, 0))

                    # Dealing with quit and play again text:
                    # (1) Making the text, text_rect
                    quit_text = font.render("Press 'q' to quit!!", True, (214, 182, 219))
                    quit_text_rect =  quit_text.get_rect()
                    
                    play_again_text = font.render("Press SPACE to play again!!", True, (156, 126, 155))
                    play_again_text_rect =  play_again_text.get_rect()
                    
                    # (2) Calculating the dynamic coordinates
                    x_text = SCREEN_WIDTH/2
                    leftover_height = SCREEN_HEIGHT - (self.toast_rect.bottom + quit_text_rect.height + play_again_text_rect.height)
                    gap_between_text = leftover_height/3

                    # (3) Applying calculated coordinates
                    quit_text_rect.midtop = (x_text, self.toast_rect.bottom + gap_between_text)
                    play_again_text_rect.midtop = (x_text, quit_text_rect.bottom + gap_between_text)

                # Rendering player_choice, computer_choice, toast, quit_text, play_again_text
                SCREEN.blit(player_choice_text, player_choice_text_rect)
                SCREEN.blit(computer_choice_text, computer_choice_text_rect)
                SCREEN.blit(self.toast, self.toast_rect)
                SCREEN.blit(quit_text, quit_text_rect)
                SCREEN.blit(play_again_text, play_again_text_rect)

            else:
                SCREEN.blit(rock, rock_rect)
                SCREEN.blit(paper, paper_rect)
                SCREEN.blit(scissors, scissors_rect)

            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()
