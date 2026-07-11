variable "aws_region" {
  default = "ap-south-1"
}

variable "project_name" {
  default = "automation-lab"
}

variable "container_port" {
  default = 5000
}

variable "cpu" {
  default = 256
}

variable "memory" {
  default = 512
}

variable "environment" {
  type    = string
  default = "development"
}