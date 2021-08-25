import random
import pandas as pd
import nltk

nltk.download('punkt')
nltk.download('stopwords')
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.classify.util import accuracy

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
        next = words[i + 1]

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
        print(nextword, end=' ')
        if nextword[-1] in END_OF_SENTENCE or nextword not in model or len(
                model[nextword]) == 0 or number_of_words == num_words:
            break
        else:
            currentword = nextword
            number_of_words += 1


# "Stop words" that you might want to use in your project/an extension
stop_words = set(stopwords.words('english'))


def format_sentence(sent):
    ''' format the text setence as a bag of words for use in nltk'''
    tokens = nltk.word_tokenize(sent)
    return ({word: True for word in tokens})


def get_reviews(data, rating):
    ''' Return the reviews from the rows in the data set with the
        given rating '''
    rows = data['Rating'] == rating
    return list(data.loc[rows, 'Review'])


def split_train_test(data, train_prop):
    ''' input: A list of data, train_prop is a number between 0 and 1
              specifying the proportion of data in the training set.
        output: A tuple of two lists, (training, testing)
    '''
    # TODO: You will write this function, and change the return value

    # number going into training
    proportion = int(len(data) * train_prop)
    training = data[:proportion]
    testing = data[proportion:]
    return (training, testing)


def format_for_classifier(data_list, label):
    ''' input: A list of documents represented as text strings
               The label of the text strings.
        output: a list with one element for each doc in data_list,
                where each entry is a list of two elements:
                [format_sentence(doc), label]
    '''
    # TODO: Write this function, change the return value
    big_list = []
    list_length = len(data_list)

    for i in range(list_length):
        text = data_list[i]
        big_list.append((format_sentence(text),label))

    return big_list


def classify_reviews():
    ''' Perform sentiment classification on movie reviews '''
    # Read the data from the file
    data = pd.read_csv("movie_reviews.csv")

    # get the text of the positive and negative reviews only.
    # positive and negative will be lists of strings
    # For now we use only very positive and very negative reviews.
    positive = get_reviews(data, 4)
    negative = get_reviews(data, 0)

    # Split each data set into training and testing sets.
    # You have to write the function split_train_test
    (pos_train_text, pos_test_text) = split_train_test(positive, 0.8)
    (neg_train_text, neg_test_text) = split_train_test(negative, 0.8)

    # Format the data to be passed to the classifier.
    # You have to write the format_for_classifier function
    pos_train = format_for_classifier(pos_train_text, 'pos')
    neg_train = format_for_classifier(neg_train_text, 'neg')

    # Create the training set by appending the pos and neg training examples
    training = pos_train + neg_train

    # Format the testing data for use with the classifier
    pos_test = format_for_classifier(pos_test_text, 'pos')
    neg_test = format_for_classifier(neg_test_text, 'neg')
    # Create the test set
    test = pos_test + neg_test

    # Train a Naive Bayes Classifier
    # Uncomment the next line once the code above is working
    classifier = NaiveBayesClassifier.train(training)

    # Uncomment the next two lines once everything above is working
    print("Accuracy of the classifier is: " + str(accuracy(classifier, test)))
    classifier.show_most_informative_features()

    # TODO: Calculate and print the accuracy on the positive and negative
    # documents separately
    # You will want to use the function classifier.classify, which takes
    # a document formatted for the classifier and returns the classification
    # of that document ("pos" or "neg").  For example:
    # classifier.classify(format_sentence("I love this movie. It was great!"))
    # will (hopefully!) return "pos"

    # TODO: Print the misclassified examples


if __name__ == "__main__":
    classify_reviews()
    print(split_train_test(["A", "B", "C", "D"], 0.25))
    print(split_train_test(["A", "B", "C", "D"], 0.5))
    print(split_train_test(["A", "B", "C", "D"], 0.2))
    print(format_for_classifier(["A good one", "The best!"], "pos"))
    print(format_for_classifier(["It was fantastic", "Absolutely the best I've seen!"], "pos"))

# dictionary = train("Yeah baby I like it like that You gotta believe me when I tell you I said I like it like that")
# dictgenerate = generate(dictionary, "like", 15)

# drakedictionary = train(drake)
# drakegenerator = generate(drakedictionary, "yeah", 20)

# print(dictgenerate)
# print(dictionary)
