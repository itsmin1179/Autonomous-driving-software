#!/usr/bin/env python

import rospy
import numpy as np
import tf
import math
from pyproj import Proj

from sensor_msgs.msg import Imu
from nav_msgs.msg import Odometry
from sensor_msgs.msg import NavSatFix
from gps_c94_m8p.msg import gps_data

class Converter:
    def __init__(self, zone=52):
        self.gps_sub = rospy.Subscriber("/ublox_gps/fix", NavSatFix, self.navsat_callback)

        self.heading_pub = rospy.Publisher('/heading', gps_data, queue_size=1)
        self.gps_status_msg = gps_data()

        self.e_off_set = 291129.30118863715
        self.n_off_set = 3980221.885665606
        self.old_heading_rad = 0.0
        self.old_heading_degrees = 0.0
        self.old_utm_x = 0.0
        self.old_utm_y = 0.0

        self.proj_UTM = Proj(proj = 'utm', zone = 52, ellps = 'WGS84', preserve_units = False)

        self.heading_msg=gps_data()
        
    def cal_gps_heading(self, new_utm_x, new_utm_y):
        heading_rad = self.old_heading_rad
        heading_degrees = self.old_heading_degrees
        delta_x = new_utm_x - self.old_utm_x
        delta_y = new_utm_y - self.old_utm_y
        
        heading_rad = math.atan2(delta_y, delta_x)

        degrees = heading_rad * 180 / math.pi
        if degrees > 90: degrees = 450 - degrees
        else: degrees = 90 - degrees
        heading_degrees = degrees

        self.old_heading_rad = heading_rad
        self.old_heading_degrees = heading_degrees
    
        self.old_utm_x = new_utm_x
        self.old_utm_y = new_utm_y
        return heading_rad, heading_degrees
        
    def navsat_callback(self, gps_msg):
        self.lat = gps_msg.latitude
        self.lon = gps_msg.longitude

        xy_zone = self.proj_UTM(self.lon, self.lat)
        x = xy_zone[0]-self.e_off_set
        y = xy_zone[1]-self.n_off_set

        rad, degree = self.cal_gps_heading(x, y)
        self.heading_msg.latitude = self.lat
        self.heading_msg.longitude = self.lon
        self.heading_msg.heading_rad = rad
        self.heading_msg.heading_pi = rad
        self.heading_msg.heading_degrees = degree
        self.heading_pub.publish(self.heading_msg)

        
if __name__=='__main__':
    rospy.init_node('gps_imu_parser', anonymous=True)
    gps_parser = Converter()
    rospy.spin()
