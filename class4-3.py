from mcpi.minecraft import Minecraft
mc = Minecraft .create()
x,y,z,= mc.player.getTilePos()
weight = 5
height = 7
lenght = 6
mc.setBlocks(x,y,z,x + weight,z +height,z + lenght,20)
mc.setBlocks(x-1,y-1,z-1,x + weight-1,z +height-1,z + lenght-1,0)
mc.player.setPos(x+2,y+2,z+2)