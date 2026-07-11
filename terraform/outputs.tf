output "ecr_repository_url" {
  value = aws_ecr_repository.app.repository_url
}

output "cluster_name" {

  value = aws_ecs_cluster.main.name

}

output "execution_role" {

  value = aws_iam_role.ecs_task_execution_role.name

}

output "vpc_id" {
  value = data.aws_vpc.default.id
}

output "alb_dns_name" {
  value = aws_lb.app.dns_name
}