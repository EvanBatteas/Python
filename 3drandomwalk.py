#3d random walk
import random
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
origin = [0,0,0]
pathx=[0]
pathy=[0]
pathz =[0]
chosen = random.randint(1,6)
if(chosen==1):
  origin[0] +=1
elif(chosen==2):
  origin[1] +=1
elif(chosen==3):
  origin[0] -= 1
elif(chosen==4):
  origin[1] -=1
elif(chosen==5):
 origin[2]+=1
elif(chosen==6):
  origin[2]-=1   
else:
  print("Out of Range")
print(origin)
pathx.append(origin[0])
pathy.append(origin[1])
pathz.append(origin[2])  
atorigin = True
multiplier = 1
x=0  
try:
 while(atorigin):
  distance = (origin[0] **2 + origin[1] **2 + origin[2]**2)**.5 - 100 * multiplier #flow acceleration for 3d
  if(distance > 100):
    multiplier = 2 +x
    x+=1
  elif(distance < 100):
    multiplier = 1 
    x = 0
  chosen = random.randint(1,6)
  if(chosen==1):
    origin[0] +=1 *multiplier
  elif(chosen==2):
    origin[1] +=1 *multiplier
  elif(chosen==3):
    origin[0] -= 1 *multiplier
  elif(chosen==4):
    origin[1] -=1 *multiplier
  elif(chosen==5):
   origin[2]+=1 *multiplier
  elif(chosen==6):
    origin[2]-=1 *multiplier
  else:
    print("Out of Range")
  pathx.append(origin[0])
  pathy.append(origin[1])
  pathz.append(origin[2])
  #plt.plot(pathx,pathy) 
  if(origin[0] == 0 and origin[1] == 0 and origin[2] == 0):
    atorigin = False 
except KeyboardInterrupt:
    #if it takes to long i can just interrupt it, and it will still plot, just not returning to origing 
    fig = plt.figure()
    ax = plt.axes(projection='3d')   
    ax.plot3D(pathx, pathy, pathz, 'blue')
    ax.scatter(0, 0, 0, c='red', marker='.', s=10)
fig = plt.figure()
ax = plt.axes(projection='3d')   
ax.plot3D(pathx, pathy, pathz, 'blue')
ax.scatter(0, 0, 0, c='red', marker='.', s=10)
#ax.plot3D(0,0,0,'.','red')
