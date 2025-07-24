import json
from typing import List, Dict

def build_policy(actions: List[str], resources: List[str], effect: str = "Allow") -> Dict:
    return {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": effect,
                "Action": actions,
                "Resource": resources
            }
        ]
    }

def to_json(policy: Dict) -> str:
    return json.dumps(policy, indent=2)