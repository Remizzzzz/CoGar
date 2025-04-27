Arm Motion Service
=================

**File**: ``scripts/arm_motion_service.py``  
**Service**: ``/check_joint_state``

Request:
.. code-block:: python

   float64[] positions
   float64[] velocities
   float64[] efforts

Response:
.. code-block:: python

   bool success

Behavior:
1. Validates joint state dimensions
2. Simulates 20% random failure rate
3. 5-second processing delay