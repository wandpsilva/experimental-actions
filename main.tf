terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

resource "aws_ebs_volume" "ebs" {
  availability_zone = "sa-east-1"
  size              = 2

  tags = {
    createdBy = "terraform"
  }
}