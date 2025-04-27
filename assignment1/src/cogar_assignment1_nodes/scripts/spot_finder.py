#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import String

class SpotFinder:
    def __init__(self):
        rospy.Subscriber("/rgbd_data", PointCloud2, self.process_data)
        rospy.Subscriber("/sonar_data", String, self.check_obstacles)  # Fixed: Method added
        self.spot_pub = rospy.Publisher("/free_spot", String, queue_size=10)

    def process_data(self, point_cloud):
        self.spot_pub.publish("x=0.5,y=0.7")  # Mock coordinates

    def check_obstacles(self, sonar_msg):  # Added this method
        rospy.loginfo(f"Sonar data: {sonar_msg.data}")

if __name__ == "__main__":
    rospy.init_node("spot_finder")
    SpotFinder()
    rospy.spin()