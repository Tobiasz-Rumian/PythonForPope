import time

import pygame

pygame.mixer.init()
pygame.mixer.music.load("Barka.mp3")
pygame.mixer.music.play()


def check_if_continue():
    barka_flags = open("BarkaFlags", "r")
    flags = []
    for line in barka_flags:
        flags.append(line)
    barka_flags.close()

    stopFlag = "false" in str(flags[0])[str(flags[0]).index("=") + 1:]
    return stopFlag


while pygame.mixer.music.get_busy() == True & check_if_continue():
    time.sleep(5)
    continue
