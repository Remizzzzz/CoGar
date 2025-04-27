Food Placement System Diagram
---------------------------

.. figure:: /_static/FoodPlacementReasoning_BehaviouralDiagram.drawio.png
   :width: 600
   :align: center
   :alt: Food Placement System Diagram

   UML diagram showing the Food placement system's components and their relationships.

Explanation
-----------
   This diagram shows the internal behaviour of the food placement reasoning subsystem.
   The behaviour is awakened when a new message is sourced by the lifelines execution of "Waiter Subsystem" and "Order Verification Subsystem". The "FreeSpotFinder" lifeline is responsible to reason about the free spot when to leave a new dish and communicate with the "Human Subject Recognition and Object Distance Perceiver" to obtain feedbacks in order to feed the "Grasp&Place" lifeline with a free spot position. The "Human Subject Recongnition" loops continuously as long as all the table targets in front of the client are acquired and stops to send to "Objects Distance Perceiver" the objects to measure distances through the "SONAR". "Grasp&Place" is the control motor lifeline, it communicates with "Force Sensors" and "Arm Join State" continuously acquiring data about the force and kinematics feedback in dish grasping transitory until its complete lay on the table. The accomplishement is manifested from the "Speaker" with a message to the "client actor" wishing an enjoiable meal through the speech received from the "Speech Elaborator". The food placement behaviour can be conditioned by the "client actor" in case of interruption due to order rejecting. If the order is accepted, the susbsytem operates until task termination which is notified to "Waiter" and "Order Verification" Subsystem, thus the TIAGo robot can return to serving area and can be reassigned to a new task.
