from decimal import Decimal
import sys

def p_start() -> None:
    to_p = """A: nate reed <nreed@linux.com> 09.10.24
D: Program meant to convert to sci notation because i'm lazy
    """
    print(to_p)

def main() -> None:
    p_start()
    while True:
        try:
            n = float(input("$ "))
            print(f"{Decimal(n):.2E}\n")
        except ValueError:
            print("0\n")
        except KeyboardInterrupt:
            sys.exit(0)

if __name__ == "__main__":
    main()
