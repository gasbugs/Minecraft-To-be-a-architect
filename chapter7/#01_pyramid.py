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

height = 100 # vertical, Horizontal

for i in range(int(height/2)):
    mc.setBlocks(x+i, y-1, z+i, x+height-i, y+i, z+height-i, blocks.SANDSTONE)
    time.sleep(2)
