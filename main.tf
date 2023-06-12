terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

resource "aws_ebs_volume" "ebs" {
  availability_zone = var.region
  size              = 2

  tags = {
    createdBy = "terraform"
  }
}