#!/usr/bin/env python3
import rospy
import unittest
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import String, Header
from sensor_msgs.msg import PointField
import numpy as np

class TestSpotFinder(unittest.TestCase):
    def setUp(self):
        rospy.init_node('test_spot_finder')
        self.received_spot = None
        rospy.Subscriber("/rgbd_data", String, self.process_data)
        self.pub = rospy.Publisher("/rgbd_data", PointCloud2, queue_size=10)

    def callback(self, msg):
        self.received_spot = msg.data

    def create_mock_pointcloud(self):
        msg = PointCloud2()
        msg.header = Header(frame_id="camera_depth_frame")
        msg.height = 1
        msg.width = 100  # 100 points
        msg.fields = [
            PointField(name="x", offset=0, datatype=PointField.FLOAT32, count=1),
            PointField(name="y", offset=4, datatype=PointField.FLOAT32, count=1),
            PointField(name="z", offset=8, datatype=PointField.FLOAT32, count=1)
        ]
        msg.is_bigendian = False
        msg.point_step = 12  # 3 floats x 4 bytes
        msg.row_step = msg.point_step * msg.width
        msg.data = np.zeros((msg.width * 3), dtype=np.float32).tobytes()  # Mock data
        msg.is_dense = True
        return msg

    def test_detection_time(self):
        start_time = rospy.Time.now()
        self.pub.publish(self.create_mock_pointcloud())  # Send correct message type
        timeout = rospy.Duration(5.0)
        while not self.received_spot and (rospy.Time.now() - start_time) < timeout:
            rospy.sleep(0.1)
        self.assertLess((rospy.Time.now() - start_time).to_sec(), 2.0)  # <2s

    def tearDown(self):
        rospy.signal_shutdown("Test complete")

if __name__ == '__main__':
    unittest.main()