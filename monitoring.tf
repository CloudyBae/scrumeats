resource "aws_instance" "web-monitoring-instance" {
  ami = "ami-0aacb17f730077b8a"
  instance_type = "t2.micro"
  availability_zone = "us-east-1a"
  key_name = "nagios_key" #Or Terraform_Key

  network_interface {
    device_index = 0
    network_interface_id = aws_network_interface.monitoring-nic.id
  }

  user_data = <<-EOF
              #!/bin/bash
              sudo apt update -y
              sudo apt install apache2 -y
              sudo systemctl start apache2
              sudo bash -c 'echo your very first web server > /var/www/html/index.html'
              EOF
    tags = {
      Name = "Monitoring_Server"
    }
}