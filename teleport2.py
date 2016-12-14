# 마인크래프트에 연결합니다.
import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# x, y, z 변수는 좌표를 나타냅니다.

x = 10
y = 110
z = 12

for i in range(100):
    # 플레이어의 위치를 변경합니다.
    print(str(i+1) + "번째 위치")
    mc.player.setTilePos(x, y, z) # 정수를 변수로 사용
    time.sleep(0.2)
    x += 10
