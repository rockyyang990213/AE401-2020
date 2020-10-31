from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z=mc.player.getTilePos()
weight = 5
height = 5
lenght = 5

mc.setBlocks(x,y,z, x+weight, y+height, z+lenght,213)


# mc.setBlock()