import math
import numpy as np
#Reading input file
data={}
with open("Milestone1\Input\Testcase4.txt") as file:
   for line in file:
      data[line.rstrip().split(':')[0]]=int(line.rstrip().split(':')[1])

print(data)
angle=data['Angle']
diameter=data['WaferDiameter']
radius=(int(diameter/2))
print(radius)
if angle <90 :
  opposite = 180-angle 
elif(angle >=90 and angle<180):
   opposite = angle+180
elif(angle>=180 and angle<270):
   opposite=angle-180
else:
    opposite = angle-180
angle=angle*(math.pi/180)
opposite=opposite*(math.pi/180)
x1=radius*math.sin(angle)
x2=radius*math.sin(opposite)
y1=radius*math.cos(angle)
y2=radius*math.cos(opposite)

print(x1,y1,x2,y2)
points=[[x1,y1],[x2,y2]]
print(points)
n=data['NumberOfPoints']




#Finding equidistanced points
x1=round(x1,4)
y1=round(y1,4)
x2=round(x2,4)
y2=round(y2,4)
result=[]
#result=[(x1,y1)]
"""dx = x2-x1
dy = y2-y1
print(dx,dy)
stepx= dx /(n-2)
stepy=dy/(n-2)
print(stepx,stepy)
px = x1
py=y1
for i in range(0,n-1):
    px=round(px,4)
    py=round(py,4)
    result.append((px,py))
    px += stepx
    py += stepy
#result.append((x2,y2))
print(len(result))
print(result)"""
xx=np.linspace(x1, x2, num=n)
yy=np.linspace(y1, y2, num=n)
for i in range(len(xx)):
   p1=round(xx[i],4)
   p2=round(yy[i],4)
   result.append((p2,p1))
   
print(len(result))
for i in result:
    print(str(i))
#writing in file
with open('output4.txt', 'w') as f:
    for i in result:
        f.write(str(i).replace(' ', ''))
        f.write('\n')