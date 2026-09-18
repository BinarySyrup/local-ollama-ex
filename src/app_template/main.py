"""main.py

CLI entrypoint and core greeting behavior for the app template.
"""
import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python-app",
        description="Minimal Python app template CLI",
    )
    parser.add_argument(
        "--name",
        default="World",
        help="Name to greet",
    )
    return parser


def run(name: str) -> str:
    return f"Hello, {name}!"


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    print(run(args.name))
    return 0
