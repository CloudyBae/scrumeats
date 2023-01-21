#This is our DynamoDB table

resource "aws_dynamodb_table" "basic-dynamodb-table" {
  name           = "Atlanta"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "FoodTruckName"
  range_key      = "ItemName"

  attribute {
    name = "FoodTruckName"
    type = "S"
  }

  attribute {
    name = "ItemName"
    type = "S"
  }

  attribute {
    name = "Price"
    type = "N"
  }

  ttl {
    attribute_name = "TimeToExist"
    enabled        = false
  }

  global_secondary_index {
    name               = "TruckPricing"
    hash_key           = "FoodTruckName"
    range_key          = "Price"
    write_capacity     = 10
    read_capacity      = 10
    projection_type    = "INCLUDE"
    non_key_attributes = ["Price"]
  }

  tags = {
    Name        = "Atlanta-Food-Trucks"
    Environment = "production"
  }
}