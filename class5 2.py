from mcpi.minecraft import Minecraft

mc = Minecraft.create()
user = input("Enter your name")
while True:

    message = input("Enter your message")

    mc.postToChat("<" + user + ">" + message )