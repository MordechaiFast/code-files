def add_it_up(till: int) -> int:
    try:
        return sum(range(till + 1))
    except TypeError:
        return 0

