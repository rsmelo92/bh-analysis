import re
import os
import string

from wordcloud import WordCloud, STOPWORDS

import matplotlib
import matplotlib.pyplot as plt

import numpy as np

import nltk
from nltk.tokenize import word_tokenize 

new_stopwords = [
  'said', 'say', 'may', 'behavior', 'behaviour', 'one', 'often', 'way', 'example', 'know', 'point',
  'make', 'must', 'thing', 'seem', 'see', 'others', 'called', 'made', 'rather', 'mean', 'given',
  'behaviorism', 'chapter', 'american', 'skinner', 'psychology', 'behaviorist', 'much', 'psychologist',
  'although', 'use', 'behavioral', 'psychologists', 'become', 'time', 'might'
]

def get_freq(path, words):
  tokens = word_tokenize(words)
  freq = nltk.FreqDist(tokens)
  plt.ion()
  freq.plot(10, cumulative=True)
  plt.savefig(path, dpi=180, bbox_inches='tight')
  plt.ioff()

def remove_stopwords(text):
  stopwords = nltk.corpus.stopwords.words('english')
  stopwords.extend(new_stopwords)
  stopwords.extend(STOPWORDS)
  word_tokens = word_tokenize(text)
  filtered_sentence = [w for w in word_tokens if not w in stopwords] 

  joined_text = ' '.join(filtered_sentence)
  return joined_text

def clean_data(data):
  # Lower case
  lower_case = data.lower()
  # Remove numbers
  input_str = re.sub(r'\d+', '', lower_case)
  
  #Remove ponctuation
  table = str.maketrans(dict.fromkeys(string.punctuation, ' '))
  no_ponctuation = input_str.translate(table)

  #Remove double space
  no_double = no_ponctuation.replace("\r"," ").replace("\n","")

  # Remove stopwords
  no_stop_words = remove_stopwords(no_double)
  
  # Remove special characters
  no_special = re.sub('\W+',' ', no_stop_words )

  # Change new line for symbol
  cleaned_data = re.sub(r"\s\s+" , " ", no_special)
  return cleaned_data

def write_to_file(file_name, text):
  f = open(file_name, 'a+')
  f.write(text)
  f.close()

def empty_file(file_name):
  try:
    os.remove(file_name)
  except:
    print("No file found to remove")
    pass

def generate_wordcloud(path, text):
  wordcloud = WordCloud(background_color="white", max_words=100, max_font_size=100).generate(text)
  wordcloud.to_file(path)

def parse_file(file):
  text_path = f'./resources/{file}/{file}.txt'
  cleaned_path = f'./resources/{file}/{file}_cleaned.txt'
  print(text_path)
  empty_file(cleaned_path)

  with open(text_path) as f:
    for line in f:
      cleaned = clean_data(line)
      cleaned_add_space = cleaned + ' '
      write_to_file(cleaned_path, cleaned_add_space)

  with open(cleaned_path) as f:
    word_cloud = f'./resources/{file}/word_cloud.png'
    top_10 = f'./resources/{file}/top_10.png'
    empty_file(word_cloud)
    empty_file(top_10)
    raw_text = f.read()
    get_freq(top_10, raw_text)
    generate_wordcloud(word_cloud, raw_text)
