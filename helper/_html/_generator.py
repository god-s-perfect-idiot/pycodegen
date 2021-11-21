from operator import sub
from random import randint
import urllib.request

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

def url(domain = ''):
    passthroughDomain = domain
    protocol = ['http', 'https'][randint(0,1)]
    useparts = randint(1,10)
    parts = randint(0,3) if useparts == 3 else 0
    subdomain = ['www', sensible(1)][randint(0,1)]
    domain = domain or sensible(1)
    topleveldomain = ['com', 'in', 'co.uk', 'org', 'edu', 'nz', 'pl', sensible(1)][randint(0,7)]
    newURL = f"{protocol}://{subdomain}.{domain}.{topleveldomain}/"
    for part in range(parts):
        wc = randint(1,5)
        path = sensible(wc).replace(' ', '-')
        newURL += f"{path}/"
    print(newURL)
    try:
        urllib.request.urlopen(newURL)
        return newURL
    except:
        return url(passthroughDomain)
    


print(url())