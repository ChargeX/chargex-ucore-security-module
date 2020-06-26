import sys
import time
import pygame
import math
import random

import modules.utils as utils
from modules.keymanager import KeyManager
import thirdparty.botan2 as bt

TEST_MSG_LIST = ['Message_1', 'Message_2', 'Message_3', 'Message_4']
CHARS_PER_LINE = 40

class App:

    def run(self):
        print('Program Started...!')

        # algorithm parameters for botan
        algorithm = 'ecdsa'
        algorithm_params = 'secp256k1'
        hash_func = 'EMSA1(SHA-256)'

        key_manager = KeyManager(algorithm=algorithm, algorithm_params=algorithm_params, hash_func=hash_func)

        # colors
        black = 0, 0, 0
        white = 255, 255, 255
        grey = 122, 122, 122

        # initilaize pygame
        pygame.init()

        # initialize screen
        size = width, height = (400, 400)
        screen = pygame.display.set_mode(size)
        screen.fill(white)

        # message area
        msg_area = (50, 50, 300, 200)
        msg_label_text = pygame.font.SysFont("monospace", 12)
        msg_label_surf, msg_label_rect = utils.text_objects("", msg_label_text, black)
        msg_button_label_center = [200, 100]
        msg_label_rect.center = (msg_button_label_center[0], msg_button_label_center[1])

        # button rects
        close_button_rect = (75, 300, 100, 40)
        close_button_label_center = (125, 320)
        close_button = pygame.Rect(*close_button_rect)

        gen_button_rect = (225, 300, 100, 40)
        gen_button_label_center = (275, 320)
        gen_button = pygame.Rect(*gen_button_rect)

        # button labels
        close_label_text = pygame.font.SysFont("monospace", 12)
        close_label_surf, close_label_rect = utils.text_objects("Close App", close_label_text, black)
        close_label_rect.center = close_button_label_center
 
        gen_label_text = pygame.font.SysFont("monospace", 12)
        gen_label_surf, gen_label_rect = utils.text_objects("Generate", gen_label_text, black)
        gen_label_rect.center = gen_button_label_center

        # render buttons and layouts
        pygame.draw.rect(screen, (grey), msg_area)
        screen.blit(msg_label_surf, msg_label_rect)
        pygame.draw.rect(screen, (grey), close_button)
        screen.blit(close_label_surf, close_label_rect)
        pygame.draw.rect(screen, (grey), gen_button)
        screen.blit(gen_label_surf, gen_label_rect)
        pygame.display.update()


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    if close_button.collidepoint(pos[0], pos[1]):
                        sys.exit()
                    if gen_button.collidepoint(pos[0], pos[1]):
                        screen.fill(white)

                        pygame.draw.rect(screen, (grey), msg_area)
                        pygame.draw.rect(screen, (grey), close_button)
                        screen.blit(close_label_surf, close_label_rect)
                        pygame.draw.rect(screen, (grey), gen_button)
                        screen.blit(gen_label_surf, gen_label_rect)

                        signature = key_manager.sign(TEST_MSG_LIST[random.randint(0, 3)]).hex()
            
                        print(math.ceil(len(signature) / CHARS_PER_LINE))
                        for i in range(math.ceil(len(signature) / CHARS_PER_LINE)):
                            msg_label_surf, msg_label_rect = utils.text_objects(signature[(i * CHARS_PER_LINE): min(((i + 1) * CHARS_PER_LINE), len(signature))], msg_label_text, black)
                            msg_label_rect.center = (msg_button_label_center[0], msg_button_label_center[1] + i * 15)
                            screen.blit(msg_label_surf, msg_label_rect)

            pygame.display.update()

	        # delay
            time.sleep(0.05)
