import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    pkg_dir = get_package_share_directory('arena_camera_node')
    config_file = os.path.join(pkg_dir, 'config', 'camera_params.yaml')

    arena_camera_node = ComposableNode(
        package='arena_camera_node',
        plugin='ArenaCameraNode',
        name='arena_camera_node',
        parameters=[config_file],
    )

    container = ComposableNodeContainer(
        name='arena_camera_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[arena_camera_node],
        output='screen',
    )

    

    return LaunchDescription([container])
