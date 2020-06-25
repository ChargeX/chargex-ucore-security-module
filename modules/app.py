import sys
import time
# import tkinter as tk
# from tkinter.font import Font
import pygame

#from thirdparty import botan2 as bt


class App:

    def run(self):
        print('Hello, cm3 tinkered!')

        # window = tk.Tk()
        # menu = tk.Menu()
        # font = tk.font.Font(font=menu["font"])
        # print(font.actual())


        # frame = tk.Frame(window)
        # frame.pack()
        # button = tk.Button(frame, command=quit)
        # font = tk.font.Font(font=button["font"])
        # print(font.actual())

#        button.pack(side=tk.LEFT)
        # window.mainloop()


#        print('Botan version number: ', bt.version_major())
        #
        pygame.init()
        size = width, height = (400, 400)
        speed = [1, 1]
        black = 0, 0, 0
        white = 255, 255, 255
        #
        screen = pygame.display.set_mode(size)
        screen.fill(white)

        font = pygame.font.SysFont("comicsansms", 72)


        label = font.render("Some text!", 1, (255,255,0))
        screen.blit(label, (100, 100))
        #
        button = pygame.Rect(380, 10, 15, 15)
        pygame.draw.rect(screen, (black), button)
        pygame.display.update()
        # ball = pygame.image.load('rsz_ball.gif')
        # ball_rect = ball.get_rect()
        
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
        
                    if button.collidepoint(pos[0], pos[1]):
                        sys.exit()
        
            # ball_rect = ball_rect.move(speed)
            # if ball_rect.left < 0 or ball_rect.right > width:
            #     speed[0] = -speed[0]
            # if ball_rect.top < 0 or ball_rect.bottom > height:
            #     speed[1] = -speed[1]
        
            # screen.fill(black)
            # screen.blit(ball, ball_rect)
            # pygame.display.flip()
        
            pygame.draw.rect(screen, black, button)
            pygame.display.update()
        
            time.sleep(0.005)
