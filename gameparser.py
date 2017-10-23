import string
import items
import containers

# List of key words (feel free to add more)
key_words = ["go", "south", "north", "west", "east", "take", "drop", "read", "hit", "inspect", "left", "right", "up", "down"
            ,"search", "boxes", "desk", "machine", "combine", "craft"]


def filter_words(words, key_words):
    """This function takes a list of words and returns a copy of the list from
    which all words provided in the list key_words have been removed.
    For example:
    """
    filtered_list = []
    for word in words:
        if word.lower() in key_words:
            filtered_list.append(word)
        for item in items.items_list:
        	if word.lower() == item["id"]:
        		filtered_list.append(word)
        for container in containers.containers_list:
            if word.lower() == container["id"]:
                filtered_list.append(word)



    return filtered_list

    
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
    return filter_words(word_list, key_words)
