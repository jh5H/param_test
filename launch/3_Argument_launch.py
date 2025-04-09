from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument


def generate_launch_description():

    period = LaunchConfiguration('period', default=2.0)
    is_debug = LaunchConfiguration('is_debug')

    logger_node = Node(
        package='param_test',
        executable='logger_1',
        name='logger_1',
        parameters=[{
            'period' : period,
            'is_debug' : is_debug,
        }],
        emulate_tty=True,
    )
    
    return LaunchDescription([
        DeclareLaunchArgument(
            'period',
            default_value=period,
            description="period of timer_callback"
        ),

        DeclareLaunchArgument(
            'is_debug',
            default_value="False",
            description="whether print or not"
        ),

        logger_node,
    ])

