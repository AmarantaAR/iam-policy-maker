from iam_policy_generator.builder import build_policy

def test_build_policy():
    actions = ["s3:GetObject"]
    resources = ["arn:aws:s3:::my-bucket/*"]
    result = build_policy(actions, resources)
    assert result["Version"] == "2012-10-17"
    assert result["Statement"][0]["Action"] == actions