#!/usr/bin/env python

import curses
import rospy
from geometry_msgs.msg import Twist

def move():
    	# Starts a new node
    	rospy.init_node('amigo_sim', anonymous=True)			#make node
    	velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    	vel_msg = Twist()

	stdscr = curses.initscr()
	curses.cbreak()
	stdscr.keypad(1)

	stdscr.refresh()
	vel_msg.linear.x = 0
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0
	
	xl = xa = 0

	i = 0.2

	while not rospy.is_shutdown():

		key = ''
		key = stdscr.getch()					#get character
		stdscr.addch(20,25,key)					#display key on terminal
		stdscr.refresh()
		if key == curses.KEY_UP:				#if up arrow pressed
			stdscr.addstr(2, 20, "Up")			
			vel_msg.linear.x = (xl + i)
			xl = vel_msg.linear.x
			xa = vel_msg.angular.z = 0
		elif key == curses.KEY_DOWN:				#if down arrow pressed
			stdscr.addstr(3, 20, "Down")
			vel_msg.linear.x = (xl - i)
			xl = vel_msg.linear.x
			xa = vel_msg.angular.z = 0
		elif key == curses.KEY_RIGHT:				#if right arrow pressed
			stdscr.addstr(4, 20, "Right")
			vel_msg.angular.z = (xa + i)
			xa = vel_msg.angular.z
			xl = vel_msg.linear.x = 0
		elif key == curses.KEY_LEFT:				#if left arrow pressed
			stdscr.addstr(5, 20, "Left")	
			vel_msg.angular.z = (xa - i)
			xa = vel_msg.angular.z
			xl = vel_msg.linear.x = 0

		velocity_publisher.publish(vel_msg)			#publish velocity data

		vel_msg.linear.x = 0
		vel_msg.linear.y = 0
		vel_msg.linear.z = 0
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		vel_msg.angular.z = 0
		


if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass				#this is an exception if Ctrl+C is pressed


