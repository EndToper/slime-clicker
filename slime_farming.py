import pygame
import random as rnd
import os
import texts
import time

pygame.init()

pygame.display.set_caption("EndToper's slime clicker")

#width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
#переменные
WIDTH, HEIGHT = 960, 760
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
FPS = 60
run = True
image_adress = os.path.join('slime_clicker','slime.png')
my_image = pygame.image.load(image_adress).convert_alpha()
image_adress = os.path.join('slime_clicker','enchanted_book.png')
img= pygame.image.load(image_adress).convert_alpha()
image_adress = os.path.join('slime_clicker','1.png')
img2= pygame.image.load(image_adress).convert_alpha()
image_adress = os.path.join('slime_clicker','x2_silver.png')
img3= pygame.image.load(image_adress).convert_alpha()
image_adress = os.path.join('slime_clicker','x2_gold.jpg')
img4= pygame.image.load(image_adress).convert_alpha()
image_adress = os.path.join('slime_clicker','x-wing.png')
img5 = pygame.image.load(image_adress).convert_alpha()
image_adress = os.path.join('slime_clicker','2.png')
img6 = pygame.image.load(image_adress).convert_alpha()
img6 = pygame.transform.scale(img6, (150, 150))
img5 = pygame.transform.scale(img5, (80, 80))
img3 = pygame.transform.scale(img3, (100, 100))
img4 = pygame.transform.scale(img4, (100, 100))
img2 = pygame.transform.scale(img2, (80, 80))
my_image = pygame.transform.scale(my_image, (250, 250))
img = pygame.transform.scale(img, (50, 50))
clicked = 0
clc = 0
click = 10**4
click_im = 0
thousand = 1000000
div = 1
typ = ''
times = 0
t = 0
t2 = time.time()
cps = 0
m ,b,t,q,qui,s,sep,o,n,d= 10**6,10**9,10**12,10**15,10**18,10**21,10**24,10**27,10**30,10**33
sep2,o2,n2,d2 = 1e+24,1e+27,1e+30,1e+33
yes = {1:'',1000:'',m:'million',b:'billion',t:'trillion',q:'quadrillion',qui:'quintillion',s:'sextillion',
       sep:'septillion',o:'octillion',n:'nonillion',d:'decillion',sep2:'septillion',o2:'octillion',n2:'nonillion',d2:'decillion'}
#классы
class Clicker(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((250, 250))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.img = my_image
    def draw(self):
        screen.blit(self.img,(self.x,self.y))
class Up(pygame.sprite.Sprite):
    def __init__(self,x,y,image,cost,c):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((c, c))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.img = image
        self.cost = cost
        self.lvl = 0
        self.cost_im = cost
        self.t = 1000000
        self.typ = ''
    def draw(self):
        screen.blit(self.img,(self.x,self.y))
#объекты
slime = Clicker(125,100)
book = Up(650,35,img,10,50)
friend = Up(630,130,img2,250,75)
silver_x2 = Up(80,500,img3,10001,100)
gold_x2 = Up(280,500,img4,100001,100)
x_wing = Up(630,250,img5,12345,80)
lis = Up(630,400,img6,999999,150)
mass = [book,friend,silver_x2,gold_x2,x_wing,lis]
#functions
def view(x,y):
    global times
    fontObj = pygame.font.Font('freesansbold.ttf', 25)
    textSurfaceObj = fontObj.render(f'+{click}', False, (255,255,255), (31,174,233))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x,y)
    screen.blit(textSurfaceObj, textRectObj)
    times -= 1
def book_name():
    fontObj = pygame.font.Font('freesansbold.ttf', 25)
    textSurfaceObj = fontObj.render(f'Разящий клинок {book.lvl}', False, (255,255,255), (231,195,173))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (800,25)
    screen.blit(textSurfaceObj, textRectObj)
def book_cost():
    fontObj = pygame.font.Font('freesansbold.ttf', 15)
    textSurfaceObj = fontObj.render(f'стоимость {book.cost_im} {book.typ}', False, (255,255,255), (231,195,173))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (830,50)
    screen.blit(textSurfaceObj, textRectObj)
def f_name():
    fontObj = pygame.font.Font('freesansbold.ttf', 25)
    textSurfaceObj = fontObj.render(f'Авантюрист {friend.lvl} ранга', False, (255,255,255), (231,195,173))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (800,110)
    screen.blit(textSurfaceObj, textRectObj)
def f_cost():
    fontObj = pygame.font.Font('freesansbold.ttf', 15)
    textSurfaceObj = fontObj.render(f'стоимость {friend.cost_im} {friend.typ}', False, (255,255,255), (231,195,173))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (830,170)
    screen.blit(textSurfaceObj, textRectObj)
#запуск функций
def func():
    slime.draw()
    book.draw()
    friend.draw()
    silver_x2.draw()
    gold_x2.draw()
    x_wing.draw()
    lis.draw()
    book_name()
    book_cost()
    texts.book_text()
    f_name()
    texts.f_text()
    f_cost()
    texts.silver_name()
    texts.gold_name()
    texts.silver_cost(silver_x2)
    texts.gold_cost(gold_x2)
    texts.x_name(x_wing)
    texts.x_text()
    texts.x_cost(x_wing)
    texts.l_text()
    texts.l_name(lis)
    texts.l_cost(lis)
#главный цикл
t = t2
while run:
    for i in mass:
        texts.trans(i,yes)
    t2 = time.time()
    if t2 - t >= 1:
        t = t2
        clicked += cps
    screen.fill((231,195,173))
    func()
    if times > 0:
        view(rx,ry)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                run = False
            #debuging start
            if i.key == pygame.K_f:
                print(typ)
                print(div)
                print(thousand)
            if i.key == pygame.K_g:
                clicked = 1
            if i.key == pygame.K_t:
                print('gold -', gold_x2.cost,gold_x2.cost_im)
                print('silver -', silver_x2.cost,silver_x2.cost_im)
            #debuging end
        if i.type == pygame.MOUSEBUTTONDOWN:
            if slime.rect.collidepoint(pygame.mouse.get_pos()):
                clicked += click
                times = 11
                rx,ry = pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]-10
            if book.rect.collidepoint(pygame.mouse.get_pos()):
                if clicked >= book.cost:
                    clicked -= book.cost
                    book.cost = round(book.cost * rnd.randint(11,16)/10)
                    book.lvl += 1
                    click = click + rnd.randint(1,5)
            if friend.rect.collidepoint(pygame.mouse.get_pos()):
                if clicked >= friend.cost:
                    clicked -= friend.cost
                    friend.cost = round(friend.cost * rnd.randint(11,16)/10)
                    friend.lvl += 1
                    cps = cps + rnd.randint(1,5)
            if silver_x2.rect.collidepoint(pygame.mouse.get_pos()):
                if clicked >= silver_x2.cost:
                    clicked -= silver_x2.cost
                    silver_x2.cost = round(silver_x2.cost ** (rnd.randint(12,17)/10))
                    click = click * 2
            if gold_x2.rect.collidepoint(pygame.mouse.get_pos()):
                if clicked >= gold_x2.cost:
                    clicked -= gold_x2.cost
                    gold_x2.cost = round(gold_x2.cost ** (rnd.randint(12,17)/10))
                    cps = cps * 2
            if x_wing.rect.collidepoint(pygame.mouse.get_pos()):
                if clicked >= x_wing.cost:
                    clicked -= x_wing.cost
                    x_wing.cost = round(x_wing.cost * rnd.randint(15,21)/10)
                    x_wing.lvl += 1
                    cps = cps + rnd.randint(100,150)
            if lis.rect.collidepoint(pygame.mouse.get_pos()):
                if clicked >= lis.cost and lis.lvl < 9:
                    clicked -= lis.cost
                    lis.cost = round(lis.cost ** 1.3)
                    lis.lvl += 1
                    cps = cps + 99999 ** (1+(lis.lvl/10))
                    click += 9999 ** (1+(lis.lvl/10))
    if clicked >= clc:
        clc = clicked
    if clicked // thousand >= 1 and clicked % thousand >= 0:
        typ = yes[thousand]
        div = thousand
        thousand = 1000*thousand
    elif clicked // thousand == 0 and clicked != 0:
        thousand = round(thousand/1000)
        typ = yes[thousand]
        div = thousand
    click_im = clicked/div
    if div == 1:
        click_im = int(click_im)
    else:
        click_im = round(click_im,3)
    fontObj = pygame.font.Font('freesansbold.ttf', 25)
    textSurfaceObj = fontObj.render(f'killed slimes - {click_im} {typ}', False, (255,255,255), (231,195,173))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (250,100)
    screen.blit(textSurfaceObj, textRectObj)
    
    pygame.display.flip()
    
pygame.quit()