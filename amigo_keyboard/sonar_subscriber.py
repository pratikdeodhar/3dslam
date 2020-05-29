#!/usr/bin/env python
import roslib; roslib.load_manifest('rosaria')
import rospy
import math

from sensor_msgs.msg import PointCloud

from geometry_msgs.msg import Twist

linearX = 0.1
linearY = 0
linearZ = 0
angularX = 0
angularY = 0
angularZ = 0
# rospy.sleep(1)
def distance(x ,y, z):
    return math.sqrt(math.pow(x,2)+math.pow(y,2)+math.pow(z,2))

# def pcCb(msg):
#     for i in range(0,8):
#         print "Channel numbPointCloud
#         print msg.points[i]PointCloud
def pcCb(msg):
    global linearX
    global linearY
    global linearZ
    global angularX
    global angularY
    global angularZ
#0,0,0,0,0,0,0,0
    #angularZ = 0.4
    d = []
    for i in range (0,8): 
        d.append(distance(msg.points[i].x,msg.points[i].y,msg.points[i].z))
    if (d[2] < 1.0 and d[3] < 1.0): #Front only - turn right
        linearX = 0
        angularZ = 0.2
	if(d[0] < 1.0 and d[5] < 1.0): # front boxed in, go backwards
            linearX = -0.2
        else: 
            angularZ = -0.1
    elif (d[0] < 1.0 and d[1] < 1.0 ): #  left closer - turn right
        linearX = 0
        angularZ = -0.1
    elif (d[1] < 1.0 and d[4] < 1.0 ): # right closer - turn left
        linearX = 0
        angularZ = 0.1
    else:                               # otherwise go forwards
        linearX = 0.2
        angularZ = 0

def talker():
 pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
#  rospy.init_node('rover', anonymous=True)
 rate = rospy.Rate(10)
 vel_msg = Twist()
 
 global linearX
 global linearY
 global linearZ
 global angularX
 global angularY
 global angularZ
 while not rospy.is_shutdown():
  vel_msg.linear.x = linearX
  vel_msg.linear.y = linearY
  vel_msg.linear.z = linearZ
  vel_msg.angular.x = angularX
  vel_msg.angular.y = angularY
  vel_msg.angular.z = angularZ
  pub.publish(vel_msg)
  rate.sleep()

if __name__ == "__main__":
    rospy.init_node('sonarVal', anonymous=True) #make node
    rospy.Subscriber('/sonar',PointCloud,pcCb)
    # rospy.sleep(1)
    try:
     talker()
    except rospy.ROSInterruptException:
     pass	
    rospy.spin()
