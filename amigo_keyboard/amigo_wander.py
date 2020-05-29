#!/usr/bin/env python
import roslib
import rospy
import numpy
import time
import rospy
import math

from geometry_msgs.msg import Twist

from sensor_msgs.msg import PointCloud
from sensor_msgs.msg import ChannelFloat32

velocity_publisher = []
distance1 = 0
distance2 = 0
distance3 = 0
distance4 = 0


#callback function calculates the distance of the obstacle from each sensor
def callback(msg):
	#global variables
	global distance1
	global distance2
	global distance3
	global distance4
    	vel_msg = Twist()
	
	#assign perticular sensor's data to a variable
	data_sense0 = (msg.points[0].x,msg.points[0].y)
	data_sense1 = (msg.points[1].x,msg.points[1].y)
	data_sense2 = (msg.points[2].x,msg.points[2].y)
	data_sense3 = (msg.points[3].x,msg.points[3].y)
	data_sense4 = (msg.points[4].x,msg.points[4].y)
	data_sense5 = (msg.points[5].x,msg.points[5].y)
	data_sense6 = (msg.points[6].x,msg.points[6].y)
	data_sense7 = (msg.points[7].x,msg.points[7].y)

	#calculate distance from x,y values
	distance0 = math.sqrt(math.pow(data_sense0[0],2) + math.pow(data_sense0[1],2))
	distance1 = math.sqrt(math.pow(data_sense1[0],2) + math.pow(data_sense1[1],2))
	distance2 = math.sqrt(math.pow(data_sense2[0],2) + math.pow(data_sense2[1],2))
	distance3 = math.sqrt(math.pow(data_sense3[0],2) + math.pow(data_sense3[1],2))
	distance4 = math.sqrt(math.pow(data_sense4[0],2) + math.pow(data_sense4[1],2))
	distance5 = math.sqrt(math.pow(data_sense5[0],2) + math.pow(data_sense5[1],2))
	distance6 = math.sqrt(math.pow(data_sense6[0],2) + math.pow(data_sense6[1],2))
	distance7 = math.sqrt(math.pow(data_sense7[0],2) + math.pow(data_sense7[1],2))

	print(distance2)
	
	
if __name__ == "__main__":
	try:
		#global variables
		global velocity_publisher
		global distance1
		global distance2
		global distance3
		global distance4

		rospy.init_node('mynode', anonymous=True) 					#make node 	    	
		rospy.Subscriber('/sonar', PointCloud, callback)				#The subscribe() is to receive messages on a given topic. Messages are passed to a callback function
		vel_msg = Twist()
		velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
		while not rospy.is_shutdown():
			if distance2 < 1 or distance3 < 1 or distance1 < 1 or distance4 < 1 :
				#if distance3 < 1:
				vel_msg.angular.z = 0.03
				vel_msg.linear.x = 0
				vel_msg.linear.y = 0
				vel_msg.linear.z = 0
				vel_msg.angular.x = 0
				vel_msg.angular.y = 0	
				print("Turn")
			else:
				vel_msg.linear.x = 0.05
				vel_msg.linear.y = 0
				vel_msg.linear.z = 0
				vel_msg.angular.x = 0
				vel_msg.angular.y = 0
				vel_msg.angular.z = 0
				print("Straight")
				
			for i in range(0,4000):
				velocity_publisher.publish(vel_msg)				#publish velocity data
				#print("publishing")
				rospy.sleep(0.00001)
	    	   	
    	except rospy.ROSInterruptException: pass						#this is an exception if Ctrl+C is pressed


