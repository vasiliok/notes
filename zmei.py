# game zmeika for PlotDevice
import random
size(400 ,400)
speed(7)

vectors = {
    KEY_LEFT: [-1,0],
    KEY_RIGHT: [1,0],
    KEY_UP: [0,-1],
    KEY_DOWN: [0,1],
}

def setup(anim):
    anim.width, anim.height = (60,60)
    anim.step = 10
    anim.path = []
    anim.x = 100
    anim.y = 100
    
    anim.direct=KEY_RIGHT
    anim.matrix = [
        [2 if not random.randrange(0,1000) % 90else 0 for i in xrange(anim.width)] for i in xrange(anim.height)
    ]
    anim.matrix[10][10]=1
    anim.matrix[11][10]=1
    anim.matrix[12][10]=1
    # head, tail
    #anim.zmei=[[10,10], [12,10]]
    anim.zmei = [[10,10], [11,10], [12,10],[13,10], [14,10]]
    anim.zmeit = 0


def draw(anim)
    #print anim.zmei
    nofill()
    stroke(0)

    for x in xrange(anim.width):
        for y in xrange(anim.height):
            if anim.matrix[x][y] == 2:
                oval(x*10, y*10, 10, 10)

    zmei_head = anim.zmei[-1]
    if anim.matrix[zmei_head[0]][zmei_head[1]] == 2:
        anim.zmei.append(
            [
                anim.zmei[-1][0] + vectors[anim.direct][0],
                anim.zmei[-1][1] + vectors[anim.direct][1]
            ]
        )
        anim.matrix[zmei_head[0]][zmei_head[1]] = 0
        print "am"
    
    if anim.direct in vectors:
        for i in range(len(anim.zmei)-1):
            anim.zmei[i][0] = anim.zmei[i+1][0]
            anim.zmei[i][1] = anim.zmei[i+1][1]

        
        anim.zmei[-1][0] = anim.zmei[-1][0] + vectors[anim.direct][0]
        anim.zmei[-1][1] = anim.zmei[-1][1] + vectors[anim.direct][1]


    for i in anim.zmei:
        rect(i[0]*10, i[1]*10, 10, 10)

    if keycode in vectors:
        anim.direct = keycode 
    #anim.zmeit = anim.zmeit + 1 if anim.zmeit < len(anim.zmei)-1 else 0

