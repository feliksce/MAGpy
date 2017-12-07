from math import cos, pi

B, R0, R, t, theta, phi = \
    [0,-1810,0,8,0,-0.56],\
    1,\
    [0.2524,0.2524,0.2524,0.2524,0.2524,0.2524],\
    [0,1.8,0,13.8,0,14],\
    [53.453,53.453,53.453,126.547,126.547,126.547],\
    [-156.884,-36.884,83.116,-143.116,96.884,-23.116]


def B20(B,R0,R,t,theta,phi):
    theta_sz = len(theta)
    result = 0
    for i in range(1, theta_sz):
        result += B[2] * (R0/R[i])**t[2] * 0.5 * (3 * cos(theta[i] * pi/180)**2 - 1)
    return result


r = B20(B,R0,R,t,theta,phi)

print(r)
