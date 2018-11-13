import math
from turtle import *
from graphics import *

# Celestial class that holds information for all celestial bodies
class Celestial:
	
	def __init__(self, radius, orbitalRadius, orbitalCentreX, orbitalCentreY, orbitalSpeed, winWidth, winHeight, path, window, outlineWidth, outlineColour, fillColour, pathColour):
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
		
		# Line and fill properties
		self.outlineWidth = outlineWidth
		self.outlineColour = outlineColour
		self.fillColour = fillColour
		self.pathColour = pathColour
		
		# Celestial object
		self.celest = Turtle()
		self.celest.penup()
		self.celest.setpos(self.centreX, self.centreY)
		self.celest.begin_fill()
		#self.celest.shape("circle")
		#self.celest.shapesize(self.radius, self.radius, self.outlineWidth)
		self.celest.circle(self.radius)
		self.celest.color("black")
		self.celest.end_fill()
		
		# Window properties
		self.winWidth = winWidth
		self.winHeight = winHeight
		self.window = window
		
		# To draw orbital path or not
		self.path = path
		
		
		
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
	
	# Sets circle properties and draws the celestial body
	#def drawCelestial(self):
		# Setting cricle outline with RGB values
		#self.circ.setOutline(color_rgb(self.outlineColour[0],self.outlineColour[1],self.outlineColour[2]))
		#self.celest.color((self.outlineColour[0],self.outlineColour[1],self.outlineColour[2]))

		# Setting circle outline width in pixels
		#self.circ.setWidth(self.outlineWidth) # width in pixels

		# Setting circle fill with RGB values
		#self.circ.setFill(color_rgb(self.fillColour[0],self.fillColour[1],self.fillColour[2]))
		#self.celest.fillcolor((self.fillColour[0],self.fillColour[1],self.fillColour[2]))

		# Drawing circle
		#self.circ.draw(self.window)
		
	# Update position of celestial body
	def updatePos(self,orbitalCentreX,orbitalCentreY):
		# Adding to theta
		self.theta = self.theta + 2*math.pi/self.orbitalSpeed
		if self.theta > 2*math.pi:
			self.theta = 0
			
		# Updating orbital centres (eg for moons)
		self.orbitalCentreX = orbitalCentreX
		self.orbitalCentreY = orbitalCentreY
		
		# Calculating new x and y coordinates for celestial body
		newX = self.orbitalCentreX + self.orbitalRadius*math.cos(self.theta)
		newY = self.orbitalCentreY - self.orbitalRadius*math.sin(self.theta)
		
		# Drawing orbital path if required
		#if self.path:
		#	pt = Point(newX,newY)
		#	pt.setFill(color_rgb(self.pathColour[0],self.pathColour[1],self.pathColour[2]))
		#	pt.draw(self.window)
		
		# Calculating dx and dy to new centre
		dx = -(self.centreX - newX)
		dy = (newY - self.centreY)
		
		# Moving celestial body
		#self.circ.move(dx,dy)
		self.celest.setpos(newX, newY)
		
		# Setting centre to new centre
		self.centreX = newX
		self.centreY = newY


def main():
	# Window width and height
	winWidth = 1000
	winHeight = 1000
	
	# Graphics window
	#win  = GraphWin("Planets", winWidth, winHeight, autoflush=False)
	# Setting background colour
	#win.setBackground(color_rgb(0,0,0))
	
	# Creating Turtle Screen, Setting Size and Colour
	win = Screen()
	win.screensize(winWidth, winHeight, "white")
	win.setworldcoordinates(0, 0, winWidth, winHeight)
	
	
	
	
	# Creating and drawing Sun
	sun = Celestial(10, 0, winWidth/2, winHeight/2, 0, winWidth, winHeight, False, win, 3, [255,255,255], [100,100,100], [0,0,0])
	#sun.drawCelestial()
	
	# Creating and drawing Mercury
	mercury = Celestial(1, sun.getRadius() + 80, sun.getCentreX(), sun.getCentreY(), 100, winWidth, winHeight, True, win, 2, [255,255,255], [100,100,100], [255,255,255])
	#mercury.drawCelestial()
	
	# Creating and drawing Venus
	venus = Celestial(2, sun.getRadius() + 160, sun.getCentreX(), sun.getCentreY(), 150, winWidth, winHeight, True, win, 2, [255,255,255], [100,100,100], [255,255,255])
	#venus.drawCelestial()
	
	# Creating and drawing Earth
	earth = Celestial(3, sun.getRadius() + 240, sun.getCentreX(), sun.getCentreY(), 200, winWidth, winHeight, True, win, 2, [255,255,255], [100,100,100], [255,255,255])
	#earth.drawCelestial()
	
	# Creating and drawing The Moon
	moon = Celestial(1, earth.getRadius() + 40, earth.getCentreX(), earth.getCentreY(), 200/12, winWidth, winHeight, False, win, 1, [255,255,255], [100,100,100], [255,255,255])
	#moon.drawCelestial()
	
	# Creating and drawing Mars
	mars = Celestial(2.5, sun.getRadius() + 320, sun.getCentreX(), sun.getCentreY(), 180, winWidth, winHeight, True, win, 2, [255,255,255], [100,100,100], [255,255,255])
	#mars.drawCelestial()
	
	# Creating and drawing Jupiter
	jupiter = Celestial(4, sun.getRadius() + 400, sun.getCentreX(), sun.getCentreY(), 250, winWidth, winHeight, True, win, 2, [255,255,255], [100,100,100], [255,255,255])
	#jupiter.drawCelestial()
	
	
	# Looping and updating positions while the mouse has not been clicked
	#while win.checkMouse()== None:
	while True:
		# Updating celestial bodies
		mercury.updatePos(sun.getCentreX(),sun.getCentreY())
		venus.updatePos(sun.getCentreX(),sun.getCentreY())
		earth.updatePos(sun.getCentreX(),sun.getCentreY())
		moon.updatePos(earth.getCentreX(),earth.getCentreY())
		mars.updatePos(sun.getCentreX(),sun.getCentreY())
		jupiter.updatePos(sun.getCentreX(),sun.getCentreY())
		
		# Updating at 30 frames per second
		#update(60)
	
main()

