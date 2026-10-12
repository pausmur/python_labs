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
<img width="307" height="116" alt="normalize" src="https://github.com/user-attachments/assets/e0933d26-6452-47f2-8933-9757ad5bc114" />


### Функция tokenize (приводит "нормализированный" текст к формату списка, где объект - слово)
```python
def tokenize(text: str) -> list[str]:
    from re import findall
    return findall(r'\w+(?:-\w+)*', text)
```
<img width="315" height="134" alt="tokenize" src="https://github.com/user-attachments/assets/ed46d45d-4863-4d29-a059-88376721d101" />


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
#### Совместный вывод функций count_freq и top_n
<img width="301" height="85" alt="freq_count+top_n" src="https://github.com/user-attachments/assets/1c22cc9d-18fd-47f9-a6b5-96078997a0b3" />


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
<img width="657" height="177" alt="text_stats" src="https://github.com/user-attachments/assets/304f4378-d706-435b-98e5-91c9128a2be1" />
