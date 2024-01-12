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
    if((x>radius or x<-radius )and (y>radius or y<-radius)):
        flag+=1
    if((x+die_size_x>radius or x+die_size_x<-radius) and (y>radius or y<-radius)):
        flag+=1
    if((x>radius or x<-radius) and (y+die_size_y>radius or y+die_size_y<-radius)):
        flag+=1
    if((x+die_size_x>radius or x+die_size_x<-radius) and (y+die_size_y>radius or y+die_size_y<-radius)):
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
    while(True):
        x,y=queue.pop(0)
        l1,l2=from_reference.pop(0)
        if(condition(x,y)==False):
            visited.remove((x,y))
            res.remove((l1,l2))
            break
        if((x+die_size_x,y) not in visited):
            queue.append([x+die_size_x,y])
            from_reference.append([l1+1,l2])
            res.append((l1+1,l2))
            visited.append((x+die_size_x,y))
        if((x-die_size_x,y) not in visited):
            queue.append([x-die_size_x,y])
            from_reference.append([l1-1,l2])
            res.append((l1-1,l2))
            visited.append((x-die_size_x,y))
        if((x,y+die_size_y) not in visited):
            queue.append([x,y+die_size_y])
            from_reference.append([l1,l2+1])
            res.append((l1,l2+1))
            visited.append((x,y+die_size_y))
        if((x,y-die_size_y) not in visited):
            queue.append([x,y-die_size_y])
            from_reference.append([l1,l2-1])
            res.append((l1,l2-1))
            visited.append((x,y-die_size_y))
        if((x+die_size_x,y+die_size_y) not in visited):
            queue.append([x+die_size_x,y+die_size_y])
            from_reference.append([l1+1,l2+1])
            res.append((l1+1,l2+1))
            visited.append((x+die_size_x,y+die_size_y))
        if((x+die_size_x,y-die_size_y) not in visited):
            queue.append([x+die_size_x,y-die_size_y])
            from_reference.append([l1+1,l2-1])
            res.append((l1+1,l2-1))
            visited.append((x+die_size_x,y-die_size_y))
        if((x-die_size_x,y-die_size_y) not in visited):
            queue.append([x-die_size_x,y-die_size_y])
            from_reference.append([l1-1,l2-1])
            res.append((l1-1,l2-1))
            visited.append((x-die_size_x,y-die_size_y))
        if((x-die_size_x,y+die_size_y) not in visited):
            queue.append([x-die_size_x,y+die_size_y])
            from_reference.append([l1-1,l2+1])
            res.append((l1-1,l2+1))
            visited.append((x-die_size_x,y+die_size_y))
        c+=1
        #print(queue,from_reference)
    return res,visited



res,visited=bfs(start_x,start_y)
result=[]
for i in range(len(res)):
    s=str(res[i]).replace(' ', '')+":"+str(visited[i]).replace(' ','')
    result.append(s)
print(result)
#writing in file
with open('milestone2_output4.txt', 'w') as f:
    for i in result:
        f.write(i)
        f.write('\n')