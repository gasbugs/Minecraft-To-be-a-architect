from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

print("world immutable on")
mc.setting("world_immutable", True)

time.sleep(10)

print("world immutable off")
mc.setting("world_immutable", False)
