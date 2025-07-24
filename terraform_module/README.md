# 📦 Terraform Module: IAM Policy from File

This module lets you create an IAM policy in AWS from a previously generated JSON file, such as one created by the `iam-policy-generator` CLI.

## 🔧 Inputs

| Variable      | Description                         | Required |
|---------------|-------------------------------------|----------|
| `policy_name` | Name of the IAM policy              | ✅       |
| `policy_path` | Path to the policy file (JSON)      | ✅       |

## 🚀 Example
```hcl
module "iam_policy" {
  source       = "../terraform-module"
  policy_name  = "my-lambda-policy"
  policy_path  = "./policy.json"
}
```

Make sure the JSON is valid and contains a top-level `Version` and `Statement` block.
