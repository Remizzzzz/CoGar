Task Assigner Node
=================

.. automodule:: task_assigner
   :members:
   :undoc-members:
   :show-inheritance:

Node Diagram
------------

.. uml::

   [Task Assigner] --> [Robot Verifier] : /robot_status
   [Task Assigner] --> [Nav Controller] : /assigned_tasks