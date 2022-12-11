# Le programme génére une séquence de de Bruijn d'ordre n et d'un alphabet de k éléments
# Exécution avec la commande : python .\bruijn.py
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
        sommet1 = x[1:]
        sommet2 = y[:n-2]
        etiq1 = y[n-2]
        sommet11 = x[:n-2]
        sommet22 = y[1:]
        etiq2 = x[n-2]
        if sommet1 == sommet2:
            aretes.append(paire_to_chaine(x)+ "----" + etiq1 + "--->" + paire_to_chaine(y))
        if sommet11 == sommet22:
            aretes.append(paire_to_chaine(y)+ "----" + etiq2 + "--->" + paire_to_chaine(x))
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
    print ("Mot de passe non trouvé dans les séquences générées.")
    return False

def affichage(k, n, all):
    sommets = set_sommets(k,n)
    aretes = set_aretes(k,n)
    total_num = (math.factorial(len(k))**(len(k)**(n-1))//(len(k)**n))
    print ("\n--> Vous avez l'alphabet suivant : " + str(k) + ", pour un ordre de " + str(n) + "\n")
    print ("--> Le nombre de sommets : " + str(len(sommets)) + "\nListes des sommets (mots) : " + str(sommets)+ "\n")
    print ("--> Le nombre d'arêtes : " + str(len(aretes)) + "\nListe des arêtes : " + str(aretes)+ "\n")
    print ("--> Le cycle eulérien généré : " + str(cycle_euler(k,n))+ "\n")
    print ("--> La séquence de Bruijn correspondante à ce cycle : " + str(get_sequence(k,n))+ "\n")
    print ("--> Taille de la séquence de Bruijn : " + str(len(k)**n)+"\n")
    print ("--> Nombre total des séquences de de Bruijn : " + str(total_num)+ "\n")
    if all == True:
        print ("--> Toutes les séquences de de Bruijn possibles : ")
        get_bruijn(k,n, total_num)


print ("\n=================== Générateur Suite de de Bruijn ======================\n")

n = input ("Entrez l'ordre n de la suite de de Bruijn : ")
n = int(n)
k = input ("Entrez le nombre d'éléments k de votre alphabet : ")
k = int(k)
#initialize the list with the size of k
l = [0] * k
for i in range(k):
    e = input ("Entrez l'élément " + str(i+1) + " de votre alphabet : ")
    #add each element to the list
    l[i] = e

#get the list of elements entered
alphabet = l

all = False

rep = input ("Souhaitez-vous afficher toutes les suites de de Bruijn possibles ? (o/n) : ")
if rep == "o":
    rep2 = input ("Attention, cela peut prendre du temps !\nEtes-vous sûr de vouloir continuer ? (o/n) : ")
    if rep2 == "o":
        all = True

rep = input ("Souhaitez-vous afficher les résultats (sommets, arêtes, cycle eulérien...) ? (o/n) : ")
if rep == "o":
    print ("\n======================= Affichage des résultats =======================")

    affichage(alphabet,n, all)

    print ("\n=========================== Fin des résultats ===========================\n")

password = input ("Entrez le mot de passe à trouver : ")
trouver_sol(alphabet,n, password)