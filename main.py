# end of sentence indicators
END_OF_SENTENCE = {'.', '!', '?'}

# contents
word_trainer = "The quick brown fox jumped over the lazy dog. The dog then barked really loudly and the fox got scared and ran away!"

# this will create / return dictionary of words from a string
def train(s):
  words = s.split() 
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

print("\n")
print(train(word_trainer))