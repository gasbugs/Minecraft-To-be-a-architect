from mcpi.minecraft import Minecraft
import time

x = -25
y = 200
z = 262

mc = Minecraft.create()
mc.player.setTilePos(x,y,z)
speedy = 0.05

for j in range(50):

    for i in range(50):
        mc.setBlock(x, y, z, 103) #수박 블럭(103) 좌표에 만들기
        time.sleep(speedy)
        x+=1

    for i in range(50):
        mc.setBlock(x, y, z, 103)
        time.sleep(speedy)
        y+=1

    for i in range(50):
        mc.setBlock(x, y, z, 103) #수박 블럭(103) 좌표에 만들기
        time.sleep(speedy)
        x-=1

    for i in range(50):
        mc.setBlock(x, y, z, 103)
        time.sleep(speedy)
        y-=1

    z += 20