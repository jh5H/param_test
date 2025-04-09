from rclpy.time import Time
from rclpy.node import Node
import rclpy


class LoggerTest(Node):
    def __init__(self):
        super().__init__('logger_test')
        # self.period = 1
        self.count = 1

        # parameter of ROS2
        self.is_debug = self.declare_parameter("is_debug", True).get_parameter_value().bool_value
        self.declare_parameter("period", 1.0)
        self.period = self.get_parameter("period").get_parameter_value().double_value
        self.get_logger().info("is_debug: {}".format(self.is_debug))    
        self.get_logger().info("period: {}".format(self.period))

        # timer of ROS2
        self.timer_ = self.create_timer(self.period, self.timer_callback)

    def timer_callback(self):
        
        
        if self.count % 2 == 0:
            self.get_logger().info(f"{self.count} is a multiple of 2.")

        if self.count % 3 == 0:
            self.get_logger().warn(f"{self.count} is a multiple of 3.")

        if self.count % 5 == 0:
            self.get_logger().fatal(f"{self.count} is a multiple of 5.")

        if self.count % 7 == 0:
            self.get_logger().error(f"{self.count} is a multiple of 7.")

        if self.count % 10 == 0:
            self.get_logger().debug(f"{self.count} is a multiple of 7.")

        if self.is_debug == True:
            self.get_logger().info("Hi")

        else:
            pass
        
        self.count += 1


def main(args=None):

    
    rclpy.init(args=args)
    node = LoggerTest()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()