#!/usr/bin/env python
import rospy
import math
import numpy as np
from sensor_msgs.msg import JointState 
from std_msgs.msg import Float64MultiArray, Bool
from std_msgs.msg import Bool
from time import time, sleep
import sys
import message_filters

# CORRECT VERSION

# processes the data from the ROSTopic named "joint_states"
class scanAndLook:
    def __init__(self):
        rospy.init_node('scan_look',anonymous=True)

        self.stop = rospy.Rate(1)
        self.intervals = 20
        global sl
        sl = .05
        
        self.statepub = rospy.Publisher('scan_state', Bool, queue_size =10)
        
        self.scan_sub = message_filters.Subscriber("scan_state", Bool)
        self.fire_sub = message_filters.Subscriber("iFire", Bool)
        
        self.sub_list = [self.scan_sub, self.fire_sub]

        # synchronise topics for isFire and jointStates so we have the right joint angles when finding isFire, 
        # slop = delay in sec in messages is syncesd
        self.scan_sync = message_filters.ApproximateTimeSynchronizer(self.sub_list, queue_size=10, slop = sl, allow_headerless=True)
        self.scan_sync.registerCallback(self.fire_callback)
    
    def fire_callback(self,scan,fire): 
        if scan.data == False or fire.data == True:
            self.statepub.publish(False)
    

#loops over the commands at 20Hz until shut down
if __name__ == '__main__': 
    scanner = scanAndLook()
    while not rospy.is_shutdown():
        try:
            rospy.spin()
        except KeyboardInterrupt:
            print("Shutting down")