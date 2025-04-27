Robot Verifier Node
==================

**File**: ``scripts/robot_verifier.py``  
**Purpose**: Monitors robot health and availability.

Subscribers:
- ``/robot_heartbeat`` (std_msgs/String): Raw status updates

Publishers:
- ``/robot_status`` (std_msgs/String): Processed availability data

Data Format:
.. code-block:: json

   {
     "robot_id": "robot1",
     "battery": 75,
     "x": 2.1,
     "y": 3.4,
     "status": "available"
   }