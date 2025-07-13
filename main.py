def read_logo() -> str:
    with open("logo.txt", "r") as f:
        logo = f.read()

    return "\033[38;2;132;187;246m" + logo + "\033[0m"

def main():
    print(read_logo())

if __name__ == "__main__":
    main()