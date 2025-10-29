import rclpy
from rclpy.node import Node


def main():
    rclpy.init()                                        # 初始化工作，分配资源
    node = Node('python_node')                          # 创建节点实例
    node.get_logger().info('你好 python 节点！')
    rclpy.spin(node)                                    # 运行节点
    rclpy.shutdown()


if __name__ == '__main__':
    main()

