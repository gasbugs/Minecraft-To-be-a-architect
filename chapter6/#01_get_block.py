from mcpi.minecraft import Minecraft

mc = Minecraft.create()

while(True):
    blockInf = mc.events.pollBlockHits()
    if len(blockInf) > 0 :
        block = blockInf[0]
        bID = mc.getBlock(block.pos.x,block.pos.y,block.pos.z)
        mc.postToChat("x : %d, y : %d, z : %d"% (block.pos.x,block.pos.y,block.pos.z))
        mc.postToChat("Block ID : " + str(bID))
        mc.postToChat("face : " + str(block.face))
        blockInf = []
