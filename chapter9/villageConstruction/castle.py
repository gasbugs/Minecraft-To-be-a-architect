from mcpi.minecraft import Minecraft
import time
from villageConstruction import blocks

class castle:
    def __init__(self):
        self.mc = None
        self.x = 0
        self.y = 0
        self.z = 0
        self.ver = 0
        self.hor = 0

    def init(self):
        self.mc.setBlocks(self.x,            self.y-1,     self.z,
                          self.x + self.ver, self.y+100, self.z + self.hor,
                          blocks.AIR)
        time.sleep(1)

    def buildWaterway(self):
        x = self.x
        y = self.y
        z = self.z
        ver = self.ver
        hor = self.hor
        mc = self.mc

        #1
        mc.setBlocks(x, y-2, z, x+ver, y-5, z+5, blocks.WATER)
        time.sleep(1)

        #2
        mc.setBlocks(x, y-2, z+hor-5, x+ver, y-5, z+hor, blocks.WATER)
        time.sleep(1)

        #3
        mc.setBlocks(x+ver-5, y - 2, z+5, x + ver, y - 5, z + hor-5, blocks.WATER)
        time.sleep(1)

        #4
        mc.setBlocks(x, y - 2, z + 5, x + 5, y - 5, z + hor - 5, blocks.WATER)
        time.sleep(1)

        # 다리 설치
        mc.setBlocks(x, y-1, z + hor/2 -2, x+5, y-1, z + hor/2 +2, blocks.WOOD_PLANKS)
        time.sleep(1)

    def buildRampart(self):
        x = self.x + 5
        y = self.y
        z = self.z + 5
        ver = self.ver - 10
        hor = self.hor - 10
        mc = self.mc

        # 바닥 깔기
        mc.setBlocks(x, y - 1 , z, x+ver, y-1, z+hor, blocks.GRASS)
        time.sleep(1)

        #1
        mc.setBlocks(x, y, z, x+ver, y+3, z+3, blocks.STONE)
        time.sleep(1)

        #2
        mc.setBlocks(x, y, z+hor-3, x+ver, y+3, z+hor, blocks.STONE)
        time.sleep(1)

        #3
        mc.setBlocks(x+ver-3, y, z+3, x + ver, y+3, z + hor-3, blocks.STONE)
        time.sleep(1)

        #4
        mc.setBlocks(x, y, z + 3, x + 3, y+3, z + hor - 3, blocks.STONE)
        time.sleep(1)

        #성벽데코
        mc.setBlocks(x,   y + 4, z,   x+ver,   y + 4, z+hor,   blocks.STONE)
        mc.setBlocks(x+1, y + 4, z+1, x+ver-1, y + 4, z+hor-1, blocks.AIR)
        time.sleep(1)

        # 망루 설치
        mc.setBlocks(x, y + 4, z, x + 3, y + 8, z + 3, blocks.STONE)
        mc.setBlocks(x + 1, y + 8, z + 1, x + 3, y + 8, z + 3, blocks.AIR)
        time.sleep(1)

        # 성문 설치
        mc.setBlocks(x, y + 4, z + hor/2 - 5, x + 3, y + 6, z + hor/2 + 5, blocks.STONE)
        mc.setBlocks(x, y,     z + hor/2 - 2, x + 3, y + 4, z + hor/2 + 2, blocks.AIR)
        time.sleep(1)

    def build(self, mc, x, y, z, ver, hor):
        self.mc = mc
        self.x = x
        self.y = y
        self.z = z
        self.ver = ver
        self.hor = hor

        time.sleep(5)

        self.init()
        self.buildWaterway()
        self.buildRampart()
