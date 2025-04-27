#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class NavController:
    def __init__(self):
        rospy.Subscriber("/assigned_tasks", String, self.navigate)
        self.cmd_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        self.warning_pub = rospy.Publisher("/collision_warnings", String, queue_size=10)

    def navigate(self, task_msg):
        twist = Twist()
        twist.linear.x = 0.5  # Mock movement
        self.cmd_pub.publish(twist)

if __name__ == "__main__":
    rospy.init_node("nav_controller")
    NavController()
    rospy.spin()