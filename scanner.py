# scanner.py
import sys
from scanner_core import scan

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scanner.py <folder>")
        sys.exit(1)

    target = sys.argv[1]
    scan(target)
