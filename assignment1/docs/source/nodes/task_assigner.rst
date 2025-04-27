Task Assigner Node
=================

**File**: ``scripts/task_assigner.py``  
**Purpose**: Central task distribution to robots based on availability and location.

Subscribers:
- ``/new_orders`` (std_msgs/String): Receives orders in format "Table X, Dish Y"
- ``/robot_status`` (std_msgs/String): Gets robot status updates

Publishers:
- ``/assigned_tasks`` (std_msgs/String): Sends assignments in format "robotX:Table Y, Dish Z"

Logic Flow:
1. Receives new order
2. Selects robot with:
   - Highest battery (>20%)
   - Closest to target table
3. Publishes assignment

Example Message:
.. code-block:: python

   "robot2:Table 3, Salmon Sushi"