variable "cluster_name" {
  type        = string
  description = "Name of the EKS cluster"
}

variable "cluster_version" {
  type        = string
  description = "Kubernetes version for the EKS cluster"
}

variable "vpc_cidr" {
  type        = string
  description = "CIDR block for the VPC"
}

variable "availability_zones" {
  type        = list(string)
  description = "List of availability zones"
}

variable "private_subnet_cidrs" {
  type        = list(string)
  description = "List of private subnet CIDR blocks"
}

variable "public_subnet_cidrs" {
  type        = list(string)
  description = "List of public subnet CIDR blocks"
}

variable "min_size" {
  type        = number
  description = "Minimum number of nodes in the EKS cluster"
}

variable "max_size" {
  type        = number
  description = "Maximum number of nodes in the EKS cluster"
}

variable "desired_size" {
  type        = number
  description = "Desired number of nodes in the EKS cluster"
}

variable "instance_type" {
  type        = string
  description = "EC2 instance type for the EKS nodes"
}
