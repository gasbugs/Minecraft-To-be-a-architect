from mcpi.minecraft import Minecraft

mc = Minecraft.create()

tilePos = mc.player.getTilePos()

print("[*] getTilePos 결과")
print(type(tilePos.x))
print("x : ", tilePos.x)
print("y : ", tilePos.y)
print("z : ", tilePos.z)
print("\n")

pos = mc.player.getPos()
print("[*] getPos 결과")
print(type(pos.x))
print("x : ", pos.x)
print("y : ", pos.y)
print("z : ", pos.z)