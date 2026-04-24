import argparse


def main():
    parser = argparse.ArgumentParser(description="Calculator CLI")
    parser.add_argument("--action", required=True, help="Action to perform: calculate, get-history")
    parser.add_argument("--operation", help="Operation in format: number,operator,number (e.g. 3,plus,9)")
    args = parser.parse_args()


if __name__ == "__main__":
    main()
