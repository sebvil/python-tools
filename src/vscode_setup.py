#!/usr/bin/env python3
"""Sets up Pipenv and settings.json to use in a new VS Code project."""

import argparse
import os
import subprocess

VS_CODE_DIR = ".vscode"
VS_CODE_CONFIG = "settings.json"
SETTINGS = """
{
    "python.formatting.provider": "black",
    "python.linting.pylamaEnabled": true,
    "python.linting.enabled": true,
    "python.linting.pylamaArgs": [
        "--linters=pycodestyle,pylint,mypy,pydocstyle",
        "--ignore=D213,D407,D406"
    ],
    "editor.formatOnPaste": false,
    "editor.formatOnType": true,
    "files.autoSave": "onFocusChange",
    "editor.formatOnSave": true,
}
""".strip()


def run_command(command: str):
    """Run a command.

    Run a commmad, informing the user of the command about to be run/

    Args:
        command (str): The command to run,

    """
    print(f"Running '{command}'")
    subprocess.run(command.split(" "))


parser = argparse.ArgumentParser(
    description=(
        "Set up Python environment for VS Code. This should be run in the root of your project."
    )
)
parser.add_argument(
    "python_version",
    metavar="version",
    type=str,
    help="version of python to use for the project",
)


args = parser.parse_args()
python_version = args.python_version

print("Setting up pipenv")
run_command(f"pipenv install --python {python_version}")
run_command("pipenv install --dev black pylama")


print("Setting up VS Code")
if not os.path.exists(VS_CODE_DIR):
    print(f"Creating directory {VS_CODE_DIR}")
    os.makedirs(VS_CODE_DIR)

with open(f"{VS_CODE_DIR}/{VS_CODE_CONFIG}", "w") as f:
    f.write(SETTINGS)
