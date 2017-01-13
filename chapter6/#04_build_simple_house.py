from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

pos = mc.player.getTilePos()

# 건설 기준점
x = pos.x+3
y = pos.y
z = pos.z

height = 5
Horizontal = 5
Vertical = 5

AIR = 0
BRICK_BLOCK =45

mc.postToChat("build simple house after 5 sec")
time.sleep(5)

mc.setBlocks(x,y,z, x+height,y+Horizontal,z+Vertical, BRICK_BLOCK)
mc.setBlocks(x+1,y,z+1, x+height-1,y+Horizontal-1,z+Vertical-1, AIR)

