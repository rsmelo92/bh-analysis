from handlers import clean_data, generate_wordcloud, create_file

Text="""
Among the behavioral facts at hand were re exes and conditioned re exes, and Watson made the most of
them, but the re ex suggested a push-pull type of causality not incompatible with the nineteenth-century
conception of a machine. The same impression was given by the work of the Russian physiologist Pavlov,
published at about the same time, and it was not corrected by the stimulus-response psychology which
emerged during the next three or four decades.
Watson naturally emphasized the most reproducible results he could #nd, and most of them had been
obtained from animals—the white rats of animal psychology and Pavlov’s dogs. It seemed to be implied that
human behavior had no distinguishing characteristics. And to bolster this claim that psychology was a science,
and to #ll out his textbook, he borrowed from anatomy and physiology, and Pavlov took the same line by
insisting that his experiments on behavior were really “an investigation of the physiological activity of the
cerebral cortex,” although neither man could point to any direct observations of the nervous system which
threw light on behavior. They were also forced into hasty interpretations of complex behavior, Watson arguing
that thinking was merely subvocal speech and Pavlov that language was simply a “second signal system.”
Watson had little or nothing to say about intention or purpose or creativity. He emphasized the technological
promise of a science of behavior, but his examples were not incompatible with a manipulative control.
"""

cleaned = clean_data(Text)
print(cleaned)

create_file('about_behaviorism_cleaned.txt', cleaned)

generate_wordcloud(cleaned)

# with open("./resources/About_Behaviorism.txt") as f:
#   for line in f:
#     (key, val) = line.lower().rstrip("\n").split(": ", 1)
#     formatted_key = stem_and_clean_sentence(key)
#     lawsuit_dictionary[formatted_key] = { "meaning": val, "rawValue": key}

#   return lawsuit_dictionary  
