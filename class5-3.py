from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x, y, z=mc.player.getTilePos()
weight = 50
height = 50
lenght = 50

mc.setBlocks(x,y,z, x+weight, y+height, z+lenght,213)


# mc.setBlock()