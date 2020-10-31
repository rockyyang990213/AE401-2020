from mcpi.minecraft import Minecraft
mc = Minecraft.create()

count=0
while count < 3:
    mc.postToChat("hi")
    count = count + 1