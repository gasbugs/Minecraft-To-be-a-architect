from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

while(True):

    position = mc.player.getTilePos()

    x = position.x
    y = position.y
    z = position.z

    time.sleep(0.2)

    for i in range(4):

        mc.setBlock(x, y, z-1, 100)
        y+=1

    position = mc.player.getTilePos()

    x = position.x
    y = position.y
    z = position.z

    time.sleep(0.2)

    for i in range(4):
        mc.setBlock(x, y, z +1, 100)
        y += 1