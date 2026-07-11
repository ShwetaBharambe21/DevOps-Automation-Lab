terraform {
  backend "s3" {
    bucket         = "automation-lab-tf-state-407772390762"
    key            = "ecs/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-lock"
    encrypt        = true
  }
}