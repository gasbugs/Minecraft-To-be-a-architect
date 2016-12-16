from mcpi.minecraft import Minecraft

mc = Minecraft.create()

pos = mc.player.getTilePos()

groundY = mc.getHeight(pos.x, pos.z)

mc.postToChat("Teleport To Ground(%s --> %s)" % (pos.y, groundY))

mc.player.setTilePos(pos.x, groundY, pos.z)
