import sys
from src.lib.text import normalize, tokenize, count_freq, top_n

text = sys.stdin.read()
if text.strip() == '': raise ValueError('Текст для преобразования не может быть пустым')

normal_text = normalize(text)
tokens = tokenize(normal_text)
unique_words = count_freq(tokens)
top_words = top_n(unique_words)

print(f'Всего слов: {len(tokens)}')
print(f'Уникальных слов: {len(unique_words)}')
print('Топ-5 слов:')
for top in top_words:
    print(f'{top[0]} : {top[1]}')
