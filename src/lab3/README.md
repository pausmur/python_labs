# Лабораторная 3
## Задание 1
### Функция normalize (приведение текста в нижний регистр "стандартными символами" с помощью casefold)
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold == True: text = text.casefold()
    else: text = text.lower()
    if yo2e == True: text = text.replace('ё','е')
    words = text.split()
    text_norm = ' '.join(words)
    return text_norm
```
![](./images/lab03/normalize.png)

### Функция tokenize (приводит "нормализированный" текст к формату списка, где объект - слово)
```python
def tokenize(text: str) -> list[str]:
    from re import findall
    return findall(r'\w+(?:-\w+)*', text)
```
![](./images/lab03/tokenize.png)

### Функция count_freq (выводит словарь, где записано слово и количество его повторений, слова записаны в порядке убывания)
```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    unique_tokens = sorted(list(set(tokens)))
    return {element: tokens.count(element) for element in unique_tokens}
```

### Функция top_n (выводит топ слов по количеству повторенийб число топа зависит от ввода пользователя)
```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key = lambda kv: (-kv[1], kv[0]))[:n]
```
![](./images/lab03/freq_count+top_n.png)

## Задание 2
### Вывод текста с применением всех функций из задания 1
```python
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
```
![](./images/lab03/text_stats)