import math
#Reading input file
data={}
with open("Milestone2\Input\Testcase1.txt") as file:
   for line in file:
      data[line.rstrip().split(':')[0]]=line.rstrip().split(':')[1]
print(data)
diameter=int(data['WaferDiameter'])
die_size_x=int(data['DieSize'].split('x')[0])
die_size_y=int(data['DieSize'].split('x')[1])
h,k=list(map(int,data['DieShiftVector'].replace('(','').replace(')','').split(',')))
print(h,k)
p1,p2=list(map(int,data['ReferenceDie'].replace('(','').replace(')','').split(',')))
print(p1,p2)

#referace coordinates LLC of reference
start_x=p1-(die_size_x/2)
start_y=p2-(die_size_y/2)

#BFS
total_boxes=(math.ceil(diameter/die_size_x)*math.ceil(diameter/die_size_y))
def bfs(start_x,start_y):
    queue=[]
    from_reference=[]
    visited=[]
    start_x=h-start_x
    start_y=k-start_y
    from_reference.append([0,0])
    queue.append([start_x,start_y])
    visited.append([start_x,start_y])
    while(True):
        x,y=queue.pop(0)
        l1,l2=from_reference.pop(0)
        if(len(visited)==total_boxes):
            break
        if([x+die_size_x,y] not in visited):
            queue.append([x+die_size_x,y])
            from_reference.append([l1+1,l2])
            visited.append([x+die_size_x,y])
        if([x-die_size_x,y] not in visited):
            queue.append([x-die_size_x,y])
            from_reference.append([l1-1,l2])
            visited.append([x-die_size_x,y])
        if([x,y+die_size_y] not in visited):
            queue.append([x,y+die_size_y])
            from_reference.append([l1,l2+1])
            visited.append([x,y+die_size_y])
        if([x,y-die_size_y] not in visited):
            queue.append([x,y-die_size_y])
            from_reference.append([l1,l2-1])
            visited.append([x,y-die_size_y])
        if([x+die_size_x,y+die_size_y] not in visited):
            queue.append([x+die_size_x,y+die_size_y])
            from_reference.append([l1+1,l2+1])
            visited.append([x+die_size_x,y+die_size_y])
        if([x+die_size_x,y-die_size_y] not in visited):
            queue.append([x+die_size_x,y-die_size_y])
            from_reference.append([l1+1,l2-1])
            visited.append([x+die_size_x,y-die_size_y])
        if([x-die_size_x,y-die_size_y] not in visited):
            queue.append([x-die_size_x,y-die_size_y])
            from_reference.append([l1-1,l2-1])
            visited.append([x-die_size_x,y-die_size_y])
        if([x-die_size_x,y+die_size_y] not in visited):
            queue.append([x-die_size_x,y+die_size_y])
            from_reference.append([l1-1,l2+1])
            visited.append([x-die_size_x,y+die_size_y])
    print(visited)

bfs(start_x,start_y)
   
   