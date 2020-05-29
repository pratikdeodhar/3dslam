#!/usr/bin/env/python
import curses
import rospy
from geometry_msgs.msg import Twist

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()



def talker():
 pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
 rospy.init_node('rover', anonymous=True)
 rate = rospy.Rate(10)
 vel_msg = Twist()
 key = ' '
 linearX = 0
 linearY	= 0
 linearZ = 0
 angularX = 0
 angularY = 0
 angularZ = 0
 while not rospy.is_shutdown():
   
    if (key != ord('q')):
        key = stdscr.getch()
        stdscr.addch(20,25,key)
        stdscr.refresh()
        if key == curses.KEY_UP:
            stdscr.addstr(2,20,"Up")
            linearX += 0.2
        elif key == curses.KEY_DOWN:
            stdscr.addstr(3,20,"Down")
            linearX -= 0.2
        elif key == curses.KEY_LEFT:
            stdscr.addstr(4,20,"Left")
            angularZ += 0.1
        elif key == curses.KEY_RIGHT:
            stdscr.addstr(5,20,"Right")
            angularZ -= 0.1
    elif key == ord('q'):
        curses.endwin()
    vel_msg.linear.x = linearX
    vel_msg.linear.y = linearY
    vel_msg.linear.z = linearZ
    vel_msg.angular.x = angularX
    vel_msg.angular.y = angularY
    vel_msg.angular.z = angularZ
    pub.publish(vel_msg)
    rate.sleep()



# while (key != ord('q')):
#     key = stdscr.getch()
#     stdscr.addch(20,25,key)
#     stdscr.refresh()
#     if key == curses.KEY_UP:
#         stdscr.addstr(2,20,"Up")
#         linearX += 0.1
#     elif key == curses.KEY_DOWN:
#         stdscr.addstr(3,20,"Down")
#         linearX -= 0.1
#     elif key == curses.KEY_LEFT:
#         stdscr.addstr(4,20,"Left")
#         linearY -= 0.1
#     elif key == curses.KEY_LEFT:
#         stdscr.addstr(5,20,"Right")
#         linearY += 0.1
# curses.endwin()

if __name__ == '__main__':
 try:
  talker()
  curses.endwin()
 except rospy.ROSInterruptException:
  pass	
