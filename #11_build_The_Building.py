from mcpi.minecraft import Minecraft
import time

AIR                  = 0
STONE                = 1
GRASS                = 2
DIRT                 = 3
COBBLESTONE          = 4
WOOD_PLANKS          = 5
SAPLING              = 6
BEDROCK              = 7
WATER_FLOWING        = 8
WATER                = 8
WATER_STATIONARY     = 9
LAVA_FLOWING         =10
LAVA                 =10
LAVA_STATIONARY      =11
SAND                 =12
GRAVEL               =13
GOLD_ORE             =14
IRON_ORE             =15
COAL_ORE             =16
WOOD                 =17
LEAVES               =18
GLASS                =20
LAPIS_LAZULI_ORE     =21
LAPIS_LAZULI_BLOCK   =22
SANDSTONE            =24
BED                  =26
COBWEB               =30
GRASS_TALL           =31
WOOL                 =35
FLOWER_YELLOW        =37
FLOWER_CYAN          =38
MUSHROOM_BROWN       =39
MUSHROOM_RED         =40
GOLD_BLOCK           =41
IRON_BLOCK           =42
STONE_SLAB_DOUBLE    =43
STONE_SLAB           =44
BRICK_BLOCK          =45
TNT                  =46
BOOKSHELF            =47
MOSS_STONE           =48
OBSIDIAN             =49
TORCH                =50
FIRE                 =51
STAIRS_WOOD          =53
CHEST                =54
DIAMOND_ORE          =56
DIAMOND_BLOCK        =57
CRAFTING_TABLE       =58
FARMLAND             =60
FURNACE_INACTIVE     =61
FURNACE_ACTIVE       =62
DOOR_WOOD            =64
LADDER               =65
STAIRS_COBBLESTONE   =67
DOOR_IRON            =71
REDSTONE_ORE         =73
SNOW                 =78
ICE                  =79
SNOW_BLOCK           =80
CACTUS               =81
CLAY                 =82
SUGAR_CANE           =83
FENCE                =85
GLOWSTONE_BLOCK      =89
BEDROCK_INVISIBLE    =95
STONE_BRICK          =98
GLASS_PANE          =102
MELON               =103
FENCE_GATE          =107
GLOWING_OBSIDIAN    =246
NETHER_REACTOR_CORE =247
PAINTING            =321
STONE_STAIRS         =67
OAK_STAIRS           =53
OAK_STAIRS           =59
NETHERRACK           =87
TRAPDOOR             =96
MELON_SEEDS         =105
BRICK_STAIRS        =108
SANDSTONE_STAIRS    =128
STONE_BRICK_STAIRS  =109
NETHER_BRICK        =112
NETHER_BRICK_STAIRS =114
QUARTZ_BLOCK        =155
QUARTZ_STAIRS       =156
STONE_CUTTER        =245
BONE_MEAL           =351


mc = Minecraft.create()
pos = mc.player.getTilePos()

# 건설 기준점
x = pos.x+1
y = pos.y
z = pos.z

#공간 초기화
mc.setBlocks(x-1,y-1,z-1, x+17+1, y+100, z+28+1, AIR)

## 1층 만들기
#1층 바닥만들기
mc.setBlocks(x,y-1,z, x+14,y-1,z+28, STONE)
mc.setBlocks(x,y-1,z+12,x+17,y-1,z+16, IRON_BLOCK)

#1층 벽만들기
# 측면
mc.setBlocks(x,y,z, x+13, y+5, z, QUARTZ_BLOCK)
mc.setBlocks(x,y,z+12, x+17, y+5, z+12, QUARTZ_BLOCK)
mc.setBlocks(x,y,z+16, x+17, y+5, z+16, QUARTZ_BLOCK)
mc.setBlocks(x,y,z+28, x+13, y+5, z+28, QUARTZ_BLOCK)

# 앞면
mc.setBlocks(x+14,y,z, x+14, y+5, z+11, BRICK_BLOCK)
mc.setBlocks(x+14,y+3,z, x+14, y+3, z+11, QUARTZ_BLOCK)
mc.setBlocks(x+14,y,z+1, x+14, y+4, z+5, AIR)
mc.setBlocks(x+14,y,z+7, x+14, y+4, z+11, AIR)
mc.setBlocks(x+14,y,z+17, x+14, y+5, z+28, BRICK_BLOCK)
mc.setBlocks(x+14,y+3,z+17, x+14, y+3, z+28, QUARTZ_BLOCK)
mc.setBlocks(x+14,y,z+17, x+14, y+4, z+21, AIR)
mc.setBlocks(x+14,y,z+23, x+14, y+4, z+27, AIR)

#뒷면
mc.setBlocks(x,y,z+1, x, y+5, z+28, BRICK_BLOCK)

# 뒷면 유리창
mc.setBlocks(x, y + 3, z + 2, x, y + 3, z + 4, GLASS)
mc.setBlocks(x, y + 3, z + 24, x, y + 3, z + 26, GLASS)
mc.setBlocks(x, y + 3, z + 13, x, y + 3, z + 15, GLASS)

# 입구 만들기
mc.setBlocks(x+17,y,z+13, x+17,y+5,z+15, GLASS)
mc.setBlocks(x+17,y+3,z+13, x+17,y+3,z+15, QUARTZ_BLOCK)
mc.setBlocks(x+17,y,z+14,x+17,y+1,z+14, DOOR_IRON)

#천장 만들기
mc.setBlocks(x,y+5,z, x+14,y+5,z+28, QUARTZ_BLOCK)

# 문 만들기
mc.setBlocks(x+7,y,z+12, x+7, y+1, z+12, DOOR_WOOD)
mc.setBlocks(x+7,y,z+16, x+7, y+1, z+16, DOOR_WOOD)

h=0

# 복층 만들기
for i in range(3): #세 층을 얹음
    time.sleep(1)

    #바닥 만들기
    h = 5*i
    mc.setBlocks(x, y + h + 6, z, x + 17, y + h + 6, z + 28, QUARTZ_BLOCK)
    mc.setBlocks(x, y + h + 6, z, x + 15, y + h + 6, z, BRICK_BLOCK)
    mc.setBlocks(x, y + h + 6, z + 28, x + 15, y + h + 6, z + 28, BRICK_BLOCK)
    mc.setBlocks(x + 1, y + h + 6, z + 1, x + 13, y + h + 6, z + 11, WOOD_PLANKS)
    mc.setBlocks(x + 1, y + h + 6, z + 18, x + 13, y + h + 6, z + 27, WOOD_PLANKS)

    # 옆면 만들기
    mc.setBlocks(x, y + h + 7, z, x + 14, y + h + 10, z, QUARTZ_BLOCK)
    mc.setBlocks(x + 15, y + h + 7, z, x + 17, y + h + 10, z, BRICK_BLOCK)

    mc.setBlocks(x + 1, y + h + 7, z + 11, x + 17, y + h + 10, z + 11, QUARTZ_BLOCK)

    mc.setBlocks(x + 1, y + h + 7, z + 17, x + 17, y + h + 10, z + 17, QUARTZ_BLOCK)

    mc.setBlocks(x, y + h + 7, z + 28, x + 14, y + h + 10, z + 28, QUARTZ_BLOCK)
    mc.setBlocks(x + 15, y + h + 7, z + 28, x + 17, y + h + 10, z + 28, BRICK_BLOCK)

    # 앞면 만들기
    mc.setBlocks(x + 17, y + h + 7, z, x + 17, y + h + 10, z + 28, BRICK_BLOCK)
    mc.setBlocks(x + 17, y + h + 7, z + 12, x + 17, y + h + 10, z + 16, QUARTZ_BLOCK)

    # 뒷면 만들기
    mc.setBlocks(x, y + h + 6, z + 1, x, y + h + 10, z + 27, BRICK_BLOCK)

    # 앞면 유리창
    mc.setBlocks(x + 17, y + h + 8, z + 2, x + 17, y + h + 9, z + 4, GLASS)
    mc.setBlocks(x + 17, y + h + 8, z + 7, x + 17, y + h + 9, z + 9, GLASS)
    mc.setBlocks(x + 17, y + h + 7, z + 13, x + 17, y + h + 10, z + 15, GLASS)
    mc.setBlocks(x + 17, y + h + 8, z + 19, x + 17, y + h + 9, z + 21, GLASS)
    mc.setBlocks(x + 17, y + h + 8, z + 24, x + 17, y + h + 9, z + 26, GLASS)

    # 뒷면 유리창
    mc.setBlocks(x, y + h + 8, z + 2, x, y + h + 9, z + 4, GLASS)
    mc.setBlocks(x, y + h + 8, z + 24, x, y + h + 9, z + 26, GLASS)
    mc.setBlocks(x, y + h + 8, z + 13, x, y + h + 9, z + 15, GLASS)

    # 옆면 유리창
    mc.setBlocks(x + 3, y + h + 8, z, x + 5, y + h + 9, z, GLASS)
    mc.setBlocks(x + 9, y + h + 8, z, x + 11, y + h + 9, z, GLASS)

    mc.setBlocks(x + 3, y + h + 8, z + 28, x + 5, y + h + 9, z + 28, GLASS)
    mc.setBlocks(x + 9, y + h + 8, z + 28, x + 11, y + h + 9, z + 28, GLASS)

    # 문 만들기
    mc.setBlocks(x+7,y + h + 7, z+11 , x+7, y + h + 8 , z+11, DOOR_WOOD)
    mc.setBlocks(x+7,y + h + 7, z+17 , x+7, y + h + 8 , z+17, DOOR_WOOD)

## 지붕 설치

#지붕 바닥
h+=5
mc.setBlocks(x, y + h + 6, z, x + 17, y + h + 6, z + 28, QUARTZ_BLOCK)
mc.setBlocks(x, y + h + 6, z, x + 15, y + h + 6, z, BRICK_BLOCK)
mc.setBlocks(x, y + h + 6, z + 28, x + 15, y + h + 6, z + 28, BRICK_BLOCK)
mc.setBlocks(x + 1, y + h + 6, z + 1, x + 13, y + h + 6, z + 11, WOOD_PLANKS)
mc.setBlocks(x + 1, y + h + 6, z + 18, x + 13, y + h + 6, z + 27, WOOD_PLANKS)

mc.setBlocks(x, y + h + 7, z, x + 17, y + h + 8, z + 28, QUARTZ_BLOCK)
mc.setBlocks(x+1, y + h + 8, z+1, x + 16, y + h + 8, z + 27, AIR)

# 계단 설치
HighstH = mc.getHeight(x, z)
for i in range(HighstH):
    if(mc.getBlock(x+2,i+1,z+14) == 0):
        pass
    else:
        mc.setBlocks(x+2,i+1,z+14 ,x+6,i+1,z+14,AIR)
        for ii in range(10):
            if mc.getBlock(x+2+ii, i+1-ii, z+14) != AIR:
                break
            else:
                mc.setBlock(x+2+ii, i+1-ii, z+14, QUARTZ_BLOCK)

