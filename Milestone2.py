import math
#Reading input file
data={}
with open("Milestone2\Input\Testcase4.txt") as file:
   for line in file:
      data[line.rstrip().split(':')[0]]=line.rstrip().split(':')[1]
print(data)
diameter=int(data['WaferDiameter'])
radius=diameter/2
die_size_x=int(data['DieSize'].split('x')[0])
die_size_y=int(data['DieSize'].split('x')[1])
h,k=list(map(int,data['DieShiftVector'].replace('(','').replace(')','').split(',')))
print(h,k)
p1,p2=list(map(int,data['ReferenceDie'].replace('(','').replace(')','').split(',')))
print(p1,p2)

#referace coordinates LLC of reference
start_x=p1-(die_size_x/2)
start_y=p2-(die_size_y/2)
print(start_x,start_y)
#BFS
total_boxes=(math.ceil(diameter/die_size_x)*math.ceil(diameter/die_size_y))
print(total_boxes)

def condition(x,y):
    flag=0
    if((x>=radius or x<=(-1*radius) )and (y>=radius or y<=(-1*radius))):
        flag+=1
    if((x+die_size_x>=radius or x+die_size_x<=(-1*radius)) and (y>=radius or y<=(-1*radius))):
        flag+=1
    if((x>=radius or x<=(-1*radius)) and (y+die_size_y>radius or y+die_size_y<=(-1*radius))):
        flag+=1
    if((x+die_size_x>=radius or x+die_size_x<=(-1*radius)) and (y+die_size_y>=radius or y+die_size_y<=(-1*radius))):
        flag+=1
    if(flag==4):
        return False
    return True
    
    
def bfs(start_x,start_y):
    queue=[]
    from_reference=[]
    visited=[]
    start_x=start_x
    start_y=start_y
    print(start_x,start_y)
    from_reference.append([0,0])
    queue.append([start_x,start_y])
    res=[(0,0)]
    visited.append((start_x,start_y))
    c=0
    r=[(start_x-h,start_y-k)]
    while(True):
        x,y=queue.pop(0)
        l1,l2=from_reference.pop(0)
        if(condition(x,y)==False):

            break
        if((x+die_size_x,y) not in visited):
            queue.append([x+die_size_x,y])
            from_reference.append([l1+1,l2])
            res.append((l1+1,l2))
            visited.append((x+die_size_x,y))
            r.append((x+die_size_x,y))
        if((x-die_size_x,y) not in visited):
            queue.append([x-die_size_x,y])
            from_reference.append([l1-1,l2])
            res.append((l1-1,l2))
            visited.append((x-die_size_x,y))
            r.append((x-die_size_x,y))
        if((x,y+die_size_y) not in visited):
            queue.append([x,y+die_size_y])
            from_reference.append([l1,l2+1])
            res.append((l1,l2+1))
            r.append((x,y+die_size_y))
            visited.append((x,y+die_size_y))
        if((x,y-die_size_y) not in visited):
            queue.append([x,y-die_size_y])
            from_reference.append([l1,l2-1])
            res.append((l1,l2-1))
            visited.append((x,y-die_size_y))
            r.append((x,y-die_size_y))
        if((x+die_size_x,y+die_size_y) not in visited):
            queue.append([x+die_size_x,y+die_size_y])
            from_reference.append([l1+1,l2+1])
            res.append((l1+1,l2+1))
            visited.append((x+die_size_x,y+die_size_y))
            r.append((x+die_size_x,y+die_size_y))
        if((x+die_size_x,y-die_size_y) not in visited):
            queue.append([x+die_size_x,y-die_size_y])
            from_reference.append([l1+1,l2-1])
            res.append((l1+1,l2-1))
            visited.append((x+die_size_x,y-die_size_y))
            r.append((x+die_size_x,y-die_size_y))
        if((x-die_size_x,y-die_size_y) not in visited):
            queue.append([x-die_size_x,y-die_size_y])
            from_reference.append([l1-1,l2-1])
            res.append((l1-1,l2-1))
            visited.append((x-die_size_x,y-die_size_y))
            r.append((x-die_size_x,y-die_size_y))
        if((x-die_size_x,y+die_size_y) not in visited):
            queue.append([x-die_size_x,y+die_size_y])
            from_reference.append([l1-1,l2+1])
            res.append((l1-1,l2+1))
            visited.append((x-die_size_x,y+die_size_y))
            r.append((x-die_size_x,y+die_size_y))
        c+=1
        #print(queue,from_reference)
    return res,visited

"""def bfs(start_x,start_y):
    queue=[]
    from_reference=[]
    visited=[]
    start_x=start_x
    start_y=start_y
    print(start_x,start_y)
    from_reference.append([0,0])
    queue.append([start_x-h,start_y-k])
    res=[(0,0)]
    visited.append((start_x-h,start_y-k))
    c=0
    while(True):
        x,y=queue.pop(0)
        l1,l2=from_reference.pop(0)
        if(len(visited)>total_boxes):
            break
        if(condition(x,y)==False):
            visited.remove((x,y))
            res.remove((l1,l2))
            break
        if((x+die_size_x-h,y-k) not in visited):
            queue.append([x+die_size_x-h,y-k])
            from_reference.append([l1+1,l2])
            res.append((l1+1,l2))
            visited.append((x+die_size_x-h,y-k))
        if((x-die_size_x-h,y-k) not in visited):
            queue.append([x-die_size_x-h,y-k])
            from_reference.append([l1-1,l2])
            res.append((l1-1,l2))
            visited.append((x-die_size_x-h,y-k))
        if((x-h,y+die_size_y-k) not in visited):
            queue.append([x-h,y+die_size_y-k])
            from_reference.append([l1,l2+1])
            res.append((l1,l2+1))
            visited.append((x-h,y+die_size_y-k))
        if((x-h,y-die_size_y-k) not in visited):
            queue.append([x-h,y-die_size_y-k])
            from_reference.append([l1,l2-1])
            res.append((l1,l2-1))
            visited.append((x-h,y-die_size_y-k))
        if((x+die_size_x-h,y+die_size_y-k) not in visited):
            queue.append([x+die_size_x-h,y+die_size_y-k])
            from_reference.append([l1+1,l2+1])
            res.append((l1+1,l2+1))
            visited.append((x+die_size_x-h,y+die_size_y-k))
        if((x+die_size_x-h,y-die_size_y-k) not in visited):
            queue.append([x+die_size_x-h,y-die_size_y-k])
            from_reference.append([l1+1,l2-1])
            res.append((l1+1,l2-1))
            visited.append((x+die_size_x-h,y-die_size_y-k))
        if((x-die_size_x-h,y-die_size_y-k) not in visited):
            queue.append([x-die_size_x-h,y-die_size_y-k])
            from_reference.append([l1-1,l2-1])
            res.append((l1-1,l2-1))
            visited.append((x-die_size_x-h,y-die_size_y-k))
        if((x-die_size_x-h,y+die_size_y-k) not in visited):
            queue.append([x-die_size_x-h,y+die_size_y-k])
            from_reference.append([l1-1,l2+1])
            res.append((l1-1,l2+1))
            visited.append((x-die_size_x-h,y+die_size_y-k))
        c+=1
        #print(queue,from_reference)
    return res,visited"""


res,visited=bfs(start_x,start_y)
print(len(res))
coordinate=[]
points=[]

"""for i in range(len(visited)):
    if(condition(visited[i][0],visited[i][1])==True):
        points.append(visited[i])
        coordinate.append(res[i])"""

print(len(points))
print(len(visited))
result=[]
for i in range(len(res)):
    s=str(res[i]).replace(' ', '')+":"+str(visited[i]).replace(' ','')
    result.append(s)
#print(result)
#writing in file
with open('milestone2_output4a.txt', 'w') as f:
    for i in result:
        f.write(i)
        f.write('\n')