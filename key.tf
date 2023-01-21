#Creates a key pair in AWS
resource "aws_key_pair" "ec2_key" {
  key_name   = "ec2_key"
  public_key = tls_private_key.rsa.public_key_openssh
}

#Uses the RSA 4096 bit hash algorithm to generate our private key
resource "tls_private_key" "rsa" {
  algorithm = "RSA"
  rsa_bits  = 4096
}
#Creates a local file that stores the pem file that contains the key
resource "local_file" "ec2_key" {
    content  = tls_private_key.rsa.private_key_pem
    filename = "ec2-key.pem"
}

resource "aws_key_pair" "nagios_key" {
  key_name   = "nagios_key"
  public_key = tls_private_key.rsa.public_key_openssh
}

resource "tls_private_key" "rsa1" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "local_file" "nagios_key" {
    content  = tls_private_key.rsa.private_key_pem
    filename = "nagios_key"
}
