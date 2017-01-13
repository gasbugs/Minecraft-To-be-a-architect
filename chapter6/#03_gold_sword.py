from mcpi.minecraft import Minecraft
import sys

mc = Minecraft.create()

mc.postToChat("Active Gold Sword")

gold = 41

while (True):
    blockInf = mc.events.pollBlockHits()
    if len(blockInf) > 0 :
        block = blockInf[0]
        mc.setBlock(block.pos.x, block.pos.y, block.pos.z, gold)
    blockInf = []

