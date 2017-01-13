from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

pos = mc.player.getTilePos()

groundY = mc.getHeight(pos.x, pos.z)

mc.postToChat("ground Teleport after 5 sec")
time.sleep(5)

mc.postToChat("Teleport To Ground(%s --> %s)" % (pos.y, groundY))

mc.player.setTilePos(pos.x, groundY, pos.z)
