from mcpi.minecraft import Minecraft

mc = Minecraft.create()

block = input("Please enter a block id")
try:
    block = int(block)
    x, y, z = mc.player.getTilePos()
    mc.setBlocks(x, y, z, block )
except:
    print("Please enter a  int")
finally:
    print("exit")