resource "aws_iam_policy" "custom" {
  name        = var.policy_name
  path        = "/"
  policy      = fileexists(var.policy_path) ? jsonencode(jsondecode(file(var.policy_path))) : "{}"
}