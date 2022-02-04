
cidx = 0
H, W = 800, 800
points_x = [(0,W)]
points_y = [(0,H)]

schemas = [['#FFFFFF']*2 + ['#DE1010','#1737CE','#FAE70D','#030200'],
           ['#FFFFFF']*2 + ['#E3D85E','#5ED0E3','#FAA9E9','#FFFFFF']]
colors = schemas[cidx]
looop = 1
ar = 0.02

rects = [(0,W,0,H)]
rects0 = []

def get_area_ratio(x1,x2,y1,y2): 
    w = abs(x1-x2)
    h = abs(y1-y2)    
    return (h*w)/(H*W)


def sample_new_rect(rects,rects0):

    if (random(10)>1) or (len(rects0)<1) :
        idx = int(random(len(rects)))
        x1,x2,y1,y2 = rects.pop(idx)
        if len(rects)>10:
            rects0.append((x1,x2,y1,y2))
    else:
        idx = int(random(len(rects0)))
        x1,x2,y1,y2 = rects0.pop(0)
        
    y1,y2 = sorted([y1,y2])
    x1,x2 = sorted([x1,x2])

    p_idx = int(random(2))
    
    # if random(2) > 0.5:
    if abs(y1-y2)>abs(x1-x2):
        x1_,x2_ = x1,x2
        y1_ = [y1,y2][p_idx]
        y2_ = random(y1,y2)
        if get_area_ratio(x1,x2,y1,y2_)>ar: rects.append((x1,x2,y1,y2_))
        if get_area_ratio(x1,x2,y2,y2_)>ar: rects.append((x1,x2,y2,y2_))
    else:
        y1_,y2_ = y1,y2
        x1_ = [x1,x2][p_idx]
        x2_ = random(x1,x2)
        if get_area_ratio(x1,x2_,y1,y2)>ar: rects.append((x1,x2_,y1,y2))
        if get_area_ratio(x2,x2_,y1,y2)>ar: rects.append((x2,x2_,y1,y2))

    x,y,w,h = x1_,y1_, x2_-x1_, y2_-y1_

    return (x,y,w,h)


def setup():
    size(W, H)
    background(255)
    frameRate(25)
    strokeWeight(6)    
    stroke(10)
    # color_mode('HSB',360,100,100,1)
    # frame_rate(4)
    fill(colors[0])
    rect(0,0,W,H)

framecnt = 0
def draw():
    # background(0)
    global rects,rects0,framecnt
    
    if framecnt%5 == 0:
        (x,y,w,h) = sample_new_rect(rects,rects0)
        
        n = len(colors)
        if (h*w)/(H*W) > 0.05: n = n - 1
        c = colors[ int(random(0,n)) ]
        # strokeWeight(6)
        fill(c)
        rect(x,y,w,h)
        
        print(len(rects),len(rects0))

    framecnt += 1
    saveFrame('./outputs/mondrian/mondrian{}_####.png'.format(cidx))
    
def mouseClicked(): 
    global looop
    if looop == 0:
        looop = 1
        loop()
    else:
        looop = 0
        noLoop()
