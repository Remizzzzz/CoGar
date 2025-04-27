Unit Tests
=========

Test Files:
- ``test_task_assigner.py``
- ``test_spot_finder.py``
- ``test_speaker_service.py``

Example Test:
.. code-block:: python

   def test_task_assignment():
       pub.publish("Table 5, Sushi")
       result = rospy.wait_for_message("/assigned_tasks", String)
       assert "robot" in result.data