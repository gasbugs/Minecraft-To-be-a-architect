from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

mc.postToChat("active ice board effect for 1min")

ice = 79

startTime = time.time()
while(True):
    tilePos = mc.player.getTilePos()
    mc.setBlock(tilePos.x, tilePos.y-1, tilePos.z ,ice)
    endTime = time.time()
    if (endTime > startTime + 60):
        break

mc.postToChat("inactive ice board effect")