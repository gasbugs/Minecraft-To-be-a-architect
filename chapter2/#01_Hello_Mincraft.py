from mcpi.minecraft import Minecraft

mc = Minecraft.create()

# 콘솔에 프린트하기
print("Hello, Python")
# 월드에 프린트하기
mc.postToChat("MCPI: Hello, Minecraft!")