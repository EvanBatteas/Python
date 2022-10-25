import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.animation as anim
from IPython.display import HTML
#make own variabe type Planet/object
class PlanetN(object):
  "A planet"
  def __init__(self,radius,mass,position,velocity,name=""):
    '''
     Initialize a planet with radius, mass, position, velocity, and a name
     position and velocity are arrays for x and y directions

    '''
    self.radius = radius
    self.position = np.array([position[0],position[1]])
    self.velocity = np.array([velocity[0],velocity[1]])
    self.mass = mass
    self.name = name
    self.graph=plt.Circle((self.position[0], self.position[1]),radius=self.radius,zorder=2)
  def draw(self, axes):
        axes.add_artist(self.graph)
  def gravitation(object1, object2, steps, stepsize=1):
    '''
    This method enacts gravitation between two objects, you call it by nameofobject1.gravitation(nameofobject2, numberofsteps,secondsperstep)
    It will return a matplotlib artist animation which can be converted to HTML5 video and play
    It will also plot the position, velocity, acceleration, and overall path taken

    '''
    artlist1 = []
    artlist2 = []
    "method to simulate graviation between two objects, could make it for infintely many objects, and in 2d or 3d"
    "one step is currently one second"   
    #make the figure for the field
    figure, axes = plt.subplots(figsize=(8,8))
    axes.set_aspect(1) #aspect ratio 1:1
    #create the limits of the field which the planets are on
    plt.xlim([-10000,10000])
    plt.ylim([-10000,10000])
    #get mass, radius, and position for object 1 and 2
    m1 = object1.mass
    m2 = object2.mass

    r1 = object1.radius
    r2 = object2.radius

    #creating lists to hold the data of both objects to plot later
    o1data =[[],[],[],[],[],[]]
    o2data =[[],[],[],[],[],[]]
    #1st 2 rows are for position x and y, 2nd 2 are for velocity x and y, 3rd 2 are for acceleration x and y


    #position is a 2x2 matrix, containing the x and y of object 1 in one row, and the x and y of object 2 in the other
    position = np.array([object1.position, object2.position])

    #getting initial velocity, also a 2x2 matrix     
    velocity = np.array([object1.velocity, object2.velocity])
    #G constant
    G=6.67e-11
    #use the distance formula to calculate the distance between the centers of both objects
    distance = ((position[0][0]-position[1][0])**2+(position[0][1]-position[1][1])**2)**.5
    
    #Use formula for gravitational force to find force exerted on and by each object
    
    force = G*((m1*m2)/((distance)**2)) 
    #make each acceleration vector independently for readability
    #position, velociy, and acceleration will all be 2x2 matrixes supported by numpy
    
    #1st index is the object, 2nd is the direction
    # 0 for 1st index is object 1, 1 is object 2
    # 0 for 2nd index is x, 1 is y 
    
    #calculating acceleration and making sure it's pointing the correct direction
    acceleration = np.zeros((2,2))
    distancex = (((position[0][0]-position[1][0])**2)**.5)
    distancey = (((position[0][1]-position[1][1])**2)**.5)
    if(position[1][0]>position[0][0]): 
       acceleration[1][0] = ((force/m2) *distancex*-1)
       acceleration[0][0] = ((force/m1)*distancex)
    if(position[1][1] > position[0][1]):
       acceleration[1][1] = ((force/m2)*distancey*-1)
       acceleration[0][1] = ((force/m1)*distancey)
    if(position[1][0]<position[0][0]): 
       acceleration[1][0] = ((force/m2) *distancex)
       acceleration[0][0] = ((force/m1)*distancex*-1)
    if(position[1][1] < position[0][1]):
       acceleration[1][1] = ((force/m2)*distancey)
       acceleration[0][1] = ((force/m1)*distancey*-1)
    
    
    #stepping function, each step is 1 second by default
    for x in range(steps):
      #Changing the force, and thusly acceleration as the position changes, using same calculations as above
      G=6.67e-11
      distance = ((position[0][0]-position[1][0])**2+(position[0][1]-position[1][1])**2)**.5
      force = G*((m1*m2)/((distance)**2)) #need to fix acceleration and force to go in proper direction
      distancex = (((position[0][0]-position[1][0])**2)**.5)
      distancey = (((position[0][1]-position[1][1])**2)**.5)
      if(position[1][0]>position[0][0]): 
       acceleration[1][0] = ((force/m2) *distancex*-1)
       acceleration[0][0] = ((force/m1)*distancex)
      if(position[1][1] > position[0][1]):
       acceleration[1][1] = ((force/m2)*distancey*-1)
       acceleration[0][1] = ((force/m1)*distancey)
      if(position[1][0]<position[0][0]): 
       acceleration[1][0] = ((force/m2) *distancex)
       acceleration[0][0] = ((force/m1)*distancex*-1)
      if(position[1][1] < position[0][1]):
       acceleration[1][1] = ((force/m2)*distancey)
       acceleration[0][1] = ((force/m1)*distancey*-1)
      #changing velocity and position with the step according to the acceleration which is derived from force
      velocity = velocity + (acceleration *stepsize)
      position = position + (velocity * stepsize)
      o1data[0].append(position[0][0])
      o1data[1].append(position[0][1])
      o1data[2].append(velocity[0][0])
      o1data[3].append(velocity[0][1])
      o1data[4].append(acceleration[0][0])
      o1data[5].append(acceleration[0][1])
      
      o2data[0].append(position[1][0])
      o2data[1].append(position[1][1])
      o2data[2].append(velocity[1][0])
      o2data[3].append(velocity[1][1])
      o2data[4].append(acceleration[1][0])
      o2data[5].append(acceleration[1][1])
      
       # need better implementation of collison, still seems to have a problem, could get points on the circumfrence of each object and do a check if they are interfering

       # could get center of each object, find the angle to it, then take the sin and cos of those angles and add the proper x and y to see if the interfere 
       # position[0][0] - position[1][0] = del x  position[0][1] - position[1][1] = del y    sqrt(dx^2 +dy^2) = hypotenuse tan(dy/dx) = theta angle of hypotenuse
       # the we add sin(theta)*object1.radius to the y pos, and cos(theta)*object1.radius to the x pos, and then do the same with 90-theta for object 2, and then find dx and dy, and see if they are 0 
       # could just check is sqrt(dx^2 +dy^2) = 0 ?? 
       # (position[0][0] + object1.radius - position[1][0]+object2.radius) = dx (position[0][1] + object1.radius - position[1][1] + object2.radius) = dy
      if((((position[1][0]>position[0][0])and((position[0][0]+object1.radius)>(position[1][0]-object2.radius))) or ((position[1][0]<position[0][0])and((position[0][0]+object1.radius)<(position[1][0]-object2.radius)))) 
      and (((position[1][1]>position[0][1])and((position[0][1]+object1.radius)>(position[1][1]-object2.radius))) or ((position[1][1]<position[0][1])and((position[0][1]+object1.radius)<(position[1][1]-object2.radius))))):
        print("the objects collided")
        
        #plotting the final position of the objects
        g1 = plt.Circle((position[0]),r1,zorder=2, color = 'orange')
        g2 = plt.Circle((position[1]),r2,zorder=2, color = 'maroon')
       
        axes.add_artist(g1)
        axes.add_artist(g2)
        artlist1.append([g1,g2])
        
    
        axes.set_axis_off()
        #for x in range(len(artlist1)):
        # animate(figure,[artlist1[x],artlist2[x]])
        #animation = anim.ArtistAnimation(figure, [artlist1, artlist2])
        #animation.to_html5_video()
        plt.show()
        
        # debug print("planet1 :", position[0], " planet2:", position[1], "planet2 accel:", acceleration[1])
        break
      if(x >= steps-1):
        #at the end of however many steps input, plot the final positions of each object
        g1 = plt.Circle((position[0]),r1,zorder=2, color = 'orange')
        g2 = plt.Circle((position[1]),r2,zorder=2, color = 'maroon')
       
        axes.add_artist(g1)
        axes.add_artist(g2)
        artlist1.append([g1,g2])
        
        #animation.to_html5_video()
        
        axes.set_axis_off()
        
        plt.show()
        ran = np.arange(0,steps*stepsize,stepsize)
        o2data = np.array(o2data)
        #plt.plot(ran,o2data[4]*1000000)
        #plt.plot(ran,o2data[0])
        #plt.plot(ran,o2data[2]*1000)
        plt.plot(o2data[0],o2data[1])
        plt.show() 
        plt.plot(o2data[2],o2data[3])
        plt.show() 
        plt.plot(o2data[4],o2data[5])
        plt.show()
        animation = anim.ArtistAnimation(figure, artlist1,interval=10) 
        print(animation)
        return animation
        # debug print("planet1 :", position[0], " planet2:", position[1], "planet2 accel:", acceleration[1])
      else:
        #c1 = sigmoid((p1x)+(p1y)) 
        #c2 = sigmoid((p2x)+(p2y))
        #plotting the path using smaller circles 
        g1 = plt.Circle((position[0]),r1,zorder=2, color='red')
        g2 = plt.Circle((position[1]),r2,zorder=2, color ='blue')
        axes.add_artist(g1)
        axes.add_artist(g2)
        artlist1.append([g1,g2])
        
