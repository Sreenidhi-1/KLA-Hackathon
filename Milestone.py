import math
#Reading input file
data={}
with open("Milestone1\Input\Testcase3.txt") as file:
   for line in file:
      data[line.rstrip().split(':')[0]]=int(line.rstrip().split(':')[1])

print(data)
angle=data['Angle']
diameter=data['WaferDiameter']
radius=data['WaferDiameter']/2
if angle <90 :
  opposite = 270-angle 
else:
  if angle > 0 :
    opposite = angle - 180
  else :
    opposite = angle + 180
x1=radius*math.sin(math.radians(270-angle))
x2=radius*math.sin(math.radians(angle))
y1=radius*math.cos(math.radians(270-angle))
y2=radius*math.cos(math.radians(angle))
points=[[x1,y1],[x2,y2]]
print(points)
n=data['NumberOfPoints']
points_on_line=diameter/n
#equation of line



#Finding equidistanced points
x1=round(x1,4)
y1=round(y1,4)
x2=round(x2,4)
y2=round(y2,4)
result=[(x1,y1)]
dx = x2-x1
dy = y2-y1
print(dx,dy)
stepx= dx /(n-2)
stepy=dy/(n-2)
print(stepx,stepy)
px = x1+stepx
py=y1+stepy
for i in range(0,n-2):
    px=round(px,4)
    py=round(py,4)
    result.append((px,py))
    px += stepx
    py += stepy
result.append((x2,y2))
print(len(result))
print(result)
for i in result:
    print(str(i))
#writing in file
with open('output3.txt', 'w') as f:
    for i in result:
        f.write(str(i).replace(' ', ''))
        f.write('\n')