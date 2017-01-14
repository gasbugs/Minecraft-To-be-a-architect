from mcpi.minecraft import Minecraft
from villageConstruction import pos
from villageConstruction import building


mc = Minecraft.create()

# 블럭의 x,y,z 좌표를 알아오세요!
x, y, z = pos.getPos(mc)

bd = building.building()
bd.build(mc, x, y, z, 3)