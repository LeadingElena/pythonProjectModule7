import string

class WordsFinder():
    def __init__(self, *file_names):
        self._file_names = file_names
        self._all_words = self.get_all_words()

    def get_all_words(self):
        all_words = {}
        for file in self._file_names:
            with open(file, encoding='utf-8') as open_file:
                text = open_file.read()
                # Удаляем знаки препинания и разбиваем текст на слова
                text = text.translate(str.maketrans('', '', string.punctuation.replace("'", ''))).lower()
                all_words[file] = text.split()
        return all_words

    def find(self, word):
        for name, list_words in self._all_words.items():
            if word.lower() in list_words:
                return {name : list_words.index(word.lower()) + 1}

    def count(self, word):
        for name, list_words in self._all_words.items():
            count_of_word = list_words.count(word.lower())
            return {name : count_of_word}

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего