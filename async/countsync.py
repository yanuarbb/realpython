import time


def count():
    """TODO: Docstring for count.
    :returns: TODO

    """
    print("One")
    time.sleep(1)
    print("Two")


def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    for _ in range(3):
        count()


if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"Executed in {elapsed:0.2f} seconds.")
