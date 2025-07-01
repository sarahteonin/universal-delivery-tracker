resource "aws_dynamodb_table" "deliveries" {
  name         = "Deliveries"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "userId"
  range_key    = "deliveryId"

  attribute {
    name = "userId"
    type = "S"
  }

  attribute {
    name = "deliveryId"
    type = "S"
  }

  tags = {
    Environment = "dev"
  }
}
