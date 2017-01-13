from mcpi.minecraft import Minecraft
import sys
import blocks

mc = Minecraft.create()

mc.postToChat("stair test")

STAIRS_WOOD          =53

xID1 = 0
xID2 = 1
zID1 = 2
zID2 = 3
# 4번 이후로는 거꾸로


while (True):
    mc.postToChat("stair test ID : 0")
    blockInf = mc.events.pollBlockHits()
    if len(blockInf) > 0 :
        block = blockInf[0]
        mc.setBlock(block.pos.x, block.pos.y, block.pos.z, blocks.STAIRS_WOOD, 0)
        break
    blockInf = []

while (True):
    mc.postToChat("stair test ID : 1")
    blockInf = mc.events.pollBlockHits()
    if len(blockInf) > 0 :
        block = blockInf[0]
        mc.setBlock(block.pos.x, block.pos.y, block.pos.z, blocks.STAIRS_WOOD, 1)
        break
    blockInf = []

while (True):
    mc.postToChat("stair test ID : 2")
    blockInf = mc.events.pollBlockHits()
    if len(blockInf) > 0 :
        block = blockInf[0]
        mc.setBlock(block.pos.x, block.pos.y, block.pos.z, blocks.STAIRS_WOOD, 2)
        break
    blockInf = []

while (True):
    mc.postToChat("stair test ID : 3")
    blockInf = mc.events.pollBlockHits()
    if len(blockInf) > 0 :
        block = blockInf[0]
        mc.setBlock(block.pos.x, block.pos.y, block.pos.z, blocks.STAIRS_WOOD, 3)
        break
    blockInf = []

