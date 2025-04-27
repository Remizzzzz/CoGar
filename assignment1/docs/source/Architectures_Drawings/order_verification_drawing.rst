Order Verification System Diagram
---------------------------

.. figure:: /_static/orderVerifBDIAGRAM.drawio.png
   :width: 600
   :align: center
   :alt: Order Verification System Diagram

   UML diagram showing the order verification system's components and their relationships.

Explanation
-----------
    This diagram shows the internal behaviour of the order verification component. This behaviour is activated whenever a robot receive a order challenge from a customer during the service of the table.
    Upon receiving the challenge, the robot will interpret the message and verify with the data of the task assigned to it if the order is wrong. If it doesn't find any issues after 3 verification, it'll
    notify the staff of the issue then continue its task while taking the behaviour adapted to an error case. Once the error is handled, the robot continue its task.