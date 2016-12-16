from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pos = mc.player.getPos() # 플로트 값 반

x = pos.x
y = pos.y
z = pos.z

witdth = 10 # 너비
height = 5  # 높이
length = 6  # 길이
blockType = 4
air = 0

# 블럭 덩어리 만들기
mc.setBlocks(x,y-1,z, x+witdth,y+height,z+length, blockType)

# 빈 빌딩 만들기
mc.setBlocks(x,y-1,z, x+witdth,y+height,z+length, blockType)
mc.setBlocks(x+1,y,z+1, x+witdth-1,y+height-1,z+length-1, air)