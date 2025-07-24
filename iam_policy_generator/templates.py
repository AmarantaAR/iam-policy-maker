SERVICE_PRESETS = {
    "s3:read-only": {
        "actions": [
            "s3:GetObject", "s3:ListBucket"
        ]
    },
    "lambda:basic-exec": {
        "actions": [
            "lambda:InvokeFunction"
        ]
    },
    "dynamodb:read-write": {
        "actions": [
            "dynamodb:GetItem", "dynamodb:PutItem", "dynamodb:UpdateItem"
        ]
    }
}

def get_actions(preset: str):
    return SERVICE_PRESETS.get(preset, {}).get("actions", [])