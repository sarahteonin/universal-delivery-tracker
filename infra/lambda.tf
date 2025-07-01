# This tells Terraform where to find and zip your Lambda code
data "archive_file" "lambda_package" {
  type        = "zip"
  source_dir  = "${path.module}/../backend/add_delivery"
  output_path = "${path.module}/../add_delivery.zip"
}

# This creates the Lambda function itself
resource "aws_lambda_function" "add_delivery" {
  function_name = "addDelivery"
  runtime       = "python3.12"
  handler       = "handler.lambda_handler"  # filename.function_name

  role          = aws_iam_role.lambda_exec_role.arn
  filename      = data.archive_file.lambda_package.output_path

  environment {
    variables = {
      TABLE_NAME = aws_dynamodb_table.deliveries.name
    }
  }

  timeout = 10
}
