from mcpi.minecraft import Minecraft
from villageConstruction import pos
from villageConstruction import castle


mc = Minecraft.create()

# 블럭의 x,y,z 좌표를 알아오세요!
x, y, z = pos.getPos(mc)

cb = castle.castle()

ver = 50
hor = 50

cb.build(mc, x, y-1, z, ver, hor)

