import random

def build_christmas_tree(size, *ornaments):
    """ Build a christmas tree with a size input """
    tree = ''

    # build the tree layer by layer
    for layer_num in range(1, size + 1):
        # determine and add spaces for layer string
        spaces = size - layer_num
        layer = ' ' * spaces

        # determine and add branches and ornaments for layer string
        branches = (layer_num * 2) - 1
        for branch in range(branches):
            if random.randint(1, 4) == 1 and ornaments:
                layer += random.choice(ornaments)
            else:
                layer += '^'
        
        # add layer to tree and enter for next layer
        tree += layer + '\n'
    
    # build tree trunk
    tree += ' ' * (size - 1) + '#' + '\n'
    tree += ' ' * (size - 1) + '#'

    return tree

