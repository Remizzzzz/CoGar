#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from cogar_assignment1_nodes.srv import Speaker, SpeakerRequest  # Use your package name

class OrderVerifier:
    def __init__(self):
        rospy.Subscriber("/dish_detected", String, self.announce_dish)
        rospy.wait_for_service('/speaker')
        self.speaker_client = rospy.ServiceProxy('/speaker', Speaker)

    def announce_dish(self, dish_msg):
        try:
            req = SpeakerRequest()
            req.message = f"Delivering {dish_msg.data}!"  # Customize announcement
            resp = self.speaker_client(req)
            if not resp.success:
                rospy.logwarn("Speaker failed. Alerting staff!")
        except rospy.ServiceException as e:
            rospy.logerr(f"Speaker error: {e}")

if __name__ == "__main__":
    rospy.init_node("order_verifier")
    OrderVerifier()
    rospy.spin()