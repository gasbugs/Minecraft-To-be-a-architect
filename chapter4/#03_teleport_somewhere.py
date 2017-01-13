from mcpi.minecraft import Minecraft

mc = Minecraft.create()

mc.postToChat("[flt]Teleport somewhere")

# 여러분들의 위치를 구하고 y 좌표(위아래)를 +10을 해주세요!
x = 16.50
y = 63.50
z = 28.50

mc.player.setTilePos(x, y, z)