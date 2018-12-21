#!/usr/bin/env python

import rospy
import subprocess 
import sys
#import dynamic_reconfigure.client



node_name_str = "/camera/spinnaker_camera_nodelet"
file_name_str = "/home/marco/spinnaker_ws/src/flir_camera_driver/spinnaker_camera_driver/params/spinnaker-config.yaml"

load_params_str = "rosrun dynamic_reconfigure dynparam load " + node_name_str + " " +file_name_str

#print(load_params_str)
#call(load_params_str)
print("Configuring Camera")
subprocess.call(load_params_str, shell=True)
print("Camera Configured")


# if __name__ == "__main__":
#     rospy.init_node("dynamic_client")
# 
#     client = dynamic_reconfigure.client.Client("dynamic_tutorials", timeout=30, config_callback=callback)
# 
#     r = rospy.Rate(0.1)
#     x = 0
#     b = False
#     while not rospy.is_shutdown():
#         x = x+1
#         if x>10:
#             x=0
#         b = not b
#         client.update_configuration({"int_param":x, "double_param":(1/(x+1)), "str_param":str(rospy.get_rostime()), "bool_param":b, "size":1})
#         r.sleep()