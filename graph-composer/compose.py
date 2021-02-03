import os
import re
import string
import random
from graph import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, 'rb') as file:
        text = file.read().decode("utf-8")
        
        # remove [verse 1: artist]
        # include the following line if you are doing song lyrics
        # text = re.sub(r'\[(.+)\]', ' ', text)
        
        text = ' '.join(text.split()) # this is saything turn whitespace into just spaces
        text = text.lower() # make everything lowercase to compare stuff
        text = text.translate(str.maketrans('', '', string.punctuation)) # remove all punctuation
    
    words = text.split() # split on space again
    
    words = words[:1000]
    
    return words

def make_graph(words):
    g = Graph()
    previous_word = None
    # for each word
    for word in words:
        # check that word is in graph, and if not then add it
        word_vertex = g.get_vertex(word)
        
        # if there was a previous word, then add an edge if does not exist
        # if exists, increment weight by 1
        if previous_word: # prev word should be a Vertex
            # check if edge exists from previous word to current word
            previous_word.increment_edge(word_vertex)
        
        previous_word = word_vertex
    
    g.generate_probability_mappings()
    
    return g

def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)
    
    return composition

def main():
    # step 1: get words from text
    #words = get_words_from_text('texts/hp_sorcerer_stone.txt')
    
    # for song lyrics
    words = []
    for song_file in os.listdir(f'songs/{artist}'):
        if song_file == '.DS_Store':
            continue
        print(song_file)
        song_words = get_words_from_text(f'songs/{artist}/{song_file}')
        words.extend(song_words)
    
        # words.extend(get_words_from_text('songs/{artist}/{song}'.format(artist=artist, song=song)))
        
    # step 2: make a graph using those words
    g = make_graph(words)
    
    # step 3: get the enxt word for x number of words (defined by user)
    # step 4: show the user!
    composition = compose(g, words, 100)
    print(' '.join(composition))
    

if __name__ == '__main__':
    print(main('taylor_swift'))