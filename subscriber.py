#!/usr/bin/env python

import rospy

from std_msgs.msg import String

def callback(msg)
    print msg.data

    rospy.init_node('subscriber_node')
    sub = rospy.Subscriber('team_Abhiyaan',String,callback)
    rospy.spin()    
