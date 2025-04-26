#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import JointState
from assignments.srv import CheckJointState, CheckJointStateRequest  # Use your package name

class ArmController:
    def __init__(self):
        rospy.Subscriber("/free_spot", String, self.place_dish)
        rospy.wait_for_service('/check_joint_state')
        self.arm_client = rospy.ServiceProxy('/check_joint_state', CheckJointState)

    def place_dish(self, spot_msg):
        try:
            req = CheckJointStateRequest()
            req.positions = [0.0] * 7  # Match TIAGo's 7 joints (adjust values as needed)
            req.velocities = [0.0] * 7
            req.efforts = [0.0] * 7
            resp = self.arm_client(req)
            rospy.loginfo(f"Arm motion {'successful' if resp.success else 'failed'}")
        except rospy.ServiceException as e:
            rospy.logerr(f"Service call failed: {e}")

if __name__ == "__main__":
    rospy.init_node("arm_controller")
    ArmController()
    rospy.spin()