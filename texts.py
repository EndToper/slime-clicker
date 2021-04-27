import pygame
import random as rnd
import os

pygame.init()
WIDTH, HEIGHT = 960, 760
screen = pygame.display.set_mode((WIDTH,HEIGHT))

def book_text():
    fontObj = pygame.font.Font('freesansbold.ttf', 15)
    textSurfaceObj2 = fontObj.render(f'За клик вы убиваете больше', False, (255,255,255), (231,195,173))
    textSurfaceObj3 = fontObj.render(f'слизи (увеличение от 1 до 5)', False, (255,255,255), (231,195,173))
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = (810,70)
    textRectObj3 = textSurfaceObj2.get_rect()
    textRectObj3.center = (810,90)
    screen.blit(textSurfaceObj3, textRectObj3)
    screen.blit(textSurfaceObj2, textRectObj2)

def f_text():
    fontObj = pygame.font.Font('freesansbold.ttf', 15)
    textSurfaceObj = fontObj.render(f'Статичный доход от 1 до 5 в секунду', False, (255,255,255), (231,195,173))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (800,135)
    screen.blit(textSurfaceObj, textRectObj)

def trans(i,mass):
    if i.cost // i.t >= 1 and i.cost % i.t >= 0:
        i.typ = mass[i.t]
        div = i.t
        i.t = i.t * 1000
    elif i.cost // i.t == 0 and i.cost != 0:
        i.t = round(i.t/1000)
        i.typ = mass[i.t]
        div = i.t
    i.cost_im = i.cost/div
    i.cost_im = round(i.cost_im,3)

def silver_name():
    fontObj = pygame.font.Font('freesansbold.ttf', 15)
    textSurfaceObj = fontObj.render(f'Клики приносят', False, (255,255,255), (231,195,173))
    lol = fontObj.render('в 2 раза больше', False, (255,255,255), (231,195,173))
    textRectObj = textSurfaceObj.get_rect()
    simple = lol.get_rect()
    textRectObj.center = (120,645)
    simple.center = (120,665)
    screen.blit(lol,simple)
    screen.blit(textSurfaceObj, textRectObj)
def gold_name():
    fontObj = pygame.font.Font('freesansbold.ttf', 15)
    textSurfaceObj = fontObj.render(f'Cps увеличивается', False, (255,255,255), (231,195,173))
    lol = fontObj.render('в 2 раза', False, (255,255,255), (231,195,173))
    textRectObj = textSurfaceObj.get_rect()
    simple = lol.get_rect()
    textRectObj.center = (330,645)
    simple.center = (330,665)
    screen.blit(lol,simple)
    screen.blit(textSurfaceObj, textRectObj)
def silver_cost(silver):
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render(f'стоимость {silver.cost_im} {silver.typ}', False, (255,255,255), (231,195,173))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (120,610)
    screen.blit(textSurfaceObj, textRectObj)
def gold_cost(silver):
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render(f'стоимость {silver.cost_im} {silver.typ}', False, (255,255,255), (231,195,173))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (360,610)
    screen.blit(textSurfaceObj, textRectObj)
def x_name(x):
    fontObj = pygame.font.Font('freesansbold.ttf', 25)
    textSurfaceObj = fontObj.render(f'''{x.lvl} x-wing'ов''', False, (255,255,255), (231,195,173))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (830,220)
    screen.blit(textSurfaceObj, textRectObj)
def x_text():
    fontObj = pygame.font.Font('freesansbold.ttf', 15)
    textSurfaceObj = fontObj.render(f'Cps возрастают', False, (255,255,255), (231,195,173))
    lol = fontObj.render('от 100 до 150', False, (255,255,255), (231,195,173))
    textRectObj = textSurfaceObj.get_rect()
    simple = lol.get_rect()
    textRectObj.center = (830,280)
    simple.center = (830,300)
    screen.blit(lol,simple)
    screen.blit(textSurfaceObj, textRectObj)
def x_cost(silver):
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render(f'стоимость {silver.cost_im} {silver.typ}', False, (255,255,255), (231,195,173))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (830,250)
    screen.blit(textSurfaceObj, textRectObj)
def l_text():
    fontObj = pygame.font.Font('freesansbold.ttf', 15)
    textSurfaceObj = fontObj.render(f'ТеБе НуЖнА СиЛа?', False, (255,255,255), (231,195,173))
    lol = fontObj.render('многократно увеличивает все показатели', False, (255,255,255), (231,195,173))
    textRectObj = textSurfaceObj.get_rect()
    simple = lol.get_rect()
    textRectObj.center = (730,600)
    simple.center = (730,620)
    screen.blit(lol,simple)
    screen.blit(textSurfaceObj, textRectObj)
def l_name(silver):
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render(f'Снято печатей {silver.lvl}', False, (255,255,255), (231,195,173))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (730,580)
    screen.blit(textSurfaceObj, textRectObj)
def l_cost(silver):
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render(f'стоимость {silver.cost_im} {silver.typ}', False, (255,255,255), (231,195,173))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (850,400)
    screen.blit(textSurfaceObj, textRectObj)