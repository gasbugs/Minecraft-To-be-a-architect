from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# 문자를 변수로 선언
h = "Hello,"
m = "Minecraft"

mc.postToChat("MCPI: " + h, m + "!")
