#!/usr/bin/env python
"""
Name: Rahul Patil
Course Project for ITCS 6185: Robot Motion Planning (Spring 2016)
Rapidly Exploring Random Trees
"""

import sys, random, math, pygame
from pygame.locals import *
from math import sqrt,cos,sin,atan2

#Initialization of constants 
XDIM = 640
YDIM = 480
WINSIZE = [XDIM, YDIM]
EPSILON = 7.0
NUMNODES = 50000
RADIUS=15
RADIUS = 10
fpsClock = pygame.time.Clock()
white = 255, 240, 200
black = 20, 20, 40
red = 255, 0, 0
blue = 0, 255, 0
green = 0, 0, 255
cyan = 0,255,255
pink = 200, 20, 240
def dist(p1,p2):
    return sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))
#Steps from a point to another
def step_from_to(p1,p2):
    if dist(p1,p2) < EPSILON:
        return p2
    else:
        theta = atan2(p2[1]-p1[1],p2[0]-p1[0])
        return p1[0] + EPSILON*cos(theta), p1[1] + EPSILON*sin(theta)

#Defines the parent of the new node depending on the distance of the node from the initial configuration
#thereby helping to rewire the tree
def ParentDefine(nearestnode,newnode,nodes):
 	for p in nodes:
	   if dist([p.x,p.y],[newnode.x,newnode.y]) <RADIUS and p.distance+dist([p.x,p.y],[newnode.x,newnode.y]) < nearestnode.distance+dist([nearestnode.x,nearestnode.y],[newnode.x,newnode.y]):
	      nearestnode = p
        newnode.distance=nearestnode.distance+dist([nearestnode.x,nearestnode.y],[newnode.x,newnode.y])
	newnode.parent=nearestnode
        return newnode,nearestnode

#Rewires the tree so that the distance from the initial configuration to any point on the tree is the shortest.
def reWiring(nodes,newnode,pygame,screen):
	for i in xrange(len(nodes)):
    	   p = nodes[i]
	   if p!=newnode.parent and dist([p.x,p.y],[newnode.x,newnode.y]) <RADIUS and newnode.distance+dist([p.x,p.y],[newnode.x,newnode.y]) < p.distance:
	      pygame.draw.aaline(screen,white,[p.x,p.y],[p.parent.x,p.parent.y])  
	      p.parent = newnode
              p.distance=newnode.distance+dist([p.x,p.y],[newnode.x,newnode.y]) 
              nodes[i]=p  
              pygame.draw.aaline(screen,black,[p.x,p.y],[newnode.x,newnode.y])                    
	return nodes

#Draws the path from the start to goal configurtion
def drawPath(start,goal,nodes,pygame,screen):
	nearestnode = nodes[0]
	for p in nodes:
	   if dist([p.x,p.y],[goal.x,goal.y]) < dist([nearestnode.x,nearestnode.y],[goal.x,goal.y]):
	      nearestnode = p
	while nearestnode!=start:
		pygame.draw.aaline(screen,cyan,[nearestnode.x,nearestnode.y],[nearestnode.parent.x,nearestnode.parent.y])  
		nearestnode=nearestnode.parent



class Node:
    x = 0
    y = 0
    distance=0  
    parent=None
    def __init__(self,xcoord, ycoord):
         self.x = xcoord
         self.y = ycoord
	
def main():
    #initialize and prepare screen
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption('RRT star')
    white = 255, 255, 255
    black = 0, 0, 0
    screen.fill(black)

    nodes = []
    
    nodes.append(Node(XDIM/4.0,YDIM/2.0)) 
    
    
    start=nodes[0]
    init = Node(XDIM/4.0,YDIM/2.0)
    pygame.draw.circle(screen, blue, (int(init.x),int(init.y)) , RADIUS)
    goal=Node(XDIM,YDIM)
    pygame.draw.circle(screen, green, (int(goal.x),int(goal.y)), RADIUS)
    pygame.display.update()
    for i in range(NUMNODES):
	rand = Node(random.random()*XDIM, random.random()*YDIM)
	nearestnode = nodes[0]
        for p in nodes:
	   if dist([p.x,p.y],[rand.x,rand.y]) < dist([nearestnode.x,nearestnode.y],[rand.x,rand.y]):
	      nearestnode = p
        interpolated= step_from_to([nearestnode.x,nearestnode.y],[rand.x,rand.y])
	
	newnode = Node(interpolated[0],interpolated[1])
 	[newnode,nearestnode]=ParentDefine(nearestnode,newnode,nodes);
       
	nodes.append(newnode)
	pygame.draw.aaline(screen,white,[nearestnode.x,nearestnode.y],[newnode.x,newnode.y])
        nodes=reWiring(nodes,newnode,pygame,screen)
        pygame.display.update()
        fpsClock.tick(10000)

        for e in pygame.event.get():
	   if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
	      sys.exit("Bye")
    drawPath(start,goal,nodes,pygame,screen)
    pygame.display.update()
    fpsClock.tick(10000)

if __name__ == '__main__':
    main()
    running = True
    while running:
       for event in pygame.event.get():
	    if event.type == pygame.QUIT:
               running = False


