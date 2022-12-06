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

def paire_to_chaine(paire):
    chaine = ''
    for element in paire:
        chaine += str(element)
    return chaine


def set_aretes(k, n):
    sommets = set_sommets(k,n)
    aretes = []
    for x, y in itertools.combinations(sommets, 2):
        node1_copy = x[1:]
        node2_copy = y[:n-2]
        label1 = y[n-2]
        node1_copy2 = x[:n-2]
        node2_copy2 = y[1:]
        label2 = x[n-2]
        if node1_copy == node2_copy:
            aretes.append(paire_to_chaine(x)+ "----" + label1 + "--->" + paire_to_chaine(v2))
        if node1_copy2 == node2_copy2:
            aretes.append(paire_to_chaine(y)+ "----" + label2 + "--->" + paire_to_chaine(v1))
    for element in k:
        aretes.append((element*(n-1)) + "----" + element + "--->"+ (element*(n-1)))
    return aretes

def cycle_euler(k,n):
    sommets = set_aretes(k,n)
    l = []
    for e in sommets:
        debut = e[:n-1]
        fin = e[-n+1:]
        l.append((debut, fin))
    random.shuffle(l)
    G = nx.DiGraph()
    G.add_edges_from(l)
    return [u for u, v in nx.eulerian_circuit(G)]

def get_sequence(k, n: int) -> str:
    cycle = cycle_euler(k,n)
    ret = ''
    for sommet in cycle:
        ret += sommet[-1]
    return ret

def get_bruijn(k,n, total_num):
    all = []
    while len(all) < total_num:
        sequence = get_sequence(k, n)
        if sequence not in all:
            all.append(sequence)
            print (sequence)
    return

def trouver_sol(k, n, password):
    all = []
    total_num = (math.factorial(len(k))**(len(k)**(n-1))//(len(k)**n))
    while len(all) < total_num:
        sequence = get_sequence(k, n)
        #si on trouve le mot de passe dans la séquence
        if password in sequence:
            print ("Mot de passe trouvé dans la séquence : " + sequence)
            return True
        else:
            if sequence not in all:
                all.append(sequence)
    return False