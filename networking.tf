#This is our VPC

resource "aws_vpc" "huntvpc" {
  cidr_block = "10.0.0.0/16"
  
  tags = {
    "Name" = "HuntVPC"
  }
}

#This is our internet gateway

resource "aws_internet_gateway" "huntway" {
  vpc_id = aws_vpc.huntvpc.id

}

#This is our route table

resource "aws_route_table" "hunt-route-table" {
  vpc_id = aws_vpc.huntvpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.huntway.id
  }

  route {
    ipv6_cidr_block        = "::/0"
    gateway_id = aws_internet_gateway.huntway.id
  }

  tags = {
    Name = "HuntRoute"
  }
}

#This is our subnet

resource "aws_subnet" "subnet-1" {
  vpc_id     = aws_vpc.huntvpc.id
  cidr_block = "10.0.1.0/24" #could also change to var.subnet_prefix to prompt input
  availability_zone = "us-east-1a"

  tags = {
    Name = "MainSubnet"
  }
}

#This assosicates our route table with our subnet

resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.subnet-1.id
  route_table_id = aws_route_table.hunt-route-table.id
}

#This is our security group

resource "aws_security_group" "allow_web" {
  name        = "allow_web_traffic"
  description = "Allow Web inbound traffic"
  vpc_id      = aws_vpc.huntvpc.id

  ingress {
    description      = "HTTPS"
    from_port        = 443
    to_port          = 443
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    description      = "HTTPS"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    description      = "SSH"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "allow_web"
  }
}

#This is our network interface

resource "aws_network_interface" "web-server-nic" {
  subnet_id       = aws_subnet.subnet-1.id
  private_ips     = ["10.0.1.50"]
  security_groups = [aws_security_group.allow_web.id]

}

#This is our elastic IP

resource "aws_eip" "eip1" {
  vpc                       = true
  network_interface         = aws_network_interface.web-server-nic.id
  associate_with_private_ip = "10.0.1.50"
  depends_on = [aws_internet_gateway.huntway]
  
}

#NIC for monitoring instance
resource "aws_network_interface" "monitoring-nic" {
  subnet_id       = aws_subnet.subnet-1.id
  private_ips     = ["10.0.1.51"]
  security_groups = [aws_security_group.allow_web.id]

}

#EIP for monitoring instance
resource "aws_eip" "eip2" {
  vpc                       = true
  network_interface         = aws_network_interface.monitoring-nic.id
  associate_with_private_ip = "10.0.1.51"
  depends_on = [aws_internet_gateway.huntway]
  
}
