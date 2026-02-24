from launch import LaunchDescription
from launch_ros.actions import Node
import launch_ros.actions
import os
 
def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ws_30pcd_et3_ros2',
            executable='main_node', 
            name='main_node',
            output='screen' 
        ),
        launch_ros.actions.Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(os.path.dirname(__file__), 'points_imu.rviz')] 
        )
    ])