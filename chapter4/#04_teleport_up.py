from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

mc.postToChat("Teleport up after 10 sec")
time.sleep(5)
mc.postToChat("Teleport up after 5 sec")
time.sleep(5)

tilePos = mc.player.getTilePos()

tilePos.y = tilePos.y + 10

mc.player.setTilePos(tilePos.x, tilePos.y, tilePos.z)

## 앞이나 옆으로 순간이동 시켜봅시다!