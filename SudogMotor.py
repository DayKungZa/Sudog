import gpiozero as gg
import time
import pygame

dc1 = gg.Motor(24,23,19,True)
dc2 = gg.Motor(27,17,18,True)
dc3 = gg.Motor(10,9,13,True)
dc4 = gg.Motor(5,6,12,True)
 
def delay(millisec):
    time.sleep(millisec/1000)

def bw(s, t):
    dc1.forward(speed=t)
    dc2.forward(speed=t)
    dc3.forward(speed=s)
    dc4.forward(speed=s)

def fw(s, t):
    dc1.backward(speed=t)
    dc2.backward(speed=t)
    dc3.backward(speed=s)
    dc4.backward(speed=s)

def ls(s, t):
    dc1.backward(speed=t)
    dc2.forward(speed=t)
    dc3.backward(speed=s)
    dc4.forward(speed=s)

def rs(s, t):
    dc1.forward(speed=t)
    dc2.backward(speed=t)
    dc3.forward(speed=s)
    dc4.backward(speed=s)

def st():
    dc1.forward(speed=0)
    dc2.forward(speed=0)
    dc3.forward(speed=0)
    dc4.forward(speed=0)

def init():
    pygame.init()
    win = pygame.display.set_mode((100,100))

def getKey(keyName):
    ans = False
    for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput [myKey]:
        ans = True
    pygame.display.update()
    return ans


def main(sp, sp2):
    if getKey('w'):
        fw(sp/100, sp2/100)
    elif getKey('s'):
        bw(sp/100, sp2/100)
    elif getKey('a'):
        ls(sp/100, sp2/100)
    elif getKey('d'):
        rs(sp/100, sp2/100)
    else:
        st()
    if getKey('UP') and sp<100:
        sp = sp+1
        print("sp =", sp/100)
    elif getKey('DOWN') and sp>0:
        sp = sp-1
        print("sp =", sp/100)
    if getKey('z') and sp2<100:
        sp2 = sp2+1
        print("sp2 =", sp2/100)
    elif getKey('x') and sp2>0:
        sp2 = sp2-1
        print("sp2 =", sp2/100)
    return sp, sp2

if __name__ == '__main__':
    init()
    st()
    sp = 80
    sp2 = 80
    print("WASD to control robot, upp and down key to change speed")
    while True:
        sp, sp2 = main(sp, sp2)
        delay(30)