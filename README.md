# 🔐 IAM Policy Generator (CLI)

Easily generate AWS IAM policies with custom actions or prebuilt service presets.

## ✨ Features
- Service presets for S3, Lambda, DynamoDB
- CLI with validation and export
- Outputs valid IAM policy JSON

## 🚀 Usage
```bash
pip install -r requirements.txt
python -m iam_policy_generator.cli generate --preset s3:read-only --resources arn:aws:s3:::my-bucket/*
```

## 🧪 Examples
```bash
python -m iam_policy_generator.cli generate \
  --actions s3:PutObject s3:GetObject \
  --resources arn:aws:s3:::my-bucket/* \
  --output write_policy.json
```
