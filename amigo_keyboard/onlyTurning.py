#!/usr/bin/env python
import roslib; roslib.load_manifest('rosaria')
import rospy
import math

from sensor_msgs.msg import PointCloud

from geometry_msgs.msg import Twist

linearX = 0
linearY = 0
linearZ = 0
angularX = 0
angularY = 0
angularZ = 0.15
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
    angularZ = 0.15

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
