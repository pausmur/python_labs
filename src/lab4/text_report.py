import sys
from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab4.io_txt_csv import read_text, write_csv

def text_report():
    try:
        text = read_text('data/lab04/input.txt', encoding='utf-8')
    except FileNotFoundError:
        print('Файл не был найден, попробуйте совершить ввод еще раз')
        sys.exit(1)
    except UnicodeDecodeError:
        print('Введен неверный тип расшифровки')
        sys.exit(1)

    normal_text = normalize(text)
    words = tokenize(normal_text)
    unique_words = count_freq(words)
    top5 = top_n(unique_words)

    print(f'Всего слов: {len(words)}')
    print(f'Уникальных слов: {len(unique_words)}')
    for i in top5:
        print(f'{i[0]}: {i[1]}')

    top_csv = sorted(unique_words.items(), key=lambda kv: (-kv[1], kv[0]))
    write_csv(top_csv, 'data/lab04/report.csv', header = ('word','count'))

if __name__ == '__main__':
    text_report()
