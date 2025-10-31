"""
Модуль для токенизации текста различными способами
"""

import re

import nltk
nltk.download('punkt_tab')

import spacy
nlp = spacy.load("en_core_web_sm")

class TextTokenizer:
    def __init__(self):
        """Инициализация токенизатора"""
        pass

    def simple_tokenize(self, text):
        """Простая токенизация по пробелам и знакам препинания"""
        tokens = re.findall(r'\b\w+\b|[^\w\s]', text)
        return [token for token in tokens if token.strip()]

    def nltk_tokenize(self, text):
        """Токенизация с использованием NLTK"""
        try:
            import nltk
            from nltk.tokenize import word_tokenize
            return word_tokenize(text)
        except ImportError:
            return "NLTK не установлен. Установите: pip install nltk"

    def spacy_tokenize(self, text):
        """Токенизация с использованием spaCy"""
        try:
            import spacy
            nlp = spacy.load("en_core_web_sm")
            doc = nlp(text)
            return [token.text for token in doc]
        except ImportError:
            return "spaCy не установлен. Установите: pip install spacy"
        except OSError:
            return "Модель spaCy не найдена. Установите: python -m spacy download en_core_web_sm"

    def tokenize_all(self, text):
        """Применяет все доступные методы токенизации"""
        return {
            'simple': self.simple_tokenize(text),
            'nltk': self.nltk_tokenize(text),
            'spacy': self.spacy_tokenize(text)
        }

def demo():
    """Демонстрационная функция"""
    tokenizer = TextTokenizer()
    sample_text = "Hello, world! This is a test sentence."
    
    results = tokenizer.tokenize_all(sample_text)
    
    print("Результаты токенизации:")
    for method, tokens in results.items():
        print(f"{method}: {tokens}")

if __name__ == "__main__":
    demo()