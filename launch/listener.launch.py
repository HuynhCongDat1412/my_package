from launch import LaunchDescription
from launch_ros.actions import Node

def genegrate_launch_description():
    return LaunchDescription([
        Node(
            package='demo_node_py',
            executable='listener'
        )
    ])