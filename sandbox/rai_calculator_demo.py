#!/usr/bin/env python3
"""Small calculator created by rAI autonomy validation."""

from __future__ import annotations

import argparse
import operator

OPERATIONS = {
    "add": operator.add,
    "sub": operator.sub,
    "mul": operator.mul,
    "div": operator.truediv,
}


def calculate(operation: str, left: float, right: float) -> float:
    if operation not in OPERATIONS:
        raise ValueError(f"Unsupported operation: {operation}")
    if operation == "div" and right == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return OPERATIONS[operation](left, right)


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple rAI calculator demo")
    parser.add_argument("operation", choices=sorted(OPERATIONS))
    parser.add_argument("left", type=float)
    parser.add_argument("right", type=float)
    args = parser.parse_args()
    print(calculate(args.operation, args.left, args.right))


if __name__ == "__main__":
    main()
