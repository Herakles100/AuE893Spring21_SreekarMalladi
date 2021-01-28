#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def move():
    # Starting a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Input variables
    speed = 1
    distance = 8

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0


    #Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0

    #Loop to move the turtle in an specified distance
    while(current_distance < 7):
        #Publish the velocity
        vel_msg.linear.x = 1
        vel_msg.angular.z = 1    
        velocity_publisher.publish(vel_msg)
        #Taking actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
        #Calculates distancePoseStamped
        current_distance= 1*(t1-t0)
        
    #After the loop, stopping the robot
    vel_msg.linear.x = 0
    vel_msg.angular.z =0
    #Forcing the robot to stop
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass

