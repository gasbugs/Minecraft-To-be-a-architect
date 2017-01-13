from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

mc = Minecraft.create()
pos = mc.player.getTilePos()

# 건설 기준점
x = pos.x+1
y = pos.y
z = pos.z

TORCH                =50

mc.setBlock(x,y,z, TORCH)