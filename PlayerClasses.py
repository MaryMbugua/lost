import pygame, sys
from pygame.locals import *

#Player class-------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, images):
        '''x: starting x coordinate
        y: starting y coordinate
        images: 3 image tuple (standing, step1, step2)'''
        pygame.sprite.Sprite.__init__(self)
        self.load_images(images)
        self.image = self.i0
        self.imageNum = 0
        self.timeTarget = 7
        self.timeNum = 0
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.left = False
        self.down = False
        self.moving = False
        self.inventory = {}
        self.location = None

    def get_inventory(self):
        '''returns inventory'''
        return self.inventory

    def load_images(self, images):
        '''loads images for later use.
        images: 3 image tuple (standing, step1, step2)'''
        self.i0 = pygame.image.load(images[0]).convert_alpha()
        self.i1 = pygame.image.load(images[1]).convert_alpha()
        self.i2 = pygame.image.load(images[2]).convert_alpha()
        self.images = (self.i0,self.i1,self.i2)

    def update(self, movex, movey, items, walls):
        '''wrapper method.
        movex: number of pixels to move on x axis
        movey: number of pixels to move on y axis
        items: Sprite Group of items with pickUp method
        walls: Sprite Group of walls'''
        self.move_sprite(movex, movey, walls)
        self.items_coll(items)
        self.render()

    def draw(self, Surface):
        '''blits self.image too the Surface.
        Surface: the surface in which self.image will be blitted'''
        Surface.blit(self.image,(self.rect.x,self.rect.y))

    def move_sprite(self, movex, movey, walls):
        '''moves sprite along x and y axis according to movex and movey.
        Also calls movementCheck variable to check for movement and direction.
        movex: number of pixels to move on x axis
        movey: number of pixels to move on y axis
        walls: Sprite Group of walls'''
        oldX = self.rect.x
        oldY = self.rect.y
        self.rect.x += movex
        self.walls_coll_x(walls)
        self.rect.y += movey
        self.walls_coll_y(walls)
        self.move_check(oldX, oldY)

    def move_check(self, oldx, oldy):
        '''checks for differences between oldx and oldy and self.rect.x and self.rect.y.
        oldx: the old x to compare current x too
        oldy: the old y to compare current y too'''
        if self.rect.x == oldx and self.rect.y == oldy:
            self.moving = False
        else:
            self.moving = True
            if self.rect.x > oldx:
                self.left = False
            elif self.rect.x < oldx:
                self.left = True
            if self.rect.y > oldy:
                self.down = True
            elif self.rect.y < oldy:
                self.down = False
    
    def render(self):
        '''sets self.image and calls the chooseImageNum method to choose an image num.'''
        self.choose_imageNum()
        if self.left == True:
            self.image = pygame.transform.flip(self.images[self.imageNum], True, False)
        else:
            self.image = self.images[self.imageNum]

    def choose_imageNum(self):
        '''Chooses which image num will used to render image.'''
        if self.moving == True:
            self.timeNum += 1
            if self.timeNum >= self.timeTarget:
                if self.imageNum == 1:
                    self.imageNum = 2
                else:
                    self.imageNum = 1
                self.timeNum = 0
        else:
            self.imageNum = 0

    def items_coll(self, items):
        '''checks if player collides with items in group
        kills sprites that collide
        items: Sprite Group of items with pickUp method'''
        collisionList = pygame.sprite.spritecollide(self, items, True)
        for collision in collisionList:
            item = collision.pick_up()
            self.update_inventory(item)

    def walls_coll_x(self, walls):
        '''tests for collisions with walls on the x axis
        walls: Sprite Group of walls'''
        collisionList = pygame.sprite.spritecollide(self, walls, False)
        for collision in collisionList:
            if self.left == False:
                self.rect.right = collision.get_left()
            else:
                self.rect.left = collision.get_right()
                
    def walls_coll_y(self, walls):
        '''tests for collisions with walls on the y axis
        walls: Sprite Group of walls'''
        collisionList = pygame.sprite.spritecollide(self, walls, False)
        for collision in collisionList:
            if self.down == True:
                self.rect.bottom = collision.get_top()
            else:
                self.rect.top = collision.get_bottom()

    def update_inventory(self, item):
        '''adds item to inventory
        item: a dictionary of key value pairs that will be added self.inventory'''
        for key in item.keys():
            if key in self.inventory:
                self.inventory[key] += item[key]
            else:
                self.inventory[key] = item[key]
    
    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_width(self):
        return self.rect.w

    def get_height(self):
        return self.rect.h

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def set_rect(self, newx, newy, newwidth, newheight):
        self.oldx = self.rect.x
        self.oldy = self.rect.y
        self.rect.x = newx
        self.rect.y = newy
        self.rect.width = newwidth
        self.rect.height = newheight

    def set_inventory(self, inventory):
        self.inventory = inventory