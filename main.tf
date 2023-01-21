#Create VPC with 1017 IPs
resource "aws_vpc" "main" {
  cidr_block       = "10.0.0.0/22"
  instance_tenancy = "default"

  tags = {
    Name = "main"
  }
}

#Create S3 Bucket for Food Vendor / Food Vendor Customers
resource "aws_s3_bucket" "b" {
  bucket = "scumlordsbucketpublic"
  acl    = "public-read"

  website {
    index_document = "index.html"
    error_document = "404.html"
  }
  tags = {
    Name        = "Static Website Contents"
    Environment = "Dev"
  }
}