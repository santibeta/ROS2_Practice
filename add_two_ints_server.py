import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

class AddTwoIntsServerNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_server")
        self.server_ = self.create_service(AddTwoInts, "manuelas", self.callback_manuelas)
        self.get_logger().info("Ta corriendo de lo lindo")
        
    def callback_manuelas(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(str(request.a) + " + " + str(request.b) + " = " + str(response.sum))
        return response
  
def main(args=None):

    rclpy.init(args=args)
    node = AddTwoIntsServerNode()
    rclpy.spin(node)
    rclpy.shutdown()

  
if __name__ == "__main__":
    main()