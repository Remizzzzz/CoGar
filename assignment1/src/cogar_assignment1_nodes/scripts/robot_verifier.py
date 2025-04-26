#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

class RobotVerifier:
    def __init__(self):
        rospy.Subscriber("/robot_heartbeat", String, self.callback)
        self.pub = rospy.Publisher("/robot_status", String, queue_size=10)
    
    def callback(self, msg):
        self.pub.publish(f"{msg.data},status=verified")

if __name__ == "__main__":
    rospy.init_node("robot_verifier")
    RobotVerifier()
    rospy.spin()