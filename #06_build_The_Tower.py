from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
pos = mc.player.getTilePos()

def build(x1,y2,z3, width, height, length):
    # 빈 빌딩 만들기
    mc.setBlocks(x, y - 1, z, x + width, y + height, z + length, blockType)
    mc.setBlocks(x + 1, y, z + 1, x + width - 1, y + height - 1, z + length - 1, air)

x = pos.x
y = pos.y
z = pos.z

max = 100.0

for i in range(int(max)):
    length = max - i
    mc.setBlocks(x+i ,y+i,z+i, length, 0, length, 4)
    print(i)