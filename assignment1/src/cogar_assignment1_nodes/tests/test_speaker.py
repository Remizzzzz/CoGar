#!/usr/bin/env python3
import rospy
import unittest
from cogar_assignment1_nodes.srv import Speaker, SpeakerRequest

class TestSpeaker(unittest.TestCase):
    def setUp(self):
        rospy.wait_for_service('/speaker')

    def test_success_rate(self):
        successes = 0
        trials = 10
        speaker_proxy = rospy.ServiceProxy('/speaker', Speaker)
        for _ in range(trials):
            resp = speaker_proxy(SpeakerRequest("Test message"))
            if resp.success:
                successes += 1
        self.assertGreaterEqual(successes / trials, 0.9)  # 90% pass rate

if __name__ == '__main__':
    unittest.main()