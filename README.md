# Robot-Motion-Planning

Name: Rahul Patil
Course Project for ITCS 6185: Robot Motion Planning (Spring 2016)
Rapidly Exploring Random Trees

Programming Language used: Python 2.7.6
Compiler version: GCC 4.8.2

Description:
	This program generates a rapidly exploring random tree from the given initial configuration to the goal configuration.
	The tree starts growing from the initial configuration based on a random point generated.
	The tree then extends towards the random configuration with the specified step size EPSILON.
	This extension takes place from the nearest node of the tree from the random configuration.
	When the goal configuration is found, the program traces back the tree from goal configuration to initial configuration.
	While generating the random configuration, collision detection is done to ensure that the points aren't generated inside an obstacle and the tree doesn't enter the obstacle.

Data Structure Design:
	We use an object with two attributes as x and y coordinates.
	We store the various nodes in a list so that we can connect the nodes on finding the path from the initial to goal configuration.

Everything works as described above.
The initial and goal configuration is taken on mouse clicks.
The nodes generated are displayed on the terminal.

For Project Report is located at the following link:
https://sites.google.com/site/rmpcourseproject2016/

The script for rrt is rrt.py and for rrt star is star.py and are run as:
Navigate to the project directory and run.
	$python rrt.py
	$python star.py
