from mcpi.minecraft import Minecraft
import sys
import time
import blocks

mc = Minecraft.create()

#xID1 --> normal --> zID1 --> normal --> xID2 --> normal --> zID3 --> normal -->

xID1 = 0
xID2 = 1
zID1 = 2
zID2 = 3
# 4번 이후로는 거꾸로

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


while (True):
    #1
    time.sleep(1)
    for i in range(10):
        if i == 0:
            mc.setBlock(x, y, z, blocks.WOOD_PLANKS)
        elif i == 9:
            mc.setBlock(x, y, z, blocks.STAIRS_WOOD, xID1)
            x += 1
            #y += 1
        else:
            mc.setBlock(x, y, z, blocks.STAIRS_WOOD, xID1)
            x += 1
            y += 1

    #2
    time.sleep(1)
    for i in range(10):
        if i == 0:
            mc.setBlock(x, y, z, blocks.WOOD_PLANKS)
        elif i == 9:
            mc.setBlock(x, y, z, blocks.STAIRS_WOOD, zID1)
            z += 1
            #y += 1
        else:
            mc.setBlock(x, y, z, blocks.STAIRS_WOOD, zID1)
            z += 1
            y += 1

    #3
    time.sleep(1)
    for i in range(10):
        if i == 0:
            mc.setBlock(x, y, z, blocks.WOOD_PLANKS)
        elif i == 9:
            mc.setBlock(x, y, z, blocks.STAIRS_WOOD, xID2)
            x -= 1
            #y += 1
        else:
            mc.setBlock(x, y, z, blocks.STAIRS_WOOD, xID2)
            x -= 1
            y += 1

    #4
    time.sleep(1)
    for i in range(10):
        if i == 0:
            mc.setBlock(x, y, z, blocks.WOOD_PLANKS)
        elif i == 9:
            mc.setBlock(x, y, z, blocks.STAIRS_WOOD, zID2)
            z -= 1
            #y += 1
        else:
            mc.setBlock(x, y, z, blocks.STAIRS_WOOD, zID2)
            z -= 1
            y += 1

    if y > 256:
        break


mc.postToChat("y limit is 256")
