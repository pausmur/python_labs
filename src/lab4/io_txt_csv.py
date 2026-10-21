from pathlib import Path
import csv
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)

    if rows:
        if not(header is None) and len(header) != len(rows[0]):
            raise ValueError('Разная длина')
        for x in rows:
            if len(x) != len(rows[0]):
                raise ValueError('Строки разной длины')
            
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

txt = read_text("data/lab04/input.txt")
write_csv([("word","count"),("test",3)], "data/check.csv")
print(txt)