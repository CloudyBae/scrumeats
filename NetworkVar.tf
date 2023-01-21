resource "aws_internet_gateway" "var-gw" {
  vpc_id = aws_vpc.main.id
}