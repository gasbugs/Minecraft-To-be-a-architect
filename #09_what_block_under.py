from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

while(True):
    pos = mc.player.getTilePos()
    blockType = mc.getBlock(pos.x, pos.y-1, pos.z)
    mc.postToChat(blockType)
    time.sleep(1)