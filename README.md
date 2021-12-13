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

