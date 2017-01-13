from mcpi.minecraft import Minecraft
import sys
import time
import blocks

mc = Minecraft.create()

mc.postToChat("please, should get x,y,z pos of a block")
x = 0
y = 0
z = 0


# 블럭의 x,y,z 좌표를 알아오세요!
while(x==0 and y==0 and z==0):
    blockInf = mc.events.pollBlockHits()
    if len(blockInf) > 0 :
        block = blockInf[0]
        x = block.pos.x
        y = block.pos.y
        z = block.pos.z
        break

height = 5 # vertical, Horizontal

while (True):
    #1
    time.sleep(1)
    mc.setBlocks(x,y,z, x+height, y+height, z+height, blocks.AIR)
    mc.setBlock(x, y, z+height/2, blocks.TOURCH)
    mc.setBlock(x + height / 2, y, z + height / 2, blocks.TOURCH)
    x += height
    y -= 1


mc.postToChat("y limit is 256")
