def run(*args: int) -> list[int]:
    print(f"[TRACE] Arguments reçus : {args}")
    return [x for x in args if x % 2 == 0]
