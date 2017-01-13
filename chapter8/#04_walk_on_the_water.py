from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

mc.postToChat("active walking on the water effect")

water = 9
ice = 79
before = None

while(True):
    pos = mc.player.getTilePos()
    block = mc.getBlock(pos.x, --pos.y,pos.z)
    if water == block:
        mc.setBlock(pos.x,pos.y,pos.z,ice)
        if before and mc.getBlock(before.x, before.y, before.z) == ice:
            mc.setBlock(before.x, before.y , before.z, water)
        before = pos
