# Autonomous driving software

This project was developed to be able to generate navigation map data, follow , and stop driving using ROS and python.

#### Development environment
> Jetson TX2
> 
> Gilbot's vehicle
> 
> ublox's GPS sensor(c94-m8p)
> 
> depth camera(Intel® RealSense™ Depth Camera D455)
> 
> ![gilbot](https://user-images.githubusercontent.com/60971835/145783801-ea147618-47c3-4921-992f-9b91a93b157c.png)


### GPS Data
---

To obtain reliable GPS data, rtk was used to reduce the margin of error and the data converted to utm coordinate system was used.

The picture below is the navigation map data of Kunsan University created by our team using GPS data.

![교내 항법지도 데이터](https://user-images.githubusercontent.com/60971835/145800246-aa256f5d-a76e-40bd-8369-500ee5d49b5f.png)

reference
+ https://github.com/bao-eng/ublox
+ https://github.com/dayjaby/ntrip_ros
+ ksnu/link_set, node_set


### Driving direction
---

I tried to use the IMU sensor to know the driving direction of the vehicle, but the data reliability of the sensor was low, so a new algorithm was applied. The value of the driving direction was obtained from the current coordinates and the previous coordinates, and the slope value of the straight line connecting the two points.

![heading 알고리즘](https://user-images.githubusercontent.com/60971835/145800237-cfdd2257-aeb2-4fbd-bb6a-228f4eb89eae.png)

reference
+ odom_heading.py


### Shortest Path
---

Dijkstra's algorithm was used to obtain the shortest path, and the shortest path was visualized by comparing the link and node values of the navigation map data we made.

Links on the generated shortest path are connected with a green line to indicate the global path.

Among the global path, starting with the link closest to the vehicle, links of a specified length are connected with a red line to indicate the local path.


### Path Following
---

For lateral control, pure pursuit algorithm was used. Since the maximum speed of the vehicle is fixed at a low speed of 10 km/h, the Look-Ahead-Distance value to be used in the algorithm is fixed.

For longitudinal control, PID control was used.


### Depth Camera
---

I couldn't buy a radar or lidar, so I used a depth camera. The distance value from the obstacle and the vehicle recognized by the camera is sent to the data topic. If the value is within 1m, the vehicle stops.

![Screenshot from 2021-11-25 16-23-18](https://user-images.githubusercontent.com/60971835/145809722-aeec1403-d55a-4687-83bf-d84e07784393.png)

In addition, if you want to install the pyrealsense2 library for running Intel's realsense-ros on the jetson TX2, you need to build it from the source. (Otherwise, it cannot be installed.)

reference
+ https://github.com/IntelRealSense/librealsense/tree/master/wrappers/python
+ https://github.com/IntelRealSense/realsense-ros

### Driving Test Video
---

This is a video of running the program in school. It can be seen that the vehicle that is out of the path at the beginning finds the path and stops when an obstacle approaches the vehicle.

##### vehicle driving

[![vehicle driving](http://img.youtube.com/vi/WpKtygzY7_A/0.jpg)](http://youtu.be/WpKtygzY7_A=0s)


##### driving data

[![driving_data](https://img.youtube.com/vi/MrNorOyhIks/0.jpg)](https://youtu.be/MrNorOyhIks=0s)

