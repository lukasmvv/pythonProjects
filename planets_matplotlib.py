import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation



# Celestial class that holds information for all celestial bodies
class Celestial:
	
	def __init__(self, radius, orbitalRadius, orbitalCentreX, orbitalCentreY, orbitalSpeed, winWidth, winHeight, path, axes, outlineWidth, outlineColour, fillColour, pathColour):
		# Celestial properties
		self.radius = radius
		self.orbitalRadius = orbitalRadius
		self.orbitalCentreX = orbitalCentreX
		self.orbitalCentreY = orbitalCentreY
		self.orbitalSpeed = orbitalSpeed
		self.centreX = orbitalCentreX + orbitalRadius
		self.centreY = orbitalCentreY
		self.theta = 0
		
		# Circle object
		#pt = Point(self.centreX, self.centreY)
		#self.circ = Circle(pt,self.radius)
		self.celestial = plt.Circle((self.centreX, self.centreY), self.radius, fc='r')
		
		# Window properties
		self.winWidth = winWidth
		self.winHeight = winHeight
		self.axes = axes
		
		# To draw orbital path or not
		self.path = path
		
		# Line and fill properties
		self.outlineWidth = outlineWidth
		self.outlineColour = outlineColour
		self.fillColour = fillColour
		self.pathColour = pathColour
		
	# Returns current centre x coordinate
	def getCentreX(self):
		return self.centreX
	
	# Returns current centre y coordinate
	def getCentreY(self):
		return self.centreY
		
	# Returns current radius
	def getRadius(self):
		return self.radius
	
	# Returns current orbital radius
	def getOrbitalRadius(self):
		return self.orbitalRadius

	# Returns current orbital centre x coordinate
	def updateOrbitalCentre(self, newOrbitalCentre):
		self.orbitalCentreX, self.orbitalCentreY = newOrbitalCentre
		
	# Returns current orbital centre y coordinate	
	def updateCentre(self, newCentre):
		self.centreX, self.centreY = newCentre




def init(celestials):
	for planets in celestials:
	planet.setCenter = (500, 500)
	mercury.center = (600, 500)
	ax.add_patch(sun)
	ax.add_patch(mercury)
	
	return []
	

def animationManage(i):
    
	x,y = mercury.center
	xs,ys = sun.center
	
	newX = 500 - 200*np.cos(np.radians(5*i))
	newY = 500 + 200*np.sin(np.radians(5*i))
	mercury.center = newX, newY
	sun.center = xs,ys
	return []





winWidth = 1000
winHeight = 1000

fig = plt.figure()
fig.set_dpi(500)
fig.set_size_inches(10, 10)

ax = plt.axes(xlim=(0, 1000), ylim=(0, 1000))

sun = Celestial(50, 0, winWidth/2, winHeight/2, 0, winWidth, winHeight, False, ax, 3, [255,255,255], [100,100,100], [0,0,0])
mercury = Celestial(10, sun.getRadius() + 80, sun.getCentreX(), sun.getCentreY(), 100, winWidth, winHeight, True, ax, 2, [255,255,255], [100,100,100], [255,255,255])

#sun = plt.Circle((500, 500), 100, fc='r')
#mercury = plt.Circle((600, 500), 50, fc='b')


numFrames = 360
numInterval = 30

anim = animation.FuncAnimation(fig, animationManage,
							   init_func=init,
							   frames=numFrames,
							   interval=numInterval,
							   blit=True,
							   repeat=True)
								   
								   
plt.show()
