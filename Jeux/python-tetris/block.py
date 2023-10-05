
import pdb

import constants
import pygame
import math
import copy
import sys

class Block(object):
    """
    Class for handling of tetris block
    """    

    def __init__(self,shape,x,y,screen,color,rotate_en):
        """
        Initialize the tetris block class

        Parameters:
            - shape - list of block data. The list contains [X,Y] coordinates of
                      building blocks.
            - x - X coordinate of first tetris shape block
            - y - Y coordinate of first tetris shape block
            - screen  - screen to draw on
            - color - the color of each shape block in RGB notation
            - rotate_en - enable or disable the rotation
        """
        self.shape = []
        for sh in shape:
            bx = sh[0]*constants.BWIDTH + x
            by = sh[1]*constants.BHEIGHT + y
            block = pygame.Rect(bx,by,constants.BWIDTH,constants.BHEIGHT)
            self.shape.append(block)     
        self.rotate_en = rotate_en
        self.x = x
        self.y = y
        self.diffx = 0
        self.diffy = 0
        self.screen = screen
        self.color = color
        self.diff_rotation = 0

    def draw(self):
        """
        Draw the block from shape blocks. Each shape block
        is filled with a color and black border.
        """
        for bl in self.shape:
            pygame.draw.rect(self.screen,self.color,bl)
            pygame.draw.rect(self.screen,constants.BLACK,bl,constants.MESH_WIDTH)
        
    def get_rotated(self,x,y):
        """
        Compute the new coordinates based on the rotation angle.
        
        Parameters:
            - x - the X coordinate to transfer
            - y - the Y coordinate to transfer

        Returns the tuple with new (X,Y) coordinates.
        """

        rads = self.diff_rotation * (math.pi / 180.0)
        newx = x*math.cos(rads) - y*math.sin(rads)
        newy = y*math.cos(rads) + x*math.sin(rads)
        return (newx,newy)        

    def move(self,x,y):
        """
        Move all elements of the block using the given offset.
        
        Parameters:
            - x - movement in the X coordinate
            - y - movement in the Y coordinate 
        """
        self.diffx += x
        self.diffy += y  
        self._update()

    def remove_blocks(self,y):
        """
        Remove blocks on the Y coordinate. All blocks
        above the Y are moved one step down. 

        Parameters:
            - y - Y coordinate to work with.
        """
        new_shape = []
        for shape_i in range(len(self.shape)):
            tmp_shape = self.shape[shape_i]
            if tmp_shape.y < y:
                new_shape.append(tmp_shape)  
                tmp_shape.move_ip(0,constants.BHEIGHT)
            elif tmp_shape.y > y:
                new_shape.append(tmp_shape)
        self.shape = new_shape

    def has_blocks(self):
        """
        Returns true if the block has some shape blocks in the shape list.
        """    
        return True if len(self.shape) > 0 else False

    def rotate(self):
        """
        Setup the rotation value to 90 degrees.
        """

        if self.rotate_en:
            self.diff_rotation = 90
            self._update()

    def _update(self):
        """
        Update the position of all shape boxes.
        """
        for bl in self.shape:

            origX = (bl.x - self.x)/constants.BWIDTH
            origY = (bl.y - self.y)/constants.BHEIGHT
            rx,ry = self.get_rotated(origX,origY)
            newX = rx*constants.BWIDTH  + self.x + self.diffx
            newY = ry*constants.BHEIGHT + self.y + self.diffy
            newPosX = newX - bl.x
            newPosY = newY - bl.y
            bl.move_ip(newPosX,newPosY)

        self.x += self.diffx
        self.y += self.diffy
        self.diffx = 0
        self.diffy = 0
        self.diff_rotation = 0

    def backup(self):
        """
        Backup the current configuration of shape blocks.
        """

        self.shape_copy = copy.deepcopy(self.shape)
        self.x_copy = self.x
        self.y_copy = self.y
        self.rotation_copy = self.diff_rotation     

    def restore(self):
        """
        Restore the previous configuraiton.
        """
        self.shape = self.shape_copy
        self.x = self.x_copy
        self.y = self.y_copy
        self.diff_rotation = self.rotation_copy

    def check_collision(self,rect_list):
        """
        The function checks if the block colides with any other block
        in the shape list. 

        Parameters:
            - rect_list - the function accepts the list of Rect object which
                         are used for the collistion detection. 
        """
        for blk in rect_list:
            collist = blk.collidelistall(self.shape)
            if len(collist):
                return True
        return False

