import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    config = os.path.join(
        get_package_share_directory('param_test'),
        'config',
        'config.yaml'
    )

    logger_node = Node(
        package='param_test',
        executable='logger_1',
        name='logger_1',
        parameters=[{
            config
        }],
        emulate_tty=True,
    )
    
    return LaunchDescription([
        logger_node,
    ])
