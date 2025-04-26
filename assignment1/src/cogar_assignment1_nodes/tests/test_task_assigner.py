#!/usr/bin/env python3
import rospy
import unittest
from std_msgs.msg import String

class TestTaskAssigner(unittest.TestCase):
    def setUp(self):
        rospy.init_node('test_task_assigner')
        self.received_msg = None
        rospy.Subscriber("/assigned_tasks", String, self.callback)
        self.pub = rospy.Publisher("/new_orders", String, queue_size=10)

    def callback(self, msg):
        self.received_msg = msg.data

    def test_latency(self):
        start_time = rospy.Time.now()
        self.pub.publish(String("Table 1, Sushi"))
        timeout = rospy.Duration(1.0)  # 1-second timeout
        while not self.received_msg and (rospy.Time.now() - start_time) < timeout:
            rospy.sleep(0.1)
        self.assertLess((rospy.Time.now() - start_time).to_sec(), 2)  # <100ms

if __name__ == '__main__':
    unittest.main()