from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    logger_node = Node(
        package='param_test',
        executable='logger_1',
        name='logger_1',
        parameters=[{
            'period' : '2.0',
            'is_debug' : True,
        }],
        # emulate_tty=True,
    )
    
    return LaunchDescription([
        logger_node,
    ])
