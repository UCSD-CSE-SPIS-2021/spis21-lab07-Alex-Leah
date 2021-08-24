import random

# end of sentence indicators
END_OF_SENTENCE = {'.', '!', '?'}

# contents
drake = open('drake.txt')
# draketext = drake.read()
# drakewords = draketext.split()

# this will create / return dictionary of words from a string
def train(s):
  text = s.read()
  words = text.split() 
  word_dictionary = dict()
  word_dictionary[None] = list()
  word_dictionary[None].append(words[0])

  for i in range(len(words) - 1):

    current = words[i]
    next = words[i+1]

    # adds new words
    if current not in word_dictionary:
      word_dictionary[current] = list()
    word_dictionary[current].append(next)

    # checks if end of sentence
    if current[-1] in END_OF_SENTENCE and current != '"':
      word_dictionary[None].append(next)

  return word_dictionary    

# create random sentences
def generate(model, first_word, num_words):
  currentword = first_word
  number_of_words = 0
  print(currentword)
  while True:
    nextword = random.choice(model[currentword]) 
    print(nextword, end = ' ')
    if nextword[-1] in END_OF_SENTENCE or nextword not in model or len(model[nextword]) == 0 or number_of_words == num_words:
      break
    else:
      currentword = nextword 
      number_of_words += 1


# dictionary = train("Yeah baby I like it like that You gotta believe me when I tell you I said I like it like that")
# dictgenerate = generate(dictionary, "like", 15)

drakedictionary = train(drake)
drakegenerator = generate(drakedictionary, "yeah", 20)

 
# print(dictgenerate)
# print(dictionary)
