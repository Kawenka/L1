def run(n: int) -> int:
    print(f"[DEBUG] Entrée : {n}")
    if n < 0:
        print("[WARNING] Négatif détecté")
    return abs(n)
