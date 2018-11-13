from graphics import *

def main():
	winWidth = 1000
	winHeight = 1000
	radius = 100
	
	win  = GraphWin("MyWindow", winWidth, winHeight)
	
	# 0,0,0 = black
	# 255, 255, 255 = white
	win.setBackground(color_rgb(0,0,0))
	
	pt = Point(winWidth/2, winHeight/2)
	circ = Circle(pt,radius)
	circ.setOutline(color_rgb(255,255,255))
	circ.setWidth(3) # width in pixels
	circ.setFill(color_rgb(100,100,100))
	circ.draw(win)
		
	for i in range(1000):
		circ.move(0.5,0.5)
	
	win.getMouse()
	win.close()
	
main()