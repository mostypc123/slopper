import argparse
import sys

import build


def main():
    parser = argparse.ArgumentParser(description="slopper compiler")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    build_parser = subparsers.add_parser("build", help="Build a file")
    build_parser.add_argument("file", help="File to build")
    build_parser.add_argument(
        "-S", action="store_true", help="stop at generating assembly"
    )
    build_parser.add_argument(
        "-v", action="store_true", help="show thinking output and assembly code"
    )
    build_parser.add_argument(
        "-o", dest="outfile", metavar="OUTPUT", help="set an output file"
    )

    args = parser.parse_args()

    if args.command == "build":
        print(f"\033[94;1m::\033[0m \033[1mBuilding {args.file}\033[0m")

        key = build.get_user_api_key()

        code = ""
        try:
            with open(args.file, "r") as f:
                code = "Main entry file:\n" + f.read()
        except Exception:
            print("\033[91mFailed to read file.\033[0m")

        # File is still empty
        if code == "":
            print("\033[91mFile is empty or an internal error occured.\033[0m")
            sys.exit(1)

        asm = build.output_asm(key, code, args.v)

        # Stop at generating assembly; same as in GCC
        if args.S:
            print(asm)
            sys.exit(0)

        # Default output file is a.out; same as in GCC
        outfile = args.outfile or "a.out"

        build.compile_to_outfile(asm, outfile)

    elif args.command is None:
        parser.print_help()


if __name__ == "__main__":
    main()
