import argparse
from src.lib.io_helpers import read_text
from src.lib.text import normalize, tokenize,count_freq, top_n

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help='Файл для чтения')
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help='Файл для чтения')
    stats_parser.add_argument("--top", type=int, default=5, help = 'Количество слов для топа (по умолчанию 5)')

    args = parser.parse_args()

    if args.command == "cat":
        try:
            rows = read_text(args.input).splitlines()
        except FileNotFoundError:
            parser.error('Файл пуст или не найден')
        if args.n:
            for cnt in range(1, len(rows) + 1):
                print(f'{cnt} {rows[cnt - 1]}')
        else:
            for row in rows: print(row)

    elif args.command == "stats":
        try:
            text = read_text(args.input)
        except FileNotFoundError:
            parser.error('Файл пуст или не найден')
        if args.top <= 0: parser.error('Топ должен быть больше нуля')
        normal_text = normalize(text)
        tokens = tokenize(normal_text)
        unique_words = count_freq(tokens)
        top_words = top_n(unique_words, n = args.top)

        print(f'Всего слов: {len(tokens)}')
        print(f'Уникальных слов: {len(unique_words)}')
        print(f'Топ-{args.top} слов:')
        for words in top_words:
            print(f'{words[0]}: {words[1]}')

if __name__ == '__main__':
    main()

