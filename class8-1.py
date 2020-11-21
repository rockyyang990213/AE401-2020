from mcpi.minecraft import Minecraft
mc = Minecraft.create()

px,py,pz = mc.player.getTilePos()

def plantTree(x,y,z):
    mc.setBlocks(x - 2, y + 4, z - 2, x + 2, y + 8, z + 2, 20)
    mc.setBlocks(x,y,z, x,y+5,z, 431)

for i in range(100):
    for j in range(10):
        for k in range(10):
            plantTree(px + i + k * 8,py+ k * 8, pz + j * 8)