def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold == True: text = text.casefold()
    else: text = text.lower()
    if yo2e == True: text = text.replace('ё','е')
    words = text.split()
    text_norm = ' '.join(words)
    return text_norm

def tokenize(text: str) -> list[str]:
    from re import findall
    return findall(r'\w+(?:-\w+)*', text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    unique_tokens = sorted(list(set(tokens)))
    return {element: tokens.count(element) for element in unique_tokens}

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key = lambda kv: (-kv[1], kv[0]))[:n]