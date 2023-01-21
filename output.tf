output "server_public_ip" {
  value = aws_eip.eip1.public_ip
}

output "server_private_ip" {
  value = aws_instance.app_server.private_ip
}

output "server_ami" {
  value = aws_instance.app_server.ami
}

output "server_key_name" {
  value = aws_instance.app_server.key_name 
}

output "server_subnet_id" {
  value = aws_instance.app_server.subnet_id
}

output "monitoring_ami" {
  value = aws_instance.Monitoring_Server.ami
}

output "monitoring_key" {
  value = aws_instance.Monitoring_Server.key_name
}

output "monitoring_public_ip" {
  value = aws_eip.eip2.public_ip
}

output "monitoring_private_ip" {
  value = aws_instance.Monitoring_Server.private_ip
}

output "monitoring_subnet_id" {
  value = aws_instance.Monitoring_Server.subnet_id
}