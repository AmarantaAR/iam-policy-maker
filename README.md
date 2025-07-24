# 🔐 IAM Policy Generator (CLI)

Easily generate AWS IAM policies with custom actions or prebuilt service presets. This project includes a CLI written in Python and optional integration with Terraform.

---

## 📁 Folder Structure
```
iam-policy-generator/
├── iam_policy_generator/      # Core CLI logic
├── examples/                  # Sample output policies
├── tests/                     # Pytest tests
├── terraform-module/          # Optional Terraform integration (if needed)
├── README.md
├── LICENSE
├── Makefile
├── requirements.txt
└── pyproject.toml
```

---

## 🚀 Features
- 🧠 Service presets (S3, Lambda, DynamoDB)
- ⚙️ CLI interface using `typer`
- 📤 Exports IAM policy in valid JSON format
- 🧪 Includes test coverage with pytest
- 🧱 Optional Terraform module to apply policies

---

## 💻 Usage
### 1. Install dependencies
```bash
make install
```

### 2. Generate a policy using a preset
```bash
make run-example
```

Or directly:
```bash
python -m iam_policy_generator.cli generate \
  --preset s3:read-only \
  --resources arn:aws:s3:::example-bucket/* \
  --output examples/sample_output.json
```

### 3. Run tests
```bash
make test
```

### 4. Build the CLI as a package
```bash
make build
```

---

## 🧪 Example Output
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListBucket"],
      "Resource": ["arn:aws:s3:::example-bucket/*"]
    }
  ]
}
```

---

## 🛠 Makefile Targets
| Command         | Description                                      |
|----------------|--------------------------------------------------|
| `make install` | Create venv and install dependencies             |
| `make test`    | Run unit tests                                   |
| `make build`   | Build the CLI for distribution                   |
| `make clean`   | Clean up venv, cache, build artifacts            |
| `make run-example` | Generate a sample policy using a preset     |

---

## 🔄 Integration with Terraform
Use the generated policy with Terraform:
```hcl
resource "aws_iam_policy" "custom" {
  name   = "my-policy"
  policy = file("./generated_policy.json")
}
```

---

## 🧑‍💻 Author
**Victoria** — DevOps & Cloud Engineer  
GitHub: [@AmarantaAR](https://github.com/AmarantaAR)

---

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
