terraform {
  backend "s3" {
    bucket  = "gitops-terraformcode-2026"
    key     = "eks/terraform.tfstate"
    region  = "us-east-1"
    encrypt = true
  }
}
