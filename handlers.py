import re
import string
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 

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

  # Change new line for symbol
  cleaned_data = re.sub(r"\s\s+" , " ", no_double)

  # Remove stopwords
  stop_words = set(stopwords.words('english')) 
  word_tokens = word_tokenize(cleaned_data) 
  filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
  # Rejoin text
  joined_text = ' '.join(filtered_sentence)

  return joined_text

def create_file(file_name, text):
  f = open(f'resources/{file_name}', 'w+')  # open file in append mode
  f.write(text)
  f.close()

def generate_wordcloud(text):
  wordcloud = WordCloud(background_color="white", max_words=100, max_font_size=100).generate(text)

  plt.figure()
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis("off")
  plt.show()
  wordcloud.to_file("img/about_behaviorism/test.png")
