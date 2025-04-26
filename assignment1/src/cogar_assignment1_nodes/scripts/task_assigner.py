#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

class TaskAssigner:
    def __init__(self):
        rospy.Subscriber("/new_orders", String, self.assign_task)
        rospy.Subscriber("/robot_status", String, self.update_robots)
        self.task_pub = rospy.Publisher("/assigned_tasks", String, queue_size=10)
        self.robots = {}  # {robot_id: [status, x, y, battery]}

    def update_robots(self, msg):
        robot_id, status, x, y, battery = msg.data.split(',')
        self.robots[robot_id] = [status, float(x), float(y), int(battery)]

    def assign_task(self, order):
        best_robot = min(self.robots, key=lambda k: self.robots[k][3])  # Pick highest battery
        self.task_pub.publish(f"{best_robot}:{order.data}")

if __name__ == "__main__":
    rospy.init_node("task_assigner")
    TaskAssigner()
    rospy.spin()