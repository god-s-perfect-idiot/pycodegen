def _init_():
    with open('keywords') as f:
        nodes = list(f)
        nodes = [node.strip() for node in nodes]
    return nodes

