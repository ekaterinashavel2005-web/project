import argparse
import os
import sys

VERSION = "0.1.0"


def main(argv=None):
    parser = argparse.ArgumentParser(prog="cardgen")
    parser.add_argument("notes", nargs="?", help="путь к Markdown-конспекту")
    parser.add_argument("--version", action="version", version=f"cardgen {VERSION}")
    args = parser.parse_args(argv)
    if not args.notes:
        parser.print_usage(sys.stderr)
        return 2
    if not os.path.isfile(args.notes):
        print(f"Ошибка: файл не найден: {args.notes}", file=sys.stderr)
        return 2
    print(f"CardGen: получен конспект {args.notes}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
