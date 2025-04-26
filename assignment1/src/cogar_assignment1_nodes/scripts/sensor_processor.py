#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32, String

class SensorProcessor:
    def __init__(self):
        rospy.Subscriber("/force_sensor", Float32, self.check_force)
        rospy.Subscriber("/arm_joint_state", String, self.check_joints)
        self.stable_pub = rospy.Publisher("/stable_spot", String, queue_size=10)

    def check_force(self, force_msg):
        if force_msg.data > 10.0:  # Threshold in Newtons
            self.stable_pub.publish("stable=True")

if __name__ == "__main__":
    rospy.init_node("sensor_processor")
    SensorProcessor()
    rospy.spin()