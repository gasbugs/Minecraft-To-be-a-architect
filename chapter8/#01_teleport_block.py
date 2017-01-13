from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

x = 0
y = 0
z = 0

mc.postToChat("please, should get x,y,z pos of a block")

# 블럭의 x,y,z 좌표를 알아오세요!
while(x==0 and y==0 and z==0):
    blockInf = mc.events.pollBlockHits()
    if len(blockInf) > 0 :
        block = blockInf[0]
        x = block.pos.x
        y = block.pos.y+1
        z = block.pos.z
        break

mc.postToChat("Setted x:%d y:%d z:%d"%(x,y,z))
mc.postToChat("If you on the block, you will go up")

while(True):
    tilePos = mc.player.getTilePos()
    if tilePos.x == x and tilePos.y ==y and tilePos.z == z:
        tilePos.y += 100
        mc.player.setTilePos(tilePos.x, tilePos.y, tilePos.z)
        #break
        mc.postToChat("you're moved up!!!")

mc.postToChat("you're moved up!!!")

## random