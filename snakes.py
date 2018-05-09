import pygame, sys, random, time

check_errors = pygame.init()

if check_errors[1]:
    print('there was {0} errors'.format(check_errors[1]))
else:
    print ('no errors.')
