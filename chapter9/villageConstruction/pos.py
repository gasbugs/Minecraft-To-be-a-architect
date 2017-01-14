# 블럭의 x,y,z 좌표를 알아오세요!
def getPos(mc):
    x = 0
    y = 0
    z = 0

    mc.postToChat("please, should get x,y,z pos of a block")

    while(x==0 and y==0 and z==0):
        blockInf = mc.events.pollBlockHits()
        if len(blockInf) > 0 :
            block = blockInf[0]
            x = block.pos.x
            y = block.pos.y+1
            z = block.pos.z
            return x, y, z
