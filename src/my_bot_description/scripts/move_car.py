#!usr/bin/env/python3
import rclpy
from sensor_msgs.msg import JointState
import time
from rclpy.node import Node
import numpy as np

def main():
    rclpy.init()
    node = Node('car_move')

    Joint_state_pub = node.create_publisher(JointState,'/joint_states',10)

    msg = JointState()
    msg.name =["right_joint","left_joint","caster joint","lider_base"]
    
    msg.position=[1.2,0.45,0.56,1.3]
    while rclpy.ok():
        msg.header.stamp=node.get_clock().now().to_msg() #time matching 
        Joint_state_pub.publish(msg)
        msg.position = msg.position+np.array([0.1,0.1,0.1,0.1])
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()