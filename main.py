from handlers import clean_data, generate_wordcloud, write_to_file, empty_file
import os

def about_behaviorism():
  empty_file("about_behaviorism/about_behaviorism_cleaned.txt")

  with open("./resources/about_behaviorism/About_Behaviorism.txt") as f:
    for line in f:
      cleaned = clean_data(line)
      cleaned_add_space = cleaned + ' '
      write_to_file('about_behaviorism/about_behaviorism_cleaned.txt', cleaned_add_space)

  with open("./resources/about_behaviorism/about_behaviorism_cleaned.txt") as f:
    generate_wordcloud('./resources/about_behaviorism/word_cloud.png', f.read(), True)

about_behaviorism()
