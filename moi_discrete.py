# Moment of inertia of discrete particles
n = int(input('enter no of particles: '))
ky = 0
kx = 0
mas = 0
c = 0
for i in range (n):
    no = int(i)
    m = float (input('enter mass of particle: '))
    x = float (input('enter x coordinate of particle: '))
    y = float (input('enter y coordinate of particle: '))
    
    kx += (m*x)
    ky += (m*y)
    mas+=m
comx = kx/mas
comy = ky/mas
print ("(", comx, ",", comy, ")")
