# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:54:57 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.setBlock(x+1,y,z,46)
mc.setBlock(x-1,y,z,46)
mc.setBlock(x,y,z+1,46)
mc.setBlock(x,y,z-1,46)
mc.setBlock(x+1,y,z+1,46)
mc.setBlock(x-1,y,z+1,46)
mc.setBlock(x+1,y,z-1,46)
mc.setBlock(x-1,y,z-1,46)  