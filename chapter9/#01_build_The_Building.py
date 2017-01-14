from mcpi.minecraft import Minecraft
import time
import blocks

mc = Minecraft.create()

x = 0
y = 0
z = 0

mc.postToChat("please, should get x,y,z pos of a block")

# 블럭의 x,y,z 좌표를 알아오세요!
while(x==0 and y==0 and z==0):
    blockInf = mc.events.pollBlockHits()
    if len(blockInf) > 0 :
        block = blockInf[0]
        x = block.pos.x
        y = block.pos.y+1
        z = block.pos.z
        break

#공간 초기화
mc.setBlocks(x-1,y-1,z-1, x+17+1, y+100, z+28+1, blocks.AIR)

## 1층 만들기
#1층 바닥만들기
mc.setBlocks(x,y-1,z, x+14,y-1,z+28, blocks.STONE)
mc.setBlocks(x,y-1,z+12,x+17,y-1,z+16, blocks.IRON_BLOCK)

#1층 벽만들기
# 측면
mc.setBlocks(x,y,z, x+13, y+5, z, blocks.QUARTZ_BLOCK)
mc.setBlocks(x,y,z+12, x+17, y+5, z+12, blocks.QUARTZ_BLOCK)
mc.setBlocks(x,y,z+16, x+17, y+5, z+16, blocks.QUARTZ_BLOCK)
mc.setBlocks(x,y,z+28, x+13, y+5, z+28, blocks.QUARTZ_BLOCK)

# 앞면
mc.setBlocks(x+14,y,z, x+14, y+5, z+11, blocks.BRICK_BLOCK)
mc.setBlocks(x+14,y+3,z, x+14, y+3, z+11, blocks.QUARTZ_BLOCK)
mc.setBlocks(x+14,y,z+1, x+14, y+4, z+5, blocks.AIR)
mc.setBlocks(x+14,y,z+7, x+14, y+4, z+11, blocks.AIR)
mc.setBlocks(x+14,y,z+17, x+14, y+5, z+28, blocks.BRICK_BLOCK)
mc.setBlocks(x+14,y+3,z+17, x+14, y+3, z+28, blocks.QUARTZ_BLOCK)
mc.setBlocks(x+14,y,z+17, x+14, y+4, z+21, blocks.AIR)
mc.setBlocks(x+14,y,z+23, x+14, y+4, z+27, blocks.AIR)

#뒷면
mc.setBlocks(x,y,z+1, x, y+5, z+28, blocks.BRICK_BLOCK)

# 뒷면 유리창
mc.setBlocks(x, y + 3, z + 2, x, y + 3, z + 4, blocks.GLASS)
mc.setBlocks(x, y + 3, z + 24, x, y + 3, z + 26, blocks.GLASS)
mc.setBlocks(x, y + 3, z + 13, x, y + 3, z + 15, blocks.GLASS)

# 입구 만들기
mc.setBlocks(x+17,y,z+13, x+17,y+5,z+15, blocks.GLASS)
mc.setBlocks(x+17,y+3,z+13, x+17,y+3,z+15, blocks.QUARTZ_BLOCK)
mc.setBlocks(x+17,y,z+14,x+17,y+1,z+14, blocks.DOOR_IRON)

#천장 만들기
mc.setBlocks(x,y+5,z, x+14,y+5,z+28, blocks.QUARTZ_BLOCK)

# 문 만들기
mc.setBlocks(x+7,y,z+12, x+7, y+1, z+12, blocks.DOOR_WOOD)
mc.setBlocks(x+7,y,z+16, x+7, y+1, z+16, blocks.DOOR_WOOD)

h=0

# 복층 만들기
for i in range(20): #세 층을 얹음
    time.sleep(1)

    #바닥 만들기
    h = 5*i
    mc.setBlocks(x, y + h + 6, z, x + 17, y + h + 6, z + 28, blocks.QUARTZ_BLOCK)
    mc.setBlocks(x, y + h + 6, z, x + 15, y + h + 6, z, blocks.BRICK_BLOCK)
    mc.setBlocks(x, y + h + 6, z + 28, x + 15, y + h + 6, z + 28, blocks.BRICK_BLOCK)
    mc.setBlocks(x + 1, y + h + 6, z + 1, x + 13, y + h + 6, z + 11, blocks.WOOD_PLANKS)
    mc.setBlocks(x + 1, y + h + 6, z + 18, x + 13, y + h + 6, z + 27, blocks.WOOD_PLANKS)

    # 옆면 만들기
    mc.setBlocks(x, y + h + 7, z, x + 14, y + h + 10, z, blocks.QUARTZ_BLOCK)
    mc.setBlocks(x + 15, y + h + 7, z, x + 17, y + h + 10, z, blocks.BRICK_BLOCK)

    mc.setBlocks(x + 1, y + h + 7, z + 11, x + 17, y + h + 10, z + 11, blocks.QUARTZ_BLOCK)

    mc.setBlocks(x + 1, y + h + 7, z + 17, x + 17, y + h + 10, z + 17, blocks.QUARTZ_BLOCK)

    mc.setBlocks(x, y + h + 7, z + 28, x + 14, y + h + 10, z + 28, blocks.QUARTZ_BLOCK)
    mc.setBlocks(x + 15, y + h + 7, z + 28, x + 17, y + h + 10, z + 28, blocks.BRICK_BLOCK)

    # 앞면 만들기
    mc.setBlocks(x + 17, y + h + 7, z, x + 17, y + h + 10, z + 28, blocks.BRICK_BLOCK)
    mc.setBlocks(x + 17, y + h + 7, z + 12, x + 17, y + h + 10, z + 16, blocks.QUARTZ_BLOCK)

    time.sleep(1)
    # 뒷면 만들기
    mc.setBlocks(x, y + h + 6, z + 1, x, y + h + 10, z + 27, blocks.BRICK_BLOCK)

    # 앞면 유리창
    mc.setBlocks(x + 17, y + h + 8, z + 2, x + 17, y + h + 9, z + 4, blocks.GLASS)
    mc.setBlocks(x + 17, y + h + 8, z + 7, x + 17, y + h + 9, z + 9, blocks.GLASS)
    mc.setBlocks(x + 17, y + h + 7, z + 13, x + 17, y + h + 10, z + 15, blocks.GLASS)
    mc.setBlocks(x + 17, y + h + 8, z + 19, x + 17, y + h + 9, z + 21, blocks.GLASS)
    mc.setBlocks(x + 17, y + h + 8, z + 24, x + 17, y + h + 9, z + 26, blocks.GLASS)

    # 뒷면 유리창
    mc.setBlocks(x, y + h + 8, z + 2, x, y + h + 9, z + 4, blocks.GLASS)
    mc.setBlocks(x, y + h + 8, z + 24, x, y + h + 9, z + 26, blocks.GLASS)
    mc.setBlocks(x, y + h + 8, z + 13, x, y + h + 9, z + 15, blocks.GLASS)

    # 옆면 유리창
    mc.setBlocks(x + 3, y + h + 8, z, x + 5, y + h + 9, z, blocks.GLASS)
    mc.setBlocks(x + 9, y + h + 8, z, x + 11, y + h + 9, z, blocks.GLASS)

    mc.setBlocks(x + 3, y + h + 8, z + 28, x + 5, y + h + 9, z + 28, blocks.GLASS)
    mc.setBlocks(x + 9, y + h + 8, z + 28, x + 11, y + h + 9, z + 28, blocks.GLASS)

    # 문 만들기
    mc.setBlocks(x+7,y + h + 7, z+11 , x+7, y + h + 8 , z+11, blocks.DOOR_WOOD)
    mc.setBlocks(x+7,y + h + 7, z+17 , x+7, y + h + 8 , z+17, blocks.DOOR_WOOD)

## 지붕 설치

#지붕 바닥
time.sleep(1)
h+=5
mc.setBlocks(x, y + h + 6, z, x + 17, y + h + 6, z + 28, blocks.QUARTZ_BLOCK)
mc.setBlocks(x, y + h + 6, z, x + 15, y + h + 6, z, blocks.BRICK_BLOCK)
mc.setBlocks(x, y + h + 6, z + 28, x + 15, y + h + 6, z + 28, blocks.BRICK_BLOCK)
mc.setBlocks(x + 1, y + h + 6, z + 1, x + 13, y + h + 6, z + 11, blocks.WOOD_PLANKS)
mc.setBlocks(x + 1, y + h + 6, z + 18, x + 13, y + h + 6, z + 27, blocks.WOOD_PLANKS)

mc.setBlocks(x, y + h + 7, z, x + 17, y + h + 8, z + 28, blocks.QUARTZ_BLOCK)
mc.setBlocks(x+1, y + h + 8, z+1, x + 16, y + h + 8, z + 27, blocks.AIR)

# 계단 설치
time.sleep(1)
HighstH = mc.getHeight(x, z)
for i in range(HighstH):
    if(mc.getBlock(x+2,i+1,z+14) == 0):
        pass
    else:
        mc.setBlocks(x+2,i+1,z+14 ,x+6,i+1,z+14,blocks.AIR)
        for ii in range(10):
            if mc.getBlock(x+2+ii, i+1-ii, z+14) != blocks.AIR:
                break
            else:
                mc.setBlock(x+2+ii, i+1-ii, z+14, blocks.QUARTZ_BLOCK)

