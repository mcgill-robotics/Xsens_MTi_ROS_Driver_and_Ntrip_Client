from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from pathlib import Path

def generate_launch_description():

    ld = LaunchDescription()

    # Set environment variables to control logging behavior
    ld.add_action(SetEnvironmentVariable('RCUTILS_LOGGING_USE_STDOUT', '1'))
    ld.add_action(SetEnvironmentVariable('RCUTILS_LOGGING_BUFFERED_STREAM', '1'))

    parameters_file_path = Path(get_package_share_directory('xsens_mti_ros2_driver'), 'param', 'xsens_mti_node.yaml')
    
    namespace_arg = DeclareLaunchArgument(
        'namespace',
        default_value='imu',
        description='Namespace for the node'
    )
    
    ld.add_action(namespace_arg)

    xsens_mti_node = Node(
            package='xsens_mti_ros2_driver',
            namespace=LaunchConfiguration('namespace'),
            executable='xsens_mti_node',
            name='xsens_mti_node',
            output='screen',
            parameters=[parameters_file_path],
            arguments=[]
            )
    ld.add_action(namespace_arg)
    ld.add_action(xsens_mti_node)

    return ld
