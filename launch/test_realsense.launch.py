import launch
from launch_ros.actions import ComposableNodeContainer, Node
from launch_ros.descriptions import ComposableNode

def generate_launch_description():

    realsense_camera_node = ComposableNode(
        name='camera',
        namespace='camera',
        package='realsense2_camera',
        plugin='realsense2_camera::RealSenseNodeFactory',
        parameters=[{
            'enable_infra1': True,
            'enable_infra2': True,
            'enable_color': False,
            'enable_depth': True,
            'depth_module.emitter_enabled': 0,
            'depth_module.profile': '640x360x90',
            'enable_gyro': True,
            'enable_accel': True,
            'gyro_fps': 200,
            'accel_fps': 200,
            'unite_imu_method': 2,
            'initial_reset': True,
            'publish_tf': False,
            'tf_publish_rate': 0.0,
            'infra1_qos': 'SENSOR_DATA',
            'infra2_qos': 'SENSOR_DATA',
            'imu_qos': 'SENSOR_DATA'
        }],
        extra_arguments=[{
            'use_intra_process_comms': True
        }]
    )


    launch_container = ComposableNodeContainer(
        name='launch_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            realsense_camera_node,
        ],
        output='screen',
    )


    return launch.LaunchDescription([
        launch_container,
    ])