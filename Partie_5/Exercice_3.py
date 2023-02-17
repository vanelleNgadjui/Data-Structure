import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def huffman(text):
    # Calcul des fréquences des caractères dans le texte
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1

    # Création des nœuds pour chaque caractère et ajout à la file de priorité
    heap = []
    for char, f in freq.items():
        heapq.heappush(heap, Node(char, f))

    # Construction de l'arbre de Huffman
    while len(heap) > 1:
        # Extraction des deux nœuds de fréquence minimale
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Création d'un nouveau nœud avec ces deux nœuds comme enfants
        new_node = Node(None, left.freq + right.freq, left, right)

        # Ajout du nouveau nœud à la file de priorité
        heapq.heappush(heap, new_node)

    # Construction du tableau des codes binaires associés à chaque caractère
    codes = {}
    def traverse(node, code):
        if node.char is not None:
            codes[node.char] = code
        else:
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')
    traverse(heap[0], '')

    # Retour des résultats
    return heap[0], codes

