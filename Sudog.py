import gpiozero as gg
import time
import pygame
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
import busio
import RPi.GPIO as gp

dc1 = gg.Motor(24,23,19,True)
dc2 = gg.Motor(27,17,18,True)
dc4 = gg.Motor(5,6,12,True)
dc3 = gg.Motor(10,9,13,True)
pump = gg.Motor(25,7,8,True) #air pump
 
def delay(millisec):
    time.sleep(millisec/1000)

def bw(s):
    dc1.forward(speed=s)
    dc2.forward(speed=s)
    dc3.forward(speed=s)
    dc4.forward(speed=s)

def fw(s):
    dc1.backward(speed=s)
    dc2.backward(speed=s)
    dc3.backward(speed=s)
    dc4.backward(speed=s)

def ls(s):
    dc1.backward(speed=s)
    dc2.forward(speed=s)
    dc3.backward(speed=s)
    dc4.forward(speed=s)

def rs(s):
    dc1.forward(speed=s)
    dc2.backward(speed=s)
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


def main(sp):
    if getKey('w'):
        fw(sp/100)
    elif getKey('s'):
        bw(sp/100)
    elif getKey('a'):
        ls(sp/100)
    elif getKey('d'):
        rs(sp/100)
    else:
        st()
    if getKey('UP') and sp<100:
        sp = sp+1
        print(sp/100)
    elif getKey('DOWN') and sp>0:
        sp = sp-1
        print(sp/100)
    return sp

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 60
actuation_ran = 180
min_pul = 200
max_pul = 2500
init_angle = [90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]

def setup_servo(ch):
    ch = int(ch)
    servoch = servo.Servo(
        pca.channels[ch], actuation_range=actuation_ran, min_pulse=min_pul, max_pulse=max_pul)
    servoch.angle = init_angle[ch]
    return servoch

def servo_angle(ser, ang):
    ser.angle = ang

if __name__ == '__main__':
    s1 = setup_servo(0)
    s2 = setup_servo(1)
    s3 = setup_servo(2)
    s4 = setup_servo(3)
    s5 = setup_servo(4)
    s6 = setup_servo(5)
    init()
    st()
    p = 0
    sp = 50
    ang1 = 90
    ang2 = 70
    ang3 = 90
    ang4 = 70
    ang5 = 90
    ang6 = 145
    while True:
        sp = main(sp)
        if getKey('RIGHT') and ang1<180:
            ang1 = ang1+1
            print("base", ang1)
        elif getKey('LEFT') and ang1>0:
            ang1 = ang1-1
            print("base", ang1)

        if getKey('1') and ang2<180:
            ang2 = ang2+1
            print("s2", ang2)
        elif getKey('2') and ang2>12:
            ang2 = ang2-1
            print("s2", ang2)

        if getKey('4') and ang3<180:
            ang3 = ang3+1
            print("s3", ang3)
        elif getKey('3') and ang3>0:
            ang3 = ang3-1
            print("s3", ang3)

        if getKey('5') and ang4<180:
            ang4 = ang4+1
            print("s4", ang4)
        elif getKey('6') and ang4>0:
            ang4 = ang4-1
            print("s4", ang4)

        if getKey('7') and ang5<180:
            ang5 = ang5+1
            print("spin", ang5)
        elif getKey('8') and ang5>0:
            ang5 = ang5-1
            print("spin", ang5)

        if getKey('e'): 
            ang6 = 80
            print("open!")
        elif getKey('q'):
            ang6 = 145
            print("catch!")

        if getKey('p'):
            if p==0:
                pump.forward(0.5)
                p=1
                print("pump on")
            else:
                pump.stop()
                p=0
                print("pump off")
            delay(100)

        #key lud
        if getKey('r'):
            ang1 = 90
            ang2 = 70
            ang3 = 90
            ang4 = 70
            ang5 = 90
            print("stretch position")
            delay(50)

        if getKey('t'):
            ang1 = 90
            ang2 = 164
            ang3 = 176
            ang4 = 85
            ang5 = 90
            print("driving position")
            
        if getKey('m'):
            m1 = int(input("manual\nenter motor :"))
            m2 = int(input("enter angle :"))
            if m1==1:
                ang1 = m2
            if m1==2:
                ang2 = m2
            if m1==3:
                ang3 = m2
            if m1==4:
                ang4 = m2
            if m1==5:
                ang5 = m2
            if m1==6:
                ang6 = m2
                
        if getKey('0'):
            ang1 = None
            ang2 = None
            ang3 = None
            ang4 = None
            ang5 = None
            ang6 = None
            print("servo disabled")
                
        if getKey('i'):
            print("----------Info-----------")
            print("motor speed:", sp)
            print("servo1:", ang1)
            print("servo2:", ang2)
            print("servo3:", ang3)
            print("servo4:", ang4)
            print("servo5:", ang5)
            print("servo6:", ang6)
            print("pump:", p)
            delay(100)

        servo_angle(s1, ang1)
        servo_angle(s2, ang2)
        servo_angle(s3, ang3)
        servo_angle(s4, ang4)
        servo_angle(s5, ang5)
        servo_angle(s6, ang6)
        delay(30)
