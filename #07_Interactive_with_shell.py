from mcpi.minecraft import Minecraft

mc = Minecraft.create()

pos = mc.player.getTilePos()

while(True):
    try :
        blockType = int(input("Block Type(Only Int): "))

        mc.setBlock(pos.x, pos.y, pos.z, blockType)

        mc.postToChat("made the block!" + str(blockType))

    except Exception as e:
        print(e)


