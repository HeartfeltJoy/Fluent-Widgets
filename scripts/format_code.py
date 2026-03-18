# -*- coding: utf-8 -*-

import subprocess
import sys


def run_command(command: list[str]) -> None:
    """Run a formatter command and stream its output."""
    try:
        result = subprocess.run(
            command,
            check=True,
            text=True,
            capture_output=True,
            encoding="utf-8",
        )
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
    except subprocess.CalledProcessError as e:
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr, file=sys.stderr)
        raise SystemExit(e.returncode) from e


def format_code() -> None:
    """Format the project with autoflake, isort and black."""
    print("Running autoflake...")
    run_command(["autoflake", "-r", "-i", "qfluentwidgets", "examples", "test"])

    print("Running isort...")
    run_command(["isort", "qfluentwidgets", "examples", "test"])

    print("Running black...")
    run_command(["black", "qfluentwidgets", "examples", "test"])


if __name__ == "__main__":
    format_code()
