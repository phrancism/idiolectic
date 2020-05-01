import io
import random

CORPUS_FILE_NAME = 'corpus.txt'
NUMBER_OF_LINES = 8

corpus_text = ""
with io.open(CORPUS_FILE_NAME, encoding='utf-8') as corpus:
    corpus_text = corpus.read()
corpus_words = corpus_text.lower().split(' ')

poem = []
for i in range(0,NUMBER_OF_LINES):
    lines = []
    last_index = random.randrange(len(corpus_words))
    last_word = corpus_words[last_index]
    lines.append(last_word)
    while True:
        try:
            index_of_next_occurrence_of_last_word = corpus_words.index(last_word, last_index + 2)
            word_following_next_occurrence_of_last_word = corpus_words[index_of_next_occurrence_of_last_word + 1]

            lines.append(word_following_next_occurrence_of_last_word)

            last_index = index_of_next_occurrence_of_last_word
            last_word = word_following_next_occurrence_of_last_word
        except:
            poem.append(" ".join(lines))
            break
        
print("\n".join(poem))