def run(texte: str, decalage: int) -> str:
    print(f"[DEBUG] Texte = {texte}, Décalage = {decalage}")
    res = []
    for c in texte:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            res.append(chr((ord(c) - base + decalage) % 26 + base))
        else:
            res.append(c)
    return "".join(res)
