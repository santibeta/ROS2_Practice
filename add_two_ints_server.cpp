#include <rclcpp/rclcpp.hpp>
#include <example_interfaces/srv/add_two_ints.hpp>

class AddTwoIntsServerNode : public rclcpp::Node
{

public:
    AddTwoIntsServerNode() : Node("pallaringa_server") // MODIFY NAME 
    {}

private:
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<MyCustomNode>(); // MODIFY NAME
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}