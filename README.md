# Sudog the Rescue Robot
This is a project for the competition: MUT RMRC Robo Cup 2022.

Competed on May 24th and June 12th, 2022.

![sudog](https://github.com/user-attachments/assets/138ce4eb-bdcb-4a7a-a90c-965ec0e9f402)

## Overview
Sudog was named after 'sudo', a command line that we struggled with, and 'dog' cause it looks cute, like a dog.

It is a rescue robot capable of advancing rough terrains, picking up objects with arms, and detecting warning signs.
Controlling via 5G wifi and using vision from the camera only, we used Raspberry Pi4 as the main computer, PCA9685 as a servo driver for the arm, and a webcam for the camera.

The competition has many challenges: warning signs detection, objects pick up, and obstacle courses ranging from tight spaces, sharp turns, uneven floors, and going up pipes.

![image](https://github.com/user-attachments/assets/a31983f9-322f-4260-b918-52f8bf859a60)

## Software
I worked on the control program runs on the Raspberry Pi. Pygame is used for getting keyboard inputs. We used WASD as motor movement inputs, 1-8 for the servos, and some shortcut keys to make recalibrating easier like the picture below.

![UI2](https://github.com/user-attachments/assets/a580176d-101c-460f-9a4c-ae4405e82735)

![image](https://github.com/user-attachments/assets/a31983f9-322f-4260-b918-52f8bf859a60)
