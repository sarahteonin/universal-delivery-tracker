# Create an HTTP API Gateway
resource "aws_apigatewayv2_api" "http_api" {
  name          = "delivery-tracker-api"
  protocol_type = "HTTP"

  cors_configuration {
    allow_origins = ["*"]
    allow_methods = ["*"]
    allow_headers = ["content-type"]
    expose_headers = []
    max_age        = 0
    allow_credentials = false
  }
}

# Allow API Gateway to call your Lambda
resource "aws_lambda_permission" "apigw_invoke" {
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.add_delivery.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.http_api.execution_arn}/*/*"
}

# Connect Lambda to API Gateway (called an "integration")
resource "aws_apigatewayv2_integration" "lambda_integration" {
  api_id             = aws_apigatewayv2_api.http_api.id
  integration_type   = "AWS_PROXY"
  integration_uri    = aws_lambda_function.add_delivery.invoke_arn
  integration_method = "POST"
  payload_format_version = "2.0"
}

# Define the route: POST /track
resource "aws_apigatewayv2_route" "post_track" {
  api_id    = aws_apigatewayv2_api.http_api.id
  route_key = "POST /track"
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

# Deploy the API (default stage)
resource "aws_apigatewayv2_stage" "default" {
  api_id      = aws_apigatewayv2_api.http_api.id
  name        = "$default"
  auto_deploy = true
}
