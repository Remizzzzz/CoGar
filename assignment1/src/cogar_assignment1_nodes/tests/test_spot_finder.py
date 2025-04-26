#!/usr/bin/env python3
import rospy
import unittest
from std_msgs.msg import String

class TestSpotFinder(unittest.TestCase):
    def setUp(self):
        rospy.init_node('test_spot_finder')
        self.received_spot = None
        rospy.Subscriber("/free_spot", String, self.callback)
        self.pub = rospy.Publisher("/rgbd_data", String, queue_size=10)

    def callback(self, msg):
        self.received_spot = msg.data

    def test_detection_time(self):
        start_time = rospy.Time.now()
        self.pub.publish(String("mock_data"))
        timeout = rospy.Duration(3.0)  # 3-second timeout
        while not self.received_spot and (rospy.Time.now() - start_time) < timeout:
            rospy.sleep(0.1)
        self.assertLess((rospy.Time.now() - start_time).to_sec(), 2.0)  # <2s

if __name__ == '__main__':
    unittest.main()