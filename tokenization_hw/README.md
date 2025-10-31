# Модуль токенизации текста

## Описание проекта

Создан класс `TextTokenizer` для токенизации текста тремя способами с помощью библиотек:
- `re` - для простой токенизации по регулярным выражениям
- `nltk` - для интеллектуальной токенизации
- `spacy` - для продвинутой лингвистической обработки

## Установка

```bash
# Установка зависимостей
pip install -r requirements.txt

# Установка модели для spaCy
python -m spacy download en_core_web_sm

from tokenizer import TextTokenizer

## Использование 
python
from tokenizer import TextTokenizer

tokenizer = TextTokenizer()
text = "Hello, world! This is a test."

# Все методы сразу
results = tokenizer.tokenize_all(text)

# Отдельные методы
tokens_simple = tokenizer.simple_tokenize(text)
tokens_nltk = tokenizer.nltk_tokenize(text) 
tokens_spacy = tokenizer.spacy_tokenize(text)

## Запуск

# Демонстрация
python demo.py

# Или напрямую
python tokenizer.py

## Методы класса

simple_tokenize() - токенизация по пробелам и знакам препинания

nltk_tokenize() - токенизация с использованием NLTK

spacy_tokenize() - токенизация с использованием spaCy

tokenize_all() - применяет все методы и возвращает словарь с результатами
