from pynput.mouse import Listener
import pygame
import time

pygame.init()
ui_click= pygame.mixer.Sound("lib\sounds\Interfaceclick.mp3")

def on_click(x,y,button,pressed):
    if pressed:
        pygame.mixer.Sound.play(ui_click)



with Listener(on_click=on_click) as listener:
    listener.join()
    time.sleep(.5)



