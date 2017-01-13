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

BRICK_BLOCK          =45

mc.postToChat("build simple house after 5 sec")
time.sleep(5)

for he in range(height):
    for ho in range(Horizontal):
        mc.setBlock(x+ho, y+he, z, BRICK_BLOCK)
    for ve in range(Vertical):
        mc.setBlock(x+Horizontal, y+he, z+ve, BRICK_BLOCK)
    for ho in range(Horizontal):
        mc.setBlock(x+Horizontal-ho, y+he, z+Vertical, BRICK_BLOCK)
    for ve in range(Vertical):
        mc.setBlock(x, y+he, z+Vertical-ve, BRICK_BLOCK)
