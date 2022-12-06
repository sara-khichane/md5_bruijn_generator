# Le programme génére une séquence de de Bruijn d'ordre n et d'un alphabet de k éléments
# Exécution avec la commande : python .\testbruijn.py
# Suivez les instructions à l'écran

import itertools
import math
import random
import networkx as nx
import matplotlib.pyplot as plt
import itertools

def set_sommets(k, n):
    length = n-1
    return list(itertools.product(k, repeat = n-1))