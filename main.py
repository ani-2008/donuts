import os
import sys
from math import pi,cos,sin
import time


os.system("clear")
A, B = 0,0

R1 = 1
R2 = 2
size = os.get_terminal_size()
screen_width = 80
screen_height = 40

screen_size = screen_width * screen_height
K2 = 200
K1 = screen_width * K2 * 3 / (8 * (R1 + R2))

PI = pi

theta = 0
PHI_SPACING = 0.02
THETA_SPACING = 0.07

chars = ".,-~:;=!*#$@"

while True:
    sys.stdout.write('\x1b[H') 
    output = [' '] * screen_size
    zbuffer = [0] * screen_size
    while theta < 2 * PI:
        
        phi = 0
        while phi < 2 * PI:
            cosA = cos(A)
            sinA = sin(A)
            cosB = cos(B)
            sinB = sin(B)
            cosphi = cos(phi)
            sinphi = sin(phi)
            costheta = cos(theta)
            sintheta = sin(theta)

            circlex = R2 + R1 * costheta
            circley = R1 * sintheta

            x = circlex * (cosB*cosphi + sinA*sinB*sinphi) - R1*cosA*sinB*sintheta
            y = circlex * (cosphi*sinB - cosB*sinA*sinphi) + R1*cosA*cosB*sintheta
            z = K2 + cosA * circlex * sinphi + R1*sinA*sintheta
            ooz = 1 / z
            
            xp = int(screen_width / 2 + K1 * ooz * x)
            yp = int(screen_height / 2 - K1 * ooz * y)
            if 0 <= xp < screen_width and 0 <= yp < screen_height:
                pos = xp + screen_width * yp
                if 0 <= pos <= screen_size:
                    L = cosphi*costheta*sinB - cosA*costheta*sinphi - sinA*sintheta + cosB*(cosA*sintheta - costheta*sinA*sinphi)
                    if ooz > zbuffer[pos]:
                        zbuffer[pos] = ooz
                        l_ind =  max(0, min(len(chars) - 1, int(L * 8)))
                        output[pos] = chars[l_ind if l_ind > 0 else 0]


            phi += PHI_SPACING
        theta += THETA_SPACING
    theta = 0
    for i in range(screen_height):
        sys.stdout.write(''.join(output[i * screen_width:(i + 1) * screen_width]) + '\n')
    sys.stdout.flush()
    time.sleep(0.03)



    A += 0.15
    B += 0.035

