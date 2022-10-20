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
while(atorigin):
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
  pathx.append(origin[0])
  pathy.append(origin[1])
  pathz.append(origin[2])
  #plt.plot(pathx,pathy) 
  if(origin[0] == 0 and origin[1] == 0 and origin[2] == 0):
    atorigin = False 
  #print(origin) 
fig = plt.figure()
ax = plt.axes(projection='3d')   
ax.plot3D(pathx, pathy, pathz, 'blue')
#ax.plot3D(0,0,0,'.','red')
