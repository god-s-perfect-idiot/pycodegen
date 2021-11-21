from random import randint
from _loader import _init_
from _elaborate import logic
import word_gen

domNodes = _init_()

def generate_head():
    domTitle = word_gen.sensible(3)
    domHead = f"""
        <head>
            <title>{domTitle}<title>
        </head>
    """
    return domHead

def generate_body():
    nodeCount = randint(30,100)
    body = "<body>"
    for nodeIndex in range(nodeCount):
        node = domNodes[randint(0, len(domNodes) - 1)]
        tag = logic(node)
        body += f"\n{tag}"
    body+="\n</body>"
    return body

def construct():
    return f"""<html>
        {generate_head()}
        {generate_body()}
    </html>"""

def write_to_file(fileName=f"_generated/{word_gen.sensible(1)}.html"):
    with open(fileName, 'w') as f:
        f.write(construct())

print(write_to_file())