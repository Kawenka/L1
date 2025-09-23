def run(texte: str) -> str:
    print("[INFO] Transformation en cours...")
    mots = texte.split(" ")
    return " ".join(m[::-1] for m in mots)
