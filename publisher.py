#!/usr/bin/env python

import rospy

from std_msgs.msg import String

rospy.init_node('publisher_node')

pub = rospy.Publisher('team_Abhiyaan',String)

rate = rospy.Rate(10)


while not rospy.is_shutdown():
    str = "Team Abhiyaan rocks:"
    pub.publish(str)
    rate.sleep()

