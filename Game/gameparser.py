import string
import items
import sched, time, random, os, sys
from pygame import mixer

mixer.init()
typing = mixer.Sound(os.path.dirname(os.path.realpath(__file__)) + "\sounds\\typing.wav")
# List of key words (feel free to add more)
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']



def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string).
    """

    item_list = ""
    for item in items:
        if item_list != "":
            item_list += ", "
            item_list += item["name"]
        else:
            item_list += item["name"]
    return item_list

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". 
    """
    items_string = list_of_items(items)
    if items_string != "":
        type_print("INVENTORY:\n")
        for item in items:
            type_print(" - " + item["name"], 0.0001)



def filter_words(words, skip_words):
    """This function takes a list of words and returns a copy of the list from
    which all words provided in the list key_words have been removed.
    For example:
    """
    filtered_list = []
    for word in words:
        if word.lower() not in skip_words:
            filtered_list.append(word)



    return filtered_list

def type_print(text, speed = 0.02):
    if os.path.isdir(os.getcwd() + "\sounds"):
        typing.play() #Plays the typing sound
    for c in text:
        sys.stdout.write( '%s' % c ) #https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
        sys.stdout.flush()
        time.sleep(speed)
    print("\n")
    if os.path.isdir(os.getcwd() + "\sounds"):
        typing.stop()#Stops the typing sound

def remove_punct(text):
    """This function is used to remove all punctuation
    marks from a string. Spaces do not count as punctuation and should
    not be removed. The funcion takes a string and returns a new string
    which does not contain any puctuation. For example:
    """
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):
            no_punct = no_punct + char
    return no_punct


def normalise_input(user_input):
    """This function removes all punctuation from the string and converts it to
    lower case. It then splits the string into a list of words (also removing
    any extra spaces between words) and further removes all "unimportant"
    words from the list of words using the filter_words() function. The
    resulting list of "important" words is returned. For example:
    """
    # Remove punctuation and convert to lower case
    no_punct = remove_punct(user_input).lower()
    #Strip the string
    no_spaces = no_punct.strip()
    word = ""
    word_list = []
    for char in no_spaces:
        if char != " ":
            word += char
        elif char == " " and word != " " and word != "":
            word_list.append(word)
            word = ""
    word_list.append(word)
    return filter_words(word_list, skip_words)
