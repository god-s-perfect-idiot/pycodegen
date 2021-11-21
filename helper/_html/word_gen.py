from random import randint

def gibberish(length, _opts = {}):
    bank = ['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    string = ''
    for i in range(length):
        rand_index = randint(0, len(bank)-1)
        string+= bank[rand_index]
    if(_opts):
        if(_opts['capitalize']):
            string = string.capitalize()
    return string

def sensible(word_count): 
    words = []
    with open('words') as f:
        words = list(f)
    words = [word.strip() for word in words]
    current = []
    for i in range(word_count):
        word_index = randint(0, len(words) - 1)
        current.append(words[word_index])
    return ' '.join(current)
