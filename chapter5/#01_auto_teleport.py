from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

mc.postToChat("Start auto Teleport after 10 sec")
time.sleep(5)
mc.postToChat("Start auto Teleport after 5 sec")
time.sleep(5)

tilePos = mc.player.getTilePos()

list1 = [0,1,2,3,4,5,6,7,8,9]
#list1 = range(10)

for i in list1:
    tilePos.y = tilePos.y + 10
    mc.player.setTilePos(tilePos.x, tilePos.y, tilePos.z)
    time.sleep(0.5)

mc.postToChat("Finish auto Teleport")

## 앞이나 옆으로 순간이동 시켜봅시다!