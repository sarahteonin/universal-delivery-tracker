# This creates the Lambda function itself
resource "aws_lambda_function" "add_delivery" {
  function_name = "addDelivery"
  runtime       = "python3.12"
  handler       = "handler.lambda_handler"

  role          = aws_iam_role.lambda_exec_role.arn
  filename      = "${path.module}/../add_delivery.zip"
  source_code_hash = filebase64sha256("${path.module}/../add_delivery.zip")


  environment {
    variables = {
      TABLE_NAME = aws_dynamodb_table.deliveries.name
    }
  }

  timeout = 10
}
