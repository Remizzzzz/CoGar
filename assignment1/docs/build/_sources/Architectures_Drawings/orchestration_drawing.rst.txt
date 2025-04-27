Orchestration System Diagram
---------------------------

.. figure:: /_static/OrchestrationSystemBehaviouralDiagram.drawio.png
   :width: 600
   :align: center
   :alt: Orchestration System Diagram

   UML diagram showing the orchestration system components and their relationships.


Explanation
-----------
   
New task process :
==================
   The order verification system is runned continuously during the service of the restaurant. The staff creates new task by entering inputs in the systems (for example : <dish_name>/<table_number>/<time_of_the_order>)
   Once a task's inputs are entered, the system compute them into a interpretable task for robots, then send it to the task manager. Once it receives the task, the task manager assign it a priority (based on <time_of_order> for example)

Task Assigning process :
========================
   At every time, the system check for robot availability. Once one is available, the system assign it the highest priority task on the task list. If the highest priority task location is already occupied by an other task, then it is derank in priority and the 
   system assign the next highest priority task, doing the same verification each time. Once a task is assigned to a robot, the ErrorHandler and the taskManager will listen to the robots event, waiting for an error or an endTaskNotification. If an error is recieved, the errorHandler will
   assign a behaviour to the robot, depending on the error id, and then, depending on the error Id, the errorHandler can notify the staff.
   Once the notifyEndTask token is received, the Task Manager delete the task and actualize task priority.