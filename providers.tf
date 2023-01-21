terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "4.36.1"
    }
    github = {
    source  = "integrations/github"
    version = "~> 4.0"
    }
  }
}
provider "aws" {
    region = "us-east-1"
}