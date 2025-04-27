Integration Tests
================

Test Scenarios:
1. Full order cycle:
   - Order → Assignment → Delivery → Verification
2. Error handling:
   - Wrong dish → Staff alert
3. Collision avoidance

Launch File:
.. code-block:: xml

   <test pkg="cogar_assignment1_nodes" type="integration_test.py" />