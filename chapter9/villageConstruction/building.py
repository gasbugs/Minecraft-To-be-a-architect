from mcpi.minecraft import Minecraft
import time
from villageConstruction import blocks

#main
class building:
    def __init__(self):
        self.mc = None
        self.x = 0
        self.y = 0
        self.z = 0
        self.h = 0
        self.floor = 0

    def buildFirstFloor(self):
        # 공간 초기화
        self.mc.setBlocks(self.x - 1, self.y - 1, self.z - 1, self.x + 17 + 1, self.y + 100, self.z + 28 + 1, blocks.AIR)

        ## 1층 만들기
        # 1층 바닥만들기
        self.mc.setBlocks(self.x, self.y - 1, self.z, self.x + 14, self.y - 1, self.z + 28, blocks.STONE)
        self.mc.setBlocks(self.x, self.y - 1, self.z + 12, self.x + 17, self.y - 1, self.z + 16, blocks.IRON_BLOCK)

        # 1층 벽만들기
        # 측면
        self.mc.setBlocks(self.x, self.y, self.z, self.x + 13, self.y + 5, self.z, blocks.QUARTZ_BLOCK)
        self.mc.setBlocks(self.x, self.y, self.z + 12, self.x + 17, self.y + 5, self.z + 12, blocks.QUARTZ_BLOCK)
        self.mc.setBlocks(self.x, self.y, self.z + 16, self.x + 17, self.y + 5, self.z + 16, blocks.QUARTZ_BLOCK)
        self.mc.setBlocks(self.x, self.y, self.z + 28, self.x + 13, self.y + 5, self.z + 28, blocks.QUARTZ_BLOCK)

        # 앞면
        self.mc.setBlocks(self.x + 14, self.y, self.z, self.x + 14, self.y + 5, self.z + 11, blocks.BRICK_BLOCK)
        self.mc.setBlocks(self.x + 14, self.y + 3, self.z, self.x + 14, self.y + 3, self.z + 11, blocks.QUARTZ_BLOCK)
        self.mc.setBlocks(self.x + 14, self.y, self.z + 1, self.x + 14, self.y + 4, self.z + 5, blocks.AIR)
        self.mc.setBlocks(self.x + 14, self.y, self.z + 7, self.x + 14, self.y + 4, self.z + 11, blocks.AIR)
        self.mc.setBlocks(self.x + 14, self.y, self.z + 17, self.x + 14, self.y + 5, self.z + 28, blocks.BRICK_BLOCK)
        self.mc.setBlocks(self.x + 14, self.y + 3, self.z + 17, self.x + 14, self.y + 3, self.z + 28, blocks.QUARTZ_BLOCK)
        self.mc.setBlocks(self.x + 14, self.y, self.z + 17, self.x + 14, self.y + 4, self.z + 21, blocks.AIR)
        self.mc.setBlocks(self.x + 14, self.y, self.z + 23, self.x + 14, self.y + 4, self.z + 27, blocks.AIR)

        # 뒷면
        self.mc.setBlocks(self.x, self.y, self.z + 1, self.x, self.y + 5, self.z + 28, blocks.BRICK_BLOCK)

        # 뒷면 유리창
        self.mc.setBlocks(self.x, self.y + 3, self.z + 2, self.x, self.y + 3, self.z + 4, blocks.GLASS)
        self.mc.setBlocks(self.x, self.y + 3, self.z + 24, self.x, self.y + 3, self.z + 26, blocks.GLASS)
        self.mc.setBlocks(self.x, self.y + 3, self.z + 13, self.x, self.y + 3, self.z + 15, blocks.GLASS)

        # 입구 만들기
        self.mc.setBlocks(self.x + 17, self.y, self.z + 13, self.x + 17, self.y + 5, self.z + 15, blocks.GLASS)
        self.mc.setBlocks(self.x + 17, self.y + 3, self.z + 13, self.x + 17, self.y + 3, self.z + 15, blocks.QUARTZ_BLOCK)
        self.mc.setBlocks(self.x + 17, self.y, self.z + 14, self.x + 17, self.y + 1, self.z + 14, blocks.DOOR_IRON)

        # 천장 만들기
        self.mc.setBlocks(self.x, self.y + 5, self.z, self.x + 14, self.y + 5, self.z + 28, blocks.QUARTZ_BLOCK)

        # 문 만들기
        self.mc.setBlocks(self.x + 7, self.y, self.z + 12, self.x + 7, self.y + 1, self.z + 12, blocks.DOOR_WOOD)
        self.mc.setBlocks(self.x + 7, self.y, self.z + 16, self.x + 7, self.y + 1, self.z + 16, blocks.DOOR_WOOD)

    def buildManyFloor(self):
        print(self.floor)
        # 복층 만들기
        for i in range(self.floor):  # 세 층을 얹음
            time.sleep(1)

            # 바닥 만들기
            self.h = 5 * i
            self.mc.setBlocks(self.x, self.y + self.h + 6, self.z, self.x + 17, self.y + self.h + 6, self.z + 28, blocks.QUARTZ_BLOCK)
            self.mc.setBlocks(self.x, self.y + self.h + 6, self.z, self.x + 15, self.y + self.h + 6, self.z, blocks.BRICK_BLOCK)
            self.mc.setBlocks(self.x, self.y + self.h + 6, self.z + 28, self.x + 15, self.y + self.h + 6, self.z + 28, blocks.BRICK_BLOCK)
            self.mc.setBlocks(self.x + 1, self.y + self.h + 6, self.z + 1, self.x + 13, self.y + self.h + 6, self.z + 11, blocks.WOOD_PLANKS)
            self.mc.setBlocks(self.x + 1, self.y + self.h + 6, self.z + 18, self.x + 13, self.y + self.h + 6, self.z + 27, blocks.WOOD_PLANKS)

            # 옆면 만들기
            self.mc.setBlocks(self.x, self.y + self.h + 7, self.z, self.x + 14, self.y + self.h + 10, self.z, blocks.QUARTZ_BLOCK)
            self.mc.setBlocks(self.x + 15, self.y + self.h + 7, self.z, self.x + 17, self.y + self.h + 10, self.z, blocks.BRICK_BLOCK)

            self.mc.setBlocks(self.x + 1, self.y + self.h + 7, self.z + 11, self.x + 17, self.y + self.h + 10, self.z + 11, blocks.QUARTZ_BLOCK)

            self.mc.setBlocks(self.x + 1, self.y + self.h + 7, self.z + 17, self.x + 17, self.y + self.h + 10, self.z + 17, blocks.QUARTZ_BLOCK)

            self.mc.setBlocks(self.x, self.y + self.h + 7, self.z + 28, self.x + 14, self.y + self.h + 10, self.z + 28, blocks.QUARTZ_BLOCK)
            self.mc.setBlocks(self.x + 15, self.y + self.h + 7, self.z + 28, self.x + 17, self.y + self.h + 10, self.z + 28, blocks.BRICK_BLOCK)

            # 앞면 만들기
            self.mc.setBlocks(self.x + 17, self.y + self.h + 7, self.z, self.x + 17, self.y + self.h + 10, self.z + 28, blocks.BRICK_BLOCK)
            self.mc.setBlocks(self.x + 17, self.y + self.h + 7, self.z + 12, self.x + 17, self.y + self.h + 10, self.z + 16, blocks.QUARTZ_BLOCK)

            time.sleep(1)
            # 뒷면 만들기
            self.mc.setBlocks(self.x, self.y + self.h + 6, self.z + 1, self.x, self.y + self.h + 10, self.z + 27, blocks.BRICK_BLOCK)

            # 앞면 유리창
            self.mc.setBlocks(self.x + 17, self.y + self.h + 8, self.z + 2, self.x + 17, self.y + self.h + 9, self.z + 4, blocks.GLASS)
            self.mc.setBlocks(self.x + 17, self.y + self.h + 8, self.z + 7, self.x + 17, self.y + self.h + 9, self.z + 9, blocks.GLASS)
            self.mc.setBlocks(self.x + 17, self.y + self.h + 7, self.z + 13, self.x + 17, self.y + self.h + 10, self.z + 15, blocks.GLASS)
            self.mc.setBlocks(self.x + 17, self.y + self.h + 8, self.z + 19, self.x + 17, self.y + self.h + 9, self.z + 21, blocks.GLASS)
            self.mc.setBlocks(self.x + 17, self.y + self.h + 8, self.z + 24, self.x + 17, self.y + self.h + 9, self.z + 26, blocks.GLASS)

            # 뒷면 유리창
            self.mc.setBlocks(self.x, self.y + self.h + 8, self.z + 2, self.x, self.y + self.h + 9, self.z + 4, blocks.GLASS)
            self.mc.setBlocks(self.x, self.y + self.h + 8, self.z + 24, self.x, self.y + self.h + 9, self.z + 26, blocks.GLASS)
            self.mc.setBlocks(self.x, self.y + self.h + 8, self.z + 13, self.x, self.y + self.h + 9, self.z + 15, blocks.GLASS)

            # 옆면 유리창
            self.mc.setBlocks(self.x + 3, self.y + self.h + 8, self.z, self.x + 5, self.y + self.h + 9, self.z, blocks.GLASS)
            self.mc.setBlocks(self.x + 9, self.y + self.h + 8, self.z, self.x + 11, self.y + self.h + 9, self.z, blocks.GLASS)

            self.mc.setBlocks(self.x + 3, self.y + self.h + 8, self.z + 28, self.x + 5, self.y + self.h + 9, self.z + 28, blocks.GLASS)
            self.mc.setBlocks(self.x + 9, self.y + self.h + 8, self.z + 28, self.x + 11, self.y + self.h + 9, self.z + 28, blocks.GLASS)

            # 문 만들기
            self.mc.setBlocks(self.x + 7, self.y + self.h + 7, self.z + 11, self.x + 7, self.y + self.h + 8, self.z + 11, blocks.DOOR_WOOD)
            self.mc.setBlocks(self.x + 7, self.y + self.h + 7, self.z + 17, self.x + 7, self.y + self.h + 8, self.z + 17, blocks.DOOR_WOOD)

    def buildLoof(self):
        ## 지붕 설치

        # 지붕 바닥
        time.sleep(1)
        self.h += 5
        self.mc.setBlocks(self.x, self.y + self.h + 6, self.z, self.x + 17, self.y + self.h + 6, self.z + 28, blocks.QUARTZ_BLOCK)
        self.mc.setBlocks(self.x, self.y + self.h + 6, self.z, self.x + 15, self.y + self.h + 6, self.z, blocks.BRICK_BLOCK)
        self.mc.setBlocks(self.x, self.y + self.h + 6, self.z + 28, self.x + 15, self.y + self.h + 6, self.z + 28, blocks.BRICK_BLOCK)
        self.mc.setBlocks(self.x + 1, self.y + self.h + 6, self.z + 1, self.x + 13, self.y + self.h + 6, self.z + 11, blocks.WOOD_PLANKS)
        self.mc.setBlocks(self.x + 1, self.y + self.h + 6, self.z + 18, self.x + 13, self.y + self.h + 6, self.z + 27, blocks.WOOD_PLANKS)

        self.mc.setBlocks(self.x, self.y + self.h + 7, self.z, self.x + 17, self.y + self.h + 8, self.z + 28, blocks.QUARTZ_BLOCK)
        self.mc.setBlocks(self.x + 1, self.y + self.h + 8, self.z + 1, self.x + 16, self.y + self.h + 8, self.z + 27, blocks.AIR)

    def setStairs(self):
            # 계단 설치
            time.sleep(1)
            HighstH = self.mc.getHeight(self.x, self.z)
            for i in range(HighstH):
                if (self.mc.getBlock(self.x + 2, i + 1, self.z + 14) == 0):
                    pass
                else:
                    self.mc.setBlocks(self.x + 2, i + 1, self.z + 14, self.x + 6, i + 1, self.z + 14, blocks.AIR)
                    for ii in range(10):
                        if self.mc.getBlock(self.x + 2 + ii, i + 1 - ii, self.z + 14) != blocks.AIR:
                            break
                        else:
                            self.mc.setBlock(self.x + 2 + ii, i + 1 - ii, self.z + 14, blocks.STAIRS_WOOD, 1)

    def build(self, mc, x, y, z, building):

        self.mc = mc
        self.x = x
        self.y = y
        self.z = z
        self.h = 0
        self.floor = building

        self.buildFirstFloor()
        self.buildManyFloor()
        self.buildLoof()
        self.setStairs()




