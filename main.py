import pygame
import sys
import random
from settings import *
from sprites import *
pygame.init()


# Setting up the screen
SCREEN = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption("Rock Paper Scissors")
pygame.display.set_icon(icon.convert_alpha())

# Converting all the sprites
rock = rock.convert_alpha()
rock_rect = rock.get_rect(topleft=(250, 500))

paper = paper.convert_alpha()
paper_rect = paper.get_rect(topleft=(550, 500))

scissors = scissors.convert_alpha()
scissors_rect = rock.get_rect(topleft=(850, 500))


class Game:
    def __init__(self):
        self.choices = {
            "rock": 1,
            "paper": 2,
            "scissors": 3
        }
        self.winner = ""
        self.player_choice = None
        self.player_choice_str = ""
        self.computer_choice = None
        self.computer_choice_str = ""
        self.text = None
        self.text_rect = None

    def get_computer_choice(self):
        computer_choice = random.randint(1, 3)
        if computer_choice == self.choices['rock']:
            computer_choice_str = "rock"
            return computer_choice, computer_choice_str

        elif computer_choice == self.choices['paper']:
            computer_choice_str = "paper"
            return computer_choice, computer_choice_str

        elif computer_choice == self.choices['scissors']:
            computer_choice_str = "scissors"
            return computer_choice, computer_choice_str

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
                            player_choice = self.choices['rock']
                            player_choice_str = "rock"
                            return player_choice, player_choice_str

                        elif paper_rect.collidepoint(mouse_pos):
                            player_choice = self.choices['paper']
                            player_choice_str = "paper"
                            return player_choice, player_choice_str

                        elif scissors_rect.collidepoint(mouse_pos):
                            player_choice = self.choices['scissors']
                            player_choice_str = "scissors"
                            return player_choice, player_choice_str

            # Rendering the sprites to the screen
            SCREEN.blit(bg, bg_rect)
            SCREEN.blit(rock, rock_rect)
            SCREEN.blit(paper, paper_rect)
            SCREEN.blit(scissors, scissors_rect)

            pygame.display.update()

    def check_winner(self):
        if self.player_choice == self.choices['rock']:
            if self.computer_choice == self.choices['rock']:
                return "draw"

            elif self.computer_choice == self.choices['paper']:
                return "computer"

            elif self.computer_choice == self.choices['scissors']:
                return "player"

        elif self.player_choice == self.choices['paper']:
            if self.computer_choice == self.choices['rock']:
                return "player"

            elif self.computer_choice == self.choices['paper']:
                return "draw"

            elif self.computer_choice == self.choices['scissors']:
                return "computer"

        elif self.player_choice == self.choices['scissors']:
            if self.computer_choice == self.choices['rock']:
                return "computer"

            elif self.computer_choice == self.choices['paper']:
                return "player"

            elif self.computer_choice == self.choices['scissors']:
                return "draw"

    def set_text(self):
        if self.winner == "draw":
            self.text = font.render('Its a draw!!', True, (149, 150, 72))
            self.text_rect = self.text.get_rect(
                center=(SCREEN_HEIGHT//2, SCREEN_WIDTH//2))

        elif self.winner == "player":
            self.text = font.render('YOU WIN!!', True, (11, 158, 18))
            self.text_rect = self.text.get_rect(
                center=(SCREEN_HEIGHT//2, SCREEN_WIDTH//2))

        elif self.winner == "computer":
            self.text = font.render('YOU LOSE!!', True, (189, 0, 0))
            self.text_rect = self.text.get_rect(
                center=(SCREEN_HEIGHT//2, SCREEN_WIDTH//2))

    def run(self):
        self.player_choice, self.player_choice_str = self.get_player_choice()
        self.computer_choice, self.computer_choice_str = self.get_computer_choice()
        self.winner = self.check_winner()
        self.set_text()
        # set choices of player and computer in text variables using font
        choice_text_player = font_for_choice.render(f"Player's choice: {self.player_choice_str.capitalize()}", True, (136, 22, 184))
        choice_text_player_rect = choice_text_player.get_rect(topleft=(0, 0))
        choice_text_computer = font_for_choice.render(f"Computer's choice: {self.computer_choice_str.capitalize()}", True, (225, 225, 0))
        choice_text_computer_rect = choice_text_player.get_rect(topleft=(SCREEN_WIDTH, 0))

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

            # Rendering sprites
            SCREEN.blit(bg, bg_rect)
            SCREEN.blit(self.text, self.text_rect)
            SCREEN.blit(choice_text_player, choice_text_player_rect)
            SCREEN.blit(choice_text_computer, choice_text_computer_rect)
            SCREEN.blit(font.render("Press 'q' to quit!!", True, (214, 182, 219)), (SCREEN_WIDTH//2+75, SCREEN_HEIGHT-758))
            SCREEN.blit(font.render("Press SPACE to play again!!", True, (156, 126, 155)), (SCREEN_WIDTH//2-50, SCREEN_HEIGHT-650))

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    while True:
        if game.run():
            break
