from mcpi.minecraft import Minecraft
mc = Minecraft.create()

count = 0
x,y,z=mc.player.getTilePos()

while count < 255:
    mc.setBlock(x,  + count, z, 57)

    count = count +1

