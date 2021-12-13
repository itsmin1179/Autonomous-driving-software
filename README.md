# Autonomous driving software

This project was developed to be able to generate navigation map data, follow a route, and stop driving using ros and python.

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

The picture below is the intra-school navigation map data created by our team using GPS data.


reference
+ https://github.com/bao-eng/ublox
+ https://github.com/dayjaby/ntrip_ros


### Driving direction
---

I tried to use the IMU sensor to know the driving direction of the vehicle, but the data reliability of the sensor was low, so a new algorithm was applied. The value of the driving direction was obtained from the current coordinates and the previous coordinates, and the slope value of the straight line connecting the two points.

![heading 알고리즘](https://user-images.githubusercontent.com/60971835/145799719-a45db5b4-e54f-46ab-abd9-b0e9102a083a.png)

reference
+ odom_heading.py
