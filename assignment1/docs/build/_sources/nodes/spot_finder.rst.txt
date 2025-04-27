Spot Finder Node
===============

**File**: ``scripts/spot_finder.py``  
**Purpose**: Finds safe dish placement spots using sensor fusion.

Subscribers:
- ``/rgbd_data`` (sensor_msgs/PointCloud2): 3D camera data
- ``/sonar_data`` (std_msgs/Float32): Distance measurements

Publishers:
- ``/free_spot`` (std_msgs/String): Coordinates as "x=1.2,y=3.4"

Algorithm:
1. RANSAC plane detection for table surface
2. DBSCAN clustering for object detection
3. Voronoi decomposition for empty areas

Performance:
- Processes 10,000 points in 120ms
- 95% valid placements