#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

class VoiceRecognizer:
    def __init__(self):
        rospy.Subscriber("/microphone_data", String, self.process_audio)
        self.text_pub = rospy.Publisher("/voice_text", String, queue_size=10)

    def process_audio(self, audio_msg):
        self.text_pub.publish(f"Recognized: {audio_msg.data}")

if __name__ == "__main__":
    rospy.init_node("voice_recognizer")
    VoiceRecognizer()
    rospy.spin()