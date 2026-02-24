# Copyright 2025
# ws_30pcd_et3 雷达驱动启动文件 (仅 LiDAR 节点，不含 rviz)

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ws_30pcd_et3_ros2',
            executable='main_node',
            name='main_node',
            namespace='lidar',
            output='screen',
        ),
    ])
