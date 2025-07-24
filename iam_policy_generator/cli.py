import typer
from typing import List
from .builder import build_policy, to_json
from .templates import get_actions

app = typer.Typer()

@app.command()
def generate(
    preset: str = typer.Option(None, help="Service preset, e.g. 's3:read-only'"),
    actions: List[str] = typer.Option(None, help="Actions list if not using preset"),
    resources: List[str] = typer.Option(..., help="List of ARNs"),
    output: str = "policy.json"
):
    if preset:
        actions = get_actions(preset)
    if not actions:
        raise typer.BadParameter("You must provide either --preset or --actions")

    policy = build_policy(actions, resources)
    with open(output, "w") as f:
        f.write(to_json(policy))
    typer.echo(f"✅ Policy written to {output}")

if __name__ == "__main__":
    app()