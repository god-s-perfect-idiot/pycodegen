from _generator import gibberish, sensible
from random import randint

def logic(node): 
    node = node.split(',')
    tag = ""
    if(node[0] == 'p'):
        wordCount = randint(30, 100)
        tag = f"""<p>
                {sensible(wordCount)}
            </p>"""
    elif(node[0] == 'a'):
        tag = f"""<a>"""
    elif(node[0] == 'span'):
        wordCount = randint(30, 100)
        tag = f"""<span>
                {sensible(wordCount)}
            </span>"""
    elif(node[0] == 'div'):
        tag = f"""<div>
            </div>"""
    elif(node[0] == 'img'):
        tag = f"""<img>"""
    return tag