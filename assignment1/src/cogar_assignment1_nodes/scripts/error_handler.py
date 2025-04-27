#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

class ErrorHandler:
    def __init__(self):
        rospy.Subscriber("/error_alerts", String, self.handle_error)
        self.staff_pub = rospy.Publisher("/staff_alerts", String, queue_size=10)

    def handle_error(self, error_msg):
        self.staff_pub.publish(f"URGENT: {error_msg.data}")

if __name__ == "__main__":
    rospy.init_node("error_handler")
    ErrorHandler()
    rospy.spin()