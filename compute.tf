#Create App Server
resource "aws_instance" "app_server" {
  ami           = "ami-05fa00d4c63e32376"
  instance_type = "t2.micro"
  key_name = "ec2_key"
  network_interface {
    device_index = 0
    network_interface_id = aws_network_interface.app_server_nic.id
  }
  tags = {
    Name = "App"
  }
    user_data = <<EOF
        #!/bin/bash
        echo "----------------------------SCRUMEATS SETUP START---------------------------------------------
        echo "download flask files..
        sudo curl https://pastebin.com/raw/UCm4QWYb >> app.py
        sudo curl https://pastebin.com/raw/74i7Cdc9 >> dynamodb_handler.py
        sudo yum install python3
        sudo yum install pip -y
        sudo pip3 install flask
        sudo pip3 install boto3
        sudo pip3 install python-decouple
        sudo python3 app.py
        echo "----------------------------SCRUMEATS SETUP END---------------------------------------------"
    EOF
}
#Create Bastion Box
resource "aws_instance" "bastion" {
  ami           = "ami-05fa00d4c63e32376" #AMAZON AMI
  #ami            = "ami-08c40ec9ead489470" #UBUNTU AMI
  instance_type = "t2.micro"
  #availability_zone = "us-east-1a"
  key_name = "ec2_key"
  network_interface {
    device_index = 0
    network_interface_id = aws_network_interface.web_server_nic.id
  }
  tags = {
    Name = "Bastion Box"
  }
    user_data = <<EOF
        #!/bin/bash
        echo "----------------------------SCRUMEATS SETUP START---------------------------------------------"
        sudo apt-get update -y
        echo "Running initial setup to prepare front end items"
        echo "Retrieve files..."
        sudo wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1c22VxrmPWJ3sReAMG2NsRaV_Wwd4ILQw' -O index.html
        sudo mv index.html /var/www/index.html
        #aws s3 cp index.html s3://scumlordsbucketpublic
        sudo yum  install httpd -y
        sudo systemctl start httpd
        echo "----------------------------SCRUMEATS SETUP END---------------------------------------------"
    EOF
}

#Create Monitoring Server
resource "aws_instance" "Monitoring_Server" {
  ami = "ami-0aacb17f730077b8a"
  instance_type = "t2.micro"
  #availability_zone = "us-east-1a"
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